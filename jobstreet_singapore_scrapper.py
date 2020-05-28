import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

dataframe = [[]]
columns = ["title","company_name","posted_at","salary","years_of_experience", "link"]


for i in range(1,50):

	home_url = "https://www.jobstreet.com.sg/en/job-search/data-science-jobs-in-singapore/"
	url = home_url+str(i)+"/"
	print("Scrapping data from Page: ",i)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")



	divisions = soup.find_all("div", {"class" : "FYwKg _11hx2_1"})
	posted_at_list = soup.find_all("time")
	i = 0
	for division in divisions:
		row = []
		#print("\n-------------------------------------------------")
		title = division.find("a").get_text()
		#print(title)
		row.append(title)

		company_name = division.find("span",{"class": "FYwKg _3CTQy _1GAuD _1PRnx"}).get_text()
		#print(company_name)
		row.append(company_name)


		posted_at = posted_at_list[i].get_text()
		i = i + 1
		#print(posted_at)
		row.append(posted_at)

		link = division.find("a").get("href")
		page = requests.get(link)
		soup2 = BeautifulSoup(page.content, "html.parser")
		div = soup2.find("div",{"class": "FYwKg _20Cd9 _3qNSL_1 bMBHP_1 sDUog_1 _1GAuD"})
		try:
			span_list = div.find_all("span",{"class": "FYwKg _1GAuD C6ZIU_1 _8QVx6_1 _3NFar_1 _29m7__1"} )
		except:
			continue
		salary = None
		if span_list[1] != None:
			salary = span_list[1].get_text()
		#print(salary)
		row.append(salary)

		try:
			text_tag = soup2.find("span",text=re.compile('\d [yY]ears'))
			experience = text_tag.get_text()
		except:
			experience = None
		#print(experience)
		row.append(experience)

		
		#print(link)
		row.append(link)

		dataframe.append(row)




dataframe[0] = columns
dataframe = pd.DataFrame(dataframe)
#print(dataframe)
dataframe.to_csv("jobstreet_singapore1.csv", index=False, header=False)

