1、docker安装redis
	docker run -d --name redis -p 6379:6379 redis

2、制作django项目镜像
	修改setting.py文件  REDIS_HOST = "127.0.0.1"  改为你准备部署redis所在host的IP，REDIS_PORT改为redis容器映射的端口
	docker build -t mysite .

3、运行容器
	docker run -d  -p 8000:8000 mysite
	