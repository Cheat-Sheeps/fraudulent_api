
# importing the pandas library 
import pandas as pd 
  
# reading the csv file 
df = pd.read_csv("domain_model/dataset_phishing.csv") 
  
# take all the data in the url column
data = df['url']

# extract the domain name from the url
domain = data.str.extract(r'(?:http[s]*://)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)')
domain = domain[0].str.replace('www.','')

# write the domain name in a third column
df['domain'] = domain

# write the new dataframe in a csv file
df.to_csv('domain_model/dataset_phishing1.csv', index=False)