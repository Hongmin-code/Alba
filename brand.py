import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

url = "http://www.alba.co.kr"
url_request = requests.get(url)
url_soup = BeautifulSoup(url_request.text, "html.parser").find("div",{"id" : "MainSuperBrand"})

main_soup = url_soup.find("ul",{"class" : "goodsBox"})
superbrands = main_soup.find_all("li")
brand_url_list = []
brand_list = []


for brand in superbrands[:-2] :
  brand = brand.find("a").get('href')
  brand_url_list.append(brand)


for brand in superbrands[:-2] :
  brand1 = brand.find("span",{"class" : "company"})
  if brand1 is not None :
    brand1 = brand1.text
    if brand1 == "이자녹스/비욘드/네이처컬렉션" :
      brand1 = '이자녹스 비욘드 네이처컬렉션'
    brand_list.append(brand1)
  else :
    pass



def last_page(url) :
  url_request = requests.get(url)
  job_count = int(BeautifulSoup(url_request.text, "html.parser").find("div",{"id" : "SubContents"}).find("div",{"id" : "NormalInfo"}).find("p").find("strong").string.replace(",",""))

  last_page = page = job_count//50 +1
  return last_page
