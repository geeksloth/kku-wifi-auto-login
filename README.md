# kku-wifi-auto-login
A python script to auto login to KKU-WiFi.

I developed this script since very long time ago. To use this scrip, we must use the same version of `chromedriver` with your `Google Chrome` installed on your OS. It properly works like a charm in Windows, but I had never tested on the other OS, but It might works as well I think :)

To use this script, you need to follow the University's policies and keep the usage in legal purpose. If you have any question or want to contribute this project, feel free to contact me or fork this repo to play by yourself.
Have fun :)

# Prerequisites
You have to prepare your `Python` Interpreter and it's required dependencies:
```bash
pip install -y requests winwifi wrapt-timeout-decorator
```
Then use Windows Scheduler to run the script at the specific time of day or week. Which are `login.py`, `logout.py`, and `watchdog.py` as you desire.
