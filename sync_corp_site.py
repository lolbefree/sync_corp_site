import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from threading import Thread
import pyautogui
from selenium.webdriver.chrome.options import Options
import subprocess
import psutil

# subprocess.Popen(["powershell.exe",
#               "C:\\UserProfile.MIMSync\\sync.ps1"],)
#
# PROCNAME = "chromedriver.exe"
# time.sleep(60)

hostname = ''
proxy_username = ''
proxy_password = ""
chrome_options = Options()
chrome_options.add_argument('--proxy-server={}'.format(hostname))


driver = webdriver.Chrome(ChromeDriverManager().install())
def enter_proxy_auth(proxy_username, proxy_password):
    time.sleep(1)
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')



def open_a_page(driver, url):
    driver.get(url)


Thread(target=open_a_page, args=(driver, hostname)).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()
time.sleep(7)

for tab in range(22):
    pyautogui.press("tab")
time.sleep(3)
pyautogui.press("enter")

# time.sleep(20)
# for proc in psutil.process_iter():
#     # check whether the process name matches
#     if proc.name() == PROCNAME or proc.name() == "chrome.exe":
#         proc.kill()