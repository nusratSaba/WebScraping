# Requesting Data
import requests

# Extracting data from html 
from bs4 import BeautifulSoup

import pandas as pd

# Store the result in 'res' variable
page = requests.get('https://realpython.github.io/fake-jobs/')
soup = BeautifulSoup(page.content, 'html.parser')
# Extract title of page
title = soup.title.text

# print(title)

job_titles = []
job_title_soup = soup.find_all(class_ = "title is-5")
for job in job_title_soup:
  job_titles.append(job.text)
  # print(job.text.strip())

companies = []
company_soup = soup.find_all(class_ = "company")
for company in company_soup:
  companies.append(company.text)

date_time = []
date_time_soup = soup.findAll('time')
for td in date_time_soup:
  date_time.append(td.text)


# Exporting all data in CSV file
all_data = pd.DataFrame()
all_data['Job Titles'] = job_titles
all_data['Company Names'] = companies
all_data['Date and Time'] = date_time

# print(all_data)

# saving the dataframe
all_data.to_csv('fakePythonInfo.csv')