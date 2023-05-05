# base image
FROM ubuntu:18.04
MAINTAINER zq
ENV TZ=Asia/Shanghai
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
    && apt -y dist-upgrade  \
    # 设置时区
    && apt install -y tzdata \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
	# 安装pillow的依赖
	&& apt -y install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev \
    # python3与pip3与中文字符集
    && apt -y install python3-pip locales vim\
    && locale-gen zh_CN.UTF-8 \
    && pip3 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple Django redis sorl-thumbnail requests pillow python-slugify \
	&& apt -y autoremove \
    && rm -rf /var/cache/apk/* \
    && rm -rf /var/lib/apt/lists/*
    
# 解决容器内中文乱码
ENV LANG zh_CN.UTF-8
ENV LANGUAGE zh_CN.UTF-8
ENV LC_ALL zh_CN.UTF-8


WORKDIR /root/mysite/
COPY . /root/mysite/
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000
