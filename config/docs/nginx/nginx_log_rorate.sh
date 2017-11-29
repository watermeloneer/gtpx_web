#!/usr/bin/env bash

LOGS_PATH=/data/logs/nginx
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
#按天切割日志
mv ${LOGS_PATH}/nginx_access.log ${LOGS_PATH}/nginx_access.log.${YESTERDAY}
#向 Nginx 主进程发送 USR1 信号，重新打开日志文件，否则会继续往mv后的文件写内容，导致切割失败.
kill -USR1 `ps axu | grep "nginx: master process" | grep -v grep | awk '{print $2}'`
#删除7天前的日志
cd ${LOGS_PATH}
find . -mtime +20 -name "*20[1-9][3-9]*" | xargs rm -f
exit 0