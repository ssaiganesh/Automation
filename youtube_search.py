#installed chocolatey using adminstrator rights
#installed selenium package
#using choco installed chromedriver
from selenium import webdriver  #use this always
from webdriver_manager.chrome import ChromeDriverManager #use this always

driver = webdriver.Chrome(ChromeDriverManager().install()) #use this always
driver.get('https://youtube.com') #url for where you want to get request 
searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input') #copied xbox from inspect of search box in youtube after opening from previous comamnd
searchbox.send_keys('Python Automation') #this is what is keyed in search box
searchbutton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button') #search button xpath
driver.execute_script("arguments[0].click();", searchbutton)
