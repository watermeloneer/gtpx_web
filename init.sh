#! /bin/bash

function init_path() {
    mkdir -p /data/webroot/
    mkdir -p /data/logs/supervisord/
}

function init_basic() {

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
