#! /bin/bash
# ==================
# 单台服务器初始化
# 
# 1. python
# 2. nginx
# 3. redis
# 4. mysql
# 
# ==================


function init_path() {
    mkdir -p /data/webroot/
    mkdir -p /data/logs/supervisord/
}

function init_redis() {
    apt-get install -y redis-server
    systemctl start redis-server
    systemctl enable redis-server
}

function init_nginx() {
    apt-get install -y nginx
    systemctl start nginx
    systemctl enable nginx
    # 配置文件 /etc/nginx/nginx.conf
    # 自定义配置可放置在 /etc/nginx/conf.d/
}

function int_mysql() {
    sudo apt-get update
    sudo apt-get install -y mysql-server
    # mysql_secure_installation 设置密码
    systemctl start mysql
    # 开机启动
    systemctl enable mysql

    
}

function init_python() {

    sudo apt-get update &&
        sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
            libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
            xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

    curl https://pyenv.run | bash

    export PYTHON_VERSION=3.5.3
    export ENV_NAME=gtpx
    wget http://npm.taobao.org/mirrors/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz -P ~/.pyenv/cache &&
        pyenv install $PYTHON_VERSION &&
        pyenv virtualenv $PYTHON_VERSION $ENV_NAME &&
        pyenv activate $ENV_NAME &&
        pip install --upgrade pip

}
