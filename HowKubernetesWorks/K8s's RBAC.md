## 基于角色的权限控制：RBAC

文章地址：[26 | 基于角色的权限控制：RBAC](https://time.geekbang.org/column/article/42154)

1. Kubernetes 项目中，负责完成授权（Authorization）工作的机制，就是 RBAC：基于角色的访问控制（Role-Based Access Control）。

2. Role 和 RoleBinding 对象都是 Namespaced 对象（NamespacedObject），它们对权限的限制规则仅在它们自己的 Namespace 内有效，roleRef 也只能引用当前 Namespace 里的 Role 对象
3. 基本概念：

   - Role：角色，它其实是一组规则，定义了一组对 Kubernetes API 对象的操作权限。
   - Subject：被作用者，既可以是"人"，也可以是"机器"，也可以使你在 Kubernetes 里定义的"用户"。
   - RoleBinding：定义了"被作用者"和"角色"的绑定关系。

4. Role 本身就是一个 Kubernetes 的 API 对象

```yml
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: mynamespace
  name: example-role
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "watch", "list"]
```

4. Namespace 是 Kubernetes 项目里的一个逻辑管理单位。不同 Namespace 的 API 对象，在通过 kubectl 命令进行操作的时候，是互相隔离开的。默认为 default。不提供实际的隔离和多租户能力，仅为"逻辑"上的隔离。

5. RoleBinding 本身也是一个 Kubernetes 的 API 对象。

```yml
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: example-rolebinding
namespace: mynamespace
subjects:

- kind: User
  name: example-user
  apiGroup: rbac.authorization.k8s.io
  roleRef:
  kind: Role
  name: example-role
  apiGroup: rbac.authorization.k8s.io
```

通过 roleRef 字段，RoleBinding 对象就可以直接通过名字，来引用定义的 Role 对象（example-role），从而定义了"被作用者（Subject）"和"角色（Role）"之间的绑定关系。

## 集群概念下的 RBAC

对于非 Namespaced 对象，如 Node（节点），或者一个 Role 需要获取所有 Namespace 的权限

ClusterRole 如下：

```yml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: example-clusterrole
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

ClusterRoleBinding 如下：

```yml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: example-clusterrolebinding
subjects:
  - kind: User
    name: example-user
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: example-clusterrole
  apiGroup: rbac.authorization.k8s.io
```

## Kubernetes 的内置用户——ServiceAccount

```yml
apiVersion: v1
kind: ServiceAccount
metadata:
  namespace: mynamespace
  name: example-sa
```

```yml
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: example-rolebinding
  namespace: mynamespace
subjects:
  - kind: ServiceAccount
    name: example-sa
    namespace: mynamespace
roleRef:
  kind: Role
  name: example-role
  apiGroup: rbac.authorization.k8s.io
```

### 用户组：Group

一个 ServiceAccount，在 Kubernetes 里对应的"用户"的名字是：`system:serviceaccount:<Namespace名字>:<ServiceAccount名字>`
其对应的内置用户组为：`system:serviceaccounts:<Namespace名字>`

### 预留 ClusterRole

在 Kubernetes 中已经内置了很多个为系统保留的 ClusterRole，它们的名字都以 system: 开头。通过`kubectl get clusterroles`查看，这些系统使用的 ClusterRole，是绑定给 Kubernetes 系统组件对应的 ServiceAccount 使用的。
