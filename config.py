# wifi configuration
conf_wifi_ssid = 'kku-wifi'
conf_wifi_pass = ''

# authentication information
conf_auth_id = "6012345678" # 10-digit without dashed
conf_auth_pw = "your-password-goes-here" # your wifi login password

# optional parameters
conf_sleep_time = 5 # waiting for everything is completely done
conf_timeout = 30 # time out for a long runtime function e.g. WinWiFi.connect()

# xpath and urls
conf_ping_url = "https://www.google.com"
conf_login_url = "https://login.kku.ac.th/"
conf_login_element_id = "username"
conf_login_element_pw = "password"
conf_login_button_xpath = "/html/body/div[2]/div/div/div[1]/div/form/div[4]/div/button"
conf_logout_url = "https://login.kku.ac.th/status"
conf_logout_button_xpath = "/html/body/div[2]/div/div/div[1]/button"

# define the exactly version of chrome driver
# can be downloaded at https://chromedriver.chromium.org/downloads
conf_chrome_driver_path = "chromedriver/95/chromedriver.exe"
