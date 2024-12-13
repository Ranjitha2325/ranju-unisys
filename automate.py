from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#we are only import webdriver from entire selenium\

#loading paticular driver of browser
#initializing web driver
chrome_driver=webdriver.Chrome()
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
#chrome_driver.get("https://portal.adhocnet.org/")

#Selinum can find elements by number of things
#name ,classanme, id
chrome_driver.find_element(By.NAME,"name").send_keys("Ranju")
chrome_driver.find_element(By.NAME,"email").send_keys("ranjitha12@gmail.com")
chrome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("HelloAzure@234")
chrome_driver.find_element(By.ID,"exampleCheck1").click()
#doing Selenium in element avlues
myselect= Select(chrome_driver.find_element(By.ID,"exampleFormControlSelect1"))
#we can select data by index, visible text
myselect.select_by_index(1)
#myselect.select_by_index("Female")
time.sleep(5)
#using css_selector for radio button
#chrome_driver.find_element(By.CSS_SELECTOR,"#inlineRadio2").click()
chrome_driver.find_element(By.NAME,"inlineRadio2").click();
time.sleep(5)
chrome_driver.find_element(By.NAME,"bday").send_keys("23-12-1999")
chrome_driver.find_element(By.CLASS_NAME,"btn btn-success").click()
time.sleep(8)


#printing title
print("page title : ",chrome_driver.title)
#current url
print("page url : ",chrome_driver.current_url)
#Saving screnshoot
chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot saved")
# closing my driver / stopping  
chrome_driver.quit()
