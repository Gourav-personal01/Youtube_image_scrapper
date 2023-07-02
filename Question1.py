# Go to this given URL and solve the following questions
# URL: https://www.youtube.com/@PW-Foundation/videos
# Q1. Write a python program to extract the video URL of the first five videos.

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
list=soup.find_all('a', class_ = "yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media")
youtube_links = ["https://www.youtube.com" + list[i]["href"] for i in range(2,7)]
print(youtube_links)

for i in youtube_links:
    f = open("Question1.csv", "a")
    f.write(f"{i}\n")
    f.close()