from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from util import WaitWrapper
from Login import *

my_user_name = '18402868183'
my_password = 'Lcmalcma123'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome('/Applications/chromedriver', options=options)
driver.get("https://leetcode-cn.com/")
wait_wrapper = WaitWrapper(driver)
# login = LoginByPassword(driver)
login = LoginByQQ(driver)

login.login()
# # 登录
# user_password_button = wait_wrapper((By.CSS_SELECTOR, '[data-cypress="sign-in-with-password"]'))
# user_password_button.click()
#
# user_id = wait_wrapper((By.CSS_SELECTOR, '[name=login]'))
# # user_id = driver.find_element(By.CSS_SELECTOR, '[name=login]')
# # user_password = wait_wrapper((By.CSS_SELECTOR, '[name="password"]'))
# user_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
# user_id.send_keys(my_user_name)
# user_password.send_keys(my_password)
# confirm_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
# confirm_button.click()

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