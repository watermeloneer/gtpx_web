# gtpx_web

特种设备作业人员网上培训项目

## 项目环境

python 3.5.4

依赖：
```shell

cd gtpx_web
pip install -r requirements.txt
```

## 线上部署

```shell

cd /dada/webroot/gtpx_web

git pull

supervisorctl
restart gtpx
```


## log

```
/data/logs/nginx/nginx_access.log
```

## 定时任务

```
/var/spool/cron/crontabs/root
```