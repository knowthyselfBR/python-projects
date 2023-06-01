from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()

driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login")
time.sleep(10)

LOGIN = os.environ.get('LOGIN')

username = driver.find_element(By.TAG_NAME, "input")
username.send_keys(LOGIN)
time.sleep(10)

avancar = driver.find_element(By.XPATH, "//*[contains(text(),'Avançar')]")
avancar.click()
time.sleep(10)

PASSWORD = os.environ.get('PASSWORD')

password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys(PASSWORD)
time.sleep(10)

entrar = driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
entrar.click()
time.sleep(10)

keyword = "produtividade"

driver.get("https://twitter.com/search?q="+keyword+"&src=typed_query")
time.sleep(10)

retweet = driver.find_elements(By.XPATH, "//div[@data-testid='retweet']")
retweet[0].click()
time.sleep(10)

quote_tweet = driver.find_element(By.XPATH, "//*[contains(text(),'Quote Tweet')]")
quote_tweet.click()
time.sleep(10)

input_div_tweet = driver.find_element(By.XPATH, "//div[contains(@class,'public-DraftStyleDefault-block')]")
input_div_tweet.send_keys("Foco, Força e Fé!")
time.sleep(5)

tweet_now = driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
tweet_now.click()
time.sleep(5)