import time
from f import login, login_get
from config import conf_auth_id, conf_auth_pw, conf_sleep_time


login_get(conf_auth_id, conf_auth_pw)
time.sleep(conf_sleep_time)

# https://login.kku.ac.th/?username=6057400031&password=1409900364524
# fyi: in case of ease way to dev easier
