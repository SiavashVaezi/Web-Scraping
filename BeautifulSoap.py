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
    # for g in movie_genre:
    #     Genre.append(g.get_text(strip=True))
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







