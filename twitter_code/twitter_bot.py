from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
import xlsxwriter
import datetime
import tweepy
import json
import socket

#Twitter configuration
API_KEY = 'ENTER API KEY HERE'
API_SECRET = 'ENTER API SECRET HERE'
ACCESS_KEY = 'ENTER ACCESS KEY HERE'
ACCESS_SECRET = 'ENTER ACCESS_SECRET HERE'
import json
import tweepy
import requests
import config

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Getting Dates
TodayDate = datetime.datetime.now()
year = TodayDate.strftime("%Y")
month = TodayDate.strftime("%m")
day = TodayDate.strftime("%d")
print(year + month + day)

PATH = r"C:\Users\jamin\OneDrive\Desktop\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path = PATH, options=options)

#Getting current day
driver = webdriver.Chrome(executable_path = PATH)
driver.get(r"https://www.mlb.com/transactions/" + year + "/" + month + "/" + day)

search_paternity = "activated"
search_pat = "from the paternity list"
players_dct = {}


def check_next_page():
    temp = driver.find_elements("xpath",r"//a[normalize-space()='Next »']")
    if len(temp) == 0:
        return False
    else:
        return True

def find_name(page):
    driver.execute_script("window.scrollTo(0, 2000)") 
    batter_name = driver.find_elements(By.CLASS_NAME, "player-link")
    transaction_detail = driver.find_elements(By.CLASS_NAME, "description")
    team_detail = driver.find_elements(By.CLASS_NAME, "club-link")
    batter_index = 0
    for i in range(len(batter_name)):
        if batter_name[batter_index].text not in transaction_detail[i].text:
            batter_index = batter_index - 1
        if search_pat in transaction_detail[i].text and search_paternity in transaction_detail[i].text:
            players_dct[batter_name[batter_index].text] = str(team_detail[i].text)
        batter_index = batter_index + 1

def get_players_activated(page):
    time.sleep(2)
    find_name(driver.page_source)
    time.sleep(2)
    while check_next_page():
        driver.find_element("xpath",r"//a[normalize-space()='Next »']").click()
        find_name(page)
        time.sleep(2)

get_players_activated(driver.page_source)
driver.close()
def tweet_players():
    for key in players_dct:
        api.update_status(str(key) + " has been activated from the paternity list today for the " + str(players_dct[key]) + " today.")

tweet_players()


