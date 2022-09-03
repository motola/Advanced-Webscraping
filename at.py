    # importing necessary websraping tools to be used in the project


from bs4 import BeautifulSoup as BS
import csv
from selenium import webdriver
from time import sleep



driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://uk.trustpilot.com/review/www.airbnb.co.uk?aspects=time&page=14')


sleep(10)
page = driver.page_source
print(page)
soup = BS(page, 'lxml')


    # getting the url



authors=[]
location=[]
rating=[]
date=[]
comment=[]



#     # scraping data with soup

for item in soup.select('article', {'class':'paper_paper__29o4A '}):
        # print(item)
        # print('______')
            ls=item.select('aside')[0]('div',{'class':'styles_consumerName__dP8Um'})[0].get_text()
            authors.append(ls)

            ls=item.select('aside')[0]('span')[1].get_text()
            location.append(ls)

            ls=item.select('img')[0]['alt']
            rating.append(ls)

            ls=item.select('time')[0].get_text()
            date.append(ls)
            
            ls=item.select('p')[0].get_text()
            comment.append(ls)
    
    

data = []
for reviews in zip(authors,location,rating,date,comment):
        data.append(reviews)

with open('output18.csv', 'w+', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['Authors','location','rating','date','comment'])
        writer.writerows(data)  
        print("Operation Completed output 18")
 