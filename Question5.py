# Go to this given URL and solve the following questions
# URL: https://www.youtube.com/@PW-Foundation/videos

# Q5. Write a python program to extract the time of posting of video for the first five videos.


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import os
import time
import requests

url = 'https://www.youtube.com/@PW-Foundation/videos'
DRIVER_PATH = r'chromedriver.exe'
service = Service(DRIVER_PATH)

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)
time.sleep(20) 
html_content = driver.page_source
# print(html_content)
soup = BeautifulSoup(html_content, 'html.parser')
list=soup.find_all('span', class_ = "inline-metadata-item style-scope ytd-video-meta-block")
youtube_time = [list[i+1].text for i in range(2,12,2)]
print(youtube_time)
for i in youtube_time:
    f = open("Question5.csv", "a")
    f.write(f"{i}\n")
    f.close()