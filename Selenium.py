from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service

#  Selenium WebDriver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)


jobs = []


for page_num in range(1, 1500):
    driver.get(f'https://jobvision.ir/jobs?page={page_num}')
    time.sleep(3)


    job_cards = driver.find_elements(By.CSS_SELECTOR, "job-card[class='col-12 row cursor px-0 ng-star-inserted']")

    for card in job_cards:
        title_elem = card.find_element(By.CSS_SELECTOR, "div.job-card-title")
        try:
            salary_elem=card.find_element(By.CSS_SELECTOR, "span[class='font-size-12px']")
            salary=salary_elem.text.strip()
            city_elem = card.find_element(By.CSS_SELECTOR, "a[href^='/jobs/category/in-all-cities']")
            city = city_elem.text.strip()
        except:
            city = "خارج از تهران"
            salary="نامشخص"

        jobs.append({'Title': title_elem.text.strip(), 'City': city, 'Salary': salary})




data = pd.DataFrame(jobs)
data.to_excel('Jobs.xlsx', index=False)

print("اطلاعات با موفقیت ذخیره شد در Jobs.xlsx")



