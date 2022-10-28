from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv
name_of_field=input("Enter the name of field you ant to search :-")
followers_from=input("Enter the no of followers from which the range should start :-")
foll_to=input("Enter the no of followers from which the range should end :-")
file_name=input("Enter the filename you want to save details in :-")
main_deatils=[]
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("user-data-dir=C:/Users/Dell/AppData/Local/Google/Chrome/User Data")

chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)
url='https://toolzu.com/search-instagram-profiles/#faq1'
driver.get(url)
search_box = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='instagramsearchform-username']")))
search_box=driver.find_element(By.XPATH,"//input[@id='instagramsearchform-username']")
search_box.send_keys(name_of_field)
followers_scrap_from= wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='instagramsearchform-followersfrom']")))
followers_scrap_from=driver.find_element(By.XPATH,"//input[@id='instagramsearchform-followersfrom']")
followers_scrap_from.send_keys(followers_from)
followers_scrap_to=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='instagramsearchform-followersto']")))
followers_scrap_to=driver.find_element(By.XPATH,"//input[@id='instagramsearchform-followersto']")
followers_scrap_to.send_keys(foll_to)
search_button=driver.find_element(By.XPATH,"//*[@type='submit']")
driver.execute_script("arguments[0].click();", search_button)
no_of_users=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='col-md-6 col-lg-6 mb-6']")))
no_of_users=driver.find_elements(By.XPATH,"//div[@class='col-md-6 col-lg-6 mb-6']")
no_of_users=len(no_of_users)
i=0
j=0
user_detail=[]
while(j<10):
   while(i <  no_of_users):
      usernames=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='mb-2']")))
      user_name=driver.find_elements(By.XPATH,"//div[@class='mb-2']")[i].text
      user_detail.append(user_name)
      try:
         email=driver.find_element(By.XPATH,f"/html/body/main/div/div[2]/div/div/div/div{[i+1]}/div/div/div[4]/span")
         user_detail.append(email.text)
         print(f"username={user_name} ; email={email.text}")
      except:
         email="---"
         user_detail.append("---")
         print(f"username={user_name} ; email={email}")
   
      main_deatils.append(user_detail)
      user_detail=[]
   
      i+=1
   # time.sleep(100)
   i=0
   next_button=driver.find_element(By.XPATH,"//span[@class='d-none d-sm-inline-block mr-1']")
   driver.execute_script("arguments[0].click();", next_button)
   time.sleep(10)
   j+=1
header = ['Username','Emails']
with open(f'{file_name}.csv', 'w', encoding='UTF8', newline='') as f:
      writer = csv.writer(f)

      # write the header
      writer.writerow(header)

      # write multiple rows
      writer.writerows(main_deatils)   

