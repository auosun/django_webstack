# django_webstack

> 一款基于 Django 和 [WebStackPage](https://github.com/WebStackPage/WebStackPage.github.io) 导航系统

## Installation

克隆代码：  
```
https://github.com/auosun/django_webstack.git
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

运行镜像:
```
$ docker run --name django_webstack -p 8000:8000 -d pikaczy/django_webstack
```

进入容器:
```
$ docker exec -it django_webstack /bin/bash
$$ python manage.py migrate #创建数据库
$$ exit #退出容器
```

重启服务:
```
$ docker restart django_webstack
```


