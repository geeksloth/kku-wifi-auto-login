from f import is_wifi_connected, wifi_connect, is_internet_connected, login
from config import *


if __name__ == '__main__':
	print ("Checking Wifi connection...")
	if is_wifi_connected():
		print ("connected.")
	else:
		print ("disconnected.")
		print ("Attempting to connect: {}".format(conf_wifi_ssid))
		if wifi_connect(conf_wifi_ssid, conf_auth_pw):
			print ("successful.")
		else:
			print ("failed.")
	print ("Checking internet access...")	
	if is_internet_connected():
		print ("successful.")
	else:
		print ("failed.")
		print ("Attempting to login...")
		if (login(conf_auth_id,conf_auth_pw)):
			print ("successful.")
		else:
			print ("failed.")
