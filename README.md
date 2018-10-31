## django-vue-boilerplate

基于 Vue 和 Django（RestFramework）的应用程序模板。


### 依赖环境

- [X] Python 3
- [X] Pipenv - [地址](https://pipenv.readthedocs.io/en/latest/)
- [X] Yarn - [地址](https://yarnpkg.com/en/docs/install#mac-stable)
- [X] Vue Cli 3 - [地址](https://cli.vuejs.org/zh/guide/installation.html)

### 安装

#### 安装模板

```
$ git clone https://github.com/zenghongtu/django-vue-boilerplate django-vue
$ cd django-vue
```

#### 安装项目依赖

```
$ pipenv install --dev & pipenv shell
$ python manage.py migrate
$ cd frontend & yarn install
```

### 运行开发环境

```
$ yarn run serve
```

### 部署

#### 运行打包
```
$ yarn run build
```
'Type 'yes' to continue, or 'no' to cancel:'

输入 ***`yes`***

#### 配置
设置 `backend.settings.prod.py` 中的 `ALLOWED_HOSTS`
- Apache: 修改 `backend.Apache.backend.conf` 中项目路径

#### 上传文件到服务器

### 目录结构

| 位置             |  说明                                   |
|----------------------|--------------------------------------------|
| `/backend`           | Django 项目和后端配置            |
| `/backend/api`       | Django App (`/api`)                        |
| `/frontend`          | Vue App .                                  |
| `/frontend/src/main.js`  | JS 入口文件                 |
| `/frontend/public/index.html` | HTML 入口文件 (`/`)         |
| `/frontend/src/assets`     | 静态文件                              |
| `/backend/dist/`             | 打包后的文件(通过` python manage.py build`) |


### 其他
示例部分代码参考[django-vue-template](https://github.com/gtalarico/django-vue-template/),特别感谢@[gtalarico](https://github.com/gtalarico)