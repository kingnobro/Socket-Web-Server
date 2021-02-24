# Socket-Web-Server
自制 Socket Web Server + MVC 框架



## 简介

- 底层通过 **Socket** 进行通信，实现对 HTTP 请求和响应进行**监听、收发、解析**功能
- 整体的实现基于 **Model View Controller(MVC)** 架构，实现数据层、视图层、控制层的解耦
    - Model 层使用基于 SQL 语句的自制 **ORM**，封装了 **CURD** 接口
    - View 层使用 **Jinja2** 渲染模板，通过使用模板简化网页生成
    - Controller 层利用高阶函数和字典实现路由分发和管理，使用装饰器实现权限验证
- 基于该框架实现了用户管理(登录、注册)，实现了类似微博评论与删除功能
- 实现了基于 **AJAX** 的留言板



## 环境部署

- MacOS
- MySQL
- Python 3.6



## 本地测试

### 登录

![](https://tva1.sinaimg.cn/large/008eGmZEgy1gnyvhyoxe2g312w0ci4qq.gif)

### 注册

![](https://tva1.sinaimg.cn/large/008eGmZEgy1gnyvie1nhug312w0cib2a.gif)

### 微博

![](https://tva1.sinaimg.cn/large/008eGmZEgy1gnyvjk5rxsg312w0cihdw.gif)

- 微博的增、删、改
- 删除和修改微博的功能有权限验证
- 博主可以删除他人评论，但不能修改他人评论；评论者可以删改自己的评论

### AJAX Todo

![](https://tva1.sinaimg.cn/large/008eGmZEgy1gnyviyuweyg312w0cikjn.gif)

- 基于 **AJAX** 的异步处理，实现无刷新下与服务器交换数据并更新网页内容

