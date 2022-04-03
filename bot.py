import os
import selenium as se
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import random
import csv
os

def clear():
    try:
        os.system('clear')
    except:
        os.system('clear')

clear()

url = input("Enter destination URL: ")
visits = int(input("Enter number of visits: "))

clear()

options = Options()
ua = UserAgent()
chrome_path = '/home/sarwagya/Downloads/chromedriver'
for i in range(visits):
    userAgent = ua.random
    #print(userAgent)
    options.add_argument('user-agent={userAgent}')
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_path)
    driver.get(url)
    driver.set_window_size(10, 10)
    time.sleep(random.randint(8 , 12))
    driver.close()
    print(i + 1)
    #print(i)
    with open('traffic3.log', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(["User Agent"])
        writer.writerow(userAgent)
        #writer.writerows(int(time.time()))
        #writer.writerow(int(i))
driver.quit()
