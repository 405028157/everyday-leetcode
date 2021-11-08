from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from util.DelayUtil import WaitWrapper
from util.Login import *

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome('/Applications/chromedriver', options=options)
driver.get("https://leetcode-cn.com/")
wait_wrapper = WaitWrapper(driver)
login = LoginByPassword(driver)
# login = LoginByQQ(driver)

login.login()

# 点击头像，点击名称进入个人主页
profile_photo = driver.find_element(By.CSS_SELECTOR, '.css-17dlube-AvatarWrapper')
profile_photo.click()
my_user_name = driver.find_element(By.CSS_SELECTOR, '.css-1mlggsb-UserName').find_element(By.CSS_SELECTOR, 'a')
my_user_name.click()

# 切换到新的页面
windows = driver.window_handles
driver.switch_to.window(windows[-1])

# 找提交记录
submits = driver.find_element(By.CSS_SELECTOR, '[data-key="submissions-content"]').find_element(By.CSS_SELECTOR, 'div') \
    .find_elements(By.CSS_SELECTOR, '.css-ex16d6-Timestamp')

submit_time = [submit.text for submit in submits]
submit_time = list(filter(lambda submit : submit.__contains__('小时'), submit_time))
today_sumbit_nums = len(submit_time)

problems = driver.find_element(By.CSS_SELECTOR, '[data-key="submissions-content"]').find_element(By.CSS_SELECTOR, 'div') \
    .find_elements(By.CSS_SELECTOR, 'a')

# debug 输出
for i in range(today_sumbit_nums):
    cur_problem = problems[i]
    print(cur_problem.text, cur_problem.get_property('href'))

for i in range(today_sumbit_nums):
    cur_problem = problems[i]
    driver.get(cur_problem.get_property('href'))
    driver.find_element(By.CSS_SELECTOR, '[data-key="submissions"]').click()
    submit_historeis = driver.find_element(By.CSS_SELECTOR, '.ant-table-tbody').find_elements(By.CSS_SELECTOR, 'a')
    for submit_history in submit_historeis:
        if submit_history.text.__contains__('通过'):
            driver.get(submit_history.get_property('href'))
            code = driver.find_element(By.CSS_SELECTOR, 'code')
            print(code.text)
            break