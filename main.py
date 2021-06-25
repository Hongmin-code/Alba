import os
import csv
import requests
from bs4 import BeautifulSoup
from brand import brand_url_list, brand_list, last_page

os.system("clear")

count = 0

for brand_url in brand_url_list : 
  brand = str(brand_list[count])
  print(f"Now scrapping {brand}...")
  jobs = []

  for page in range(last_page(brand_url)) :
    url = f"{brand_url}?page={page+1}&pagesize=50&"
    url_request = requests.get(url)
    job_list = BeautifulSoup(url_request.text, "html.parser").find("div",{"id" : "SubWrap"}).find("div",{"id":"SubContents"}).find("div",{"id":"NormalInfo"}).find("table")

    job_space = job_list.find_all("td",{"class" : "local first"})
    job_title = job_list.find_all("td", {"class" : "title"})
    job_time = job_list.find_all("td",{"class" : "data"})
    job_pay = job_list.find_all("td", {"class" : "pay"})
    job_regdate = job_list.find_all("td",{"class" : "regDate last"})

    space_list = []
    title_list = []
    time_list = []
    pay_list = []
    regdate_list = []

    for space in job_space :
      space_list.append(space.text.strip().replace("\xa0",' '))
    for title in job_title :
      title_list.append(title.find("span", {"class" : "company"}).text.strip())
    for time in job_time :
      time_list.append(time.text)
    for pay in job_pay :
      pay_list.append(pay.text)
    for regdate in job_regdate :
      regdate_list.append(regdate.text.strip())

    
    for data in range(len(job_space)) :
      info = []
      info.append(space_list[data])
      info.append(title_list[data])
      info.append(time_list[data])
      info.append(pay_list[data])
      info.append(regdate_list[data])
      jobs.append(info)

  def save_to_file(jobs) :
    file = open(f"{brand}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "regdate"])
    for j in jobs :
      writer.writerow(j)
    return

  save_to_file(jobs)

  print(f"{brand}.csv is saved!\n")

  count += 1

print("Done!")

