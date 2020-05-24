
import web_scrapping_package as p
import pandas as pd

main_url = "https://finance.yahoo.com"
page_url = "https://finance.yahoo.com/screener/unsaved/e2e2de3b-ea56-46b8-b070-9c877a3bacde?count=100&offset=0"
page_number = 1
current_page = page_url


columns = ['Symbol','Yahoo finance url','Name','Current Price','Volume','Avg Volume','Market Cap','PE Ratio','52 Week High','52 Week Low', 'Profit Margin','Operating Margin','Return on Equity','Earnings Per Share']
dataframe = [[]]
dataframe[0] = columns

def get_data_from_page(url):
	page_soup = p.get_soup_from_url(url)
	rows = p.get_table_rows(page_soup)
	p.get_values_in_a_row(rows, dataframe)


while page_number < 11	:
	print("Collecting data from page: ", page_number," :", current_page)
	get_data_from_page(current_page)
	page_number = page_number + 1
	current_page = p.get_next_page_url(current_page)

dataframe = pd.DataFrame(dataframe)
dataframe.to_csv("Yahoo_finance_data.csv", index=False, header=False)





