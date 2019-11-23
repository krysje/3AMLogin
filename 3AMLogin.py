from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r"drivers\geckodriver.exe")


driver.get("http://172.16.1.3:8002/index.php?zone=lan&redirurl=http%3A%2F%2Fdetectportal.firefox.com%2Fsuccess.txt")
driver.find_element_by_name("auth_user").send_keys("2017ucp1192")
driver.find_element_by_name("auth_pass").send_keys("Aman@123")
driver.find_element_by_name("accept").click()

time.sleep(5)
driver.quit()
print("Login completed successfully!")
