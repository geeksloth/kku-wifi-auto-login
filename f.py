import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import winwifi
from wrapt_timeout_decorator import *
from config import *
import webbrowser


def is_wifi_connected(timeout=5)->bool:
	connected_interfaces = winwifi.WinWiFi.get_connected_interfaces()
	if connected_interfaces:
		return True
	else:
		return False

@timeout(conf_timeout)
def wifi_connect(ssid:str=conf_wifi_ssid, passwd:str=conf_wifi_pass)->bool:
	winwifi.WinWiFi.connect(ssid, passwd, remember = True)
	time.sleep(conf_sleep_time)
	return is_wifi_connected()

def is_internet_connected(url:str=conf_ping_url, timeout=5)->bool:
	try:
		request = requests.get(url, timeout=timeout, allow_redirects=False)
		print(request.status_code)
		if request.status_code!=200:
			return False
		return True
	except (requests.ConnectionError, requests.Timeout) as e:
		print(e)
		return False

@timeout(conf_timeout)
def login(username:str,password:str)->bool:
	try:
		browser = webdriver.Chrome(executable_path=conf_chrome_driver_path)
		browser.get(conf_login_url)
		time.sleep(0)
		browser.find_element_by_id(conf_login_element_id).send_keys(username)
		browser.find_element_by_id(conf_login_element_pw).send_keys(password)
		browser.find_element_by_xpath(conf_login_button_xpath).click()
		time.sleep(conf_sleep_time)
		return True
	except Exception as e:
		print(e)
		return False

@timeout(conf_timeout)
def login_get(username:str,password:str)->bool:
	try:
		url = 'https://login.kku.ac.th/?username='+username+'&password='+password
		webbrowser.get("google-chrome").open(url)
		return True
	except Exception as e:
		print(e)
		return False

@timeout(conf_timeout)
def logout()->bool:
	try:
		browser = webdriver.Chrome(executable_path=conf_chrome_driver_path)
		browser.get(conf_logout_url)
		time.sleep(0)
		browser.find_element_by_xpath(conf_logout_button_xpath).click()
		time.sleep(conf_sleep_time)
		return True
	except Exception as e:
		print(e)
		return False
