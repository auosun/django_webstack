# Django_Webstack

> 一款基于 Django 和 [WebStackPage](https://github.com/WebStackPage/WebStackPage.github.io) 导航系统

## Future

1. Webstack页面 可配置
2. 优化Django-Admin显示
3. 添加 about page

## Installation

克隆代码：  
```
$ git clone https://github.com/auosun/django_webstack.git
```

### Docker 
> 基于 Docker Django官方镜像构建

构建镜像：
```
$ docker build -t django_webstack .
```

拉取镜像:
```
$ docker pull pikaczy/django_webstack
```

使用本地Django代码运行镜像:
```
$ docker run --name django_webstack -v <Django代码目录>:/usr/src/app -w /usr/src/app -p 8000:8000 -d pikaczy/django_webstack
```

直接运行镜像:
```
$ docker run --name django_webstack -p 8000:8000 -d pikaczy/django_webstack
```

进入容器:
```
$ docker exec -it django_webstack /bin/bash
$$ python manage.py makemigrations webstack
$$ python manage.py migrate 
$$ python manage.py createsuperuser #创建管理员用户
$$ exit #退出容器
```

重启服务:
```
$ docker restart django_webstack
```

## Usage
主页: ```http://localhost:8000```  
管理员界面: ```http://localhost:8000/admin```

分组和站点排序：以权重参数降序排列

## Thanks
前端设计：[**WebStackPage**](https://github.com/WebStackPage/WebStackPage.github.io)

Web框架：[**Django**](https://github.com/django/django) 后台框架使用 Django-Admin 
