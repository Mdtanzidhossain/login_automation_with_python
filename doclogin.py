from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost/clinicare/doctor.php")
# print(driver.title)



input_user = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/center/form/div/div[2]/input')
input_pass = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/center/form/div/div[4]/input')

input_user.send_keys("ali@gmail.com")
time.sleep(5)
input_pass.send_keys("65656")

btnSubmit = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/center/form/a/input')
btnSubmit.click()


while True:
	pass