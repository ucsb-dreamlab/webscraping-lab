from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.scrapethissite.com/pages/ajax-javascript/")
button = driver.find_element(by=By.ID, value="2015")
button.click()
sleep(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.find(class_='film').prettify())
driver.close()