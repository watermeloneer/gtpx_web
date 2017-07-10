#!/usr/bin/env bash
export RUN_ENV=deploy
/Users/turkey/.pyenv/versions/web/bin/supervisord -c /etc/supervisor/supervisord.conf
# sudo /Users/turkey/.pyenv/versions/web/bin/supervisorctl -c /etc/supervisor/supervisord.conf start celery:
# sudo /Users/turkey/.pyenv/versions/web/bin/supervisorctl -c /etc/supervisor/supervisord.conf start celerybeat: