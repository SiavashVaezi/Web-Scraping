## Web-Scraping Portfolio Projects
Welcome to my Web-Scraping repository. Here you can find my projects with different python libraries. In every project I try to enhance my ability in using different scrapy method to extract
data from the web.

## About Me
A passionate data science learner with a keen interest in business analysis through data-driven strategies. I thrive on combining technical expertise with analytical skills to craft intelligent solutions for complex challenges. I strongly believe in optimizing business processes and creating positive impacts by leveraging the power of data. Currently, I am dedicated to expanding my knowledge and skills in data analysis and information-based decision-making.

## Project 1: Movie Platform (BeautifulSoup)

```python
import pandas as pd
from bs4 import BeautifulSoup
import requests
from pandas.core.computation.ops import isnumeric

title=[]
Genre=[]
Rate=[]
rate=[]

for page_number in range(1,100):
    url = f'https://www.uptvs.com/category/moviesz/page/{page_number}'
    response=requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup=BeautifulSoup(response.text, 'html.parser')

    movie_title=soup.select('a.text-dark')
    # movie_genre = soup.('i.ficon-menu-button text-gray small-12 d-inline-block pl-1')
    movie_rate=soup.select('span.text-gray-2')
    for t in movie_title[3:]:
        title.append(t.get_text(strip=True))
    for r in movie_rate:
        rating=r.get_text(strip=True)
        if rating.replace('.', '', 1).isdigit():
            if float(rating)<=10:
                Rate.append(str(float(rating)))

# rate += ["Unknown"] * (len(title) - len(rate))


if not title or not Rate :
    print("Warning: No job data extracted. Check your selectors.")


print(f"Title count: {len(title)}, Rate count: {len(Rate)}")

data = pd.DataFrame({'Title': title, 'Rate': Rate})

data.to_excel('Movies.xlsx', index=False, engine='xlsxwriter')

## Project 2: Job Search Platform (Selenium)
In the first project I used selenium library to extract data from one of the main job search platform. Here are the steps I took in this project:
1) Importing Libraries
   
      ```python
      from selenium import webdriver
      from selenium.webdriver.common.by import By
      import time
      import pandas as pd
      from selenium.webdriver.chrome.service import Service
3) Selenium Web-Driver
      ```python
      service = Service("chromedriver.exe")
      driver = webdriver.Chrome(service=service)
4) Use For-Loops to Scraping in 1500 pages for extracting Job-Titles/Locations/Salaries
      ```python
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

4) Use Pandas to save the extracted data to a excel file
      ```python
      data = pd.DataFrame(jobs)
      data.to_excel('Jobs.xlsx', index=False)


