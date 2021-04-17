import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from logging import StreamHandler, Formatter, INFO, getLogger


class Selenium_Interface:
    url = None

    userdata_dir = 'UserData'
    options = Options()
    options.add_argument('--user-data-dir=' + userdata_dir)

    # Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
    # #options.set_headless(True)

    def __init__(self):
        self.driver = webdriver.Chrome(options=self.options)





    driver.get(url)
    res = driver.find_elements_by_class_name("uniCartNum")
    if len(res) == 0:
        getLogger().info("no switch found 404")
    else:
        getLogger().info("switch has been found")
        # ``` 自動注文へ ```
        break
    if count > lim:
        break

    time.sleep(interval)
    count += 1
