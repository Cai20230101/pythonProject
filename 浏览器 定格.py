from selenium import webdriver
import time
from pathlib import Path
from selenium.webdriver.common.by import By
import pickle

session_file = "C://Users//Cai//Desktop//123.txt"
def create_driver():
    driver = webdriver.Chrome()
    with open(session_file, 'wb') as f:
        params = {"session_id": driver.session_id}
        pickle.dump(params, f)
    return driver

if not Path(session_file).exists():
    driver = create_driver()
else:
    with open(session_file, 'rb') as f:
        params = pickle.load(f)
        try:
            driver = webdriver.Remote(command_executor=params["server_url"])
            driver.quit()  # 退出start_session新开的空白浏览器
            driver.session_id = params["session_id"]
            driver.execute_script('window.open("");')
            driver.switch_to.window(driver.window_handles[-1])
        except:
            driver = create_driver()


# 打开网页
driver =create_driver()
#
driver.get("https://www.taobao.com")
# # browser.implicitly_wait(1)
# driver.maximize_window()

