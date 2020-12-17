# Necessary import

import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

## Part 1. Functions related to historical Coronavirus data of last 30 days
def obtain_historical_data():
    r = requests.get("https://corona.lmao.ninja/v2/historical?lastdays=30")
    if r.status_code != 200:
        print('API status !=200, failed')
    elif r.status_code == 200:
        print('API status = 200, sucessful')
    historical_data = r.json() # convert the results to json format
    print(json.dumps(historical_data, indent=2, sort_keys=True))
    return(historical_data)

# 1.1 Historical data of cases in each country
def organized_historical_cases(historical_data):
    df = pd.DataFrame(historical_data)
    list_timeline = df['timeline'].values.tolist()
    timeline = pd.DataFrame(list_timeline)
    list_cases = timeline['cases'].values.tolist()
    cases = pd.DataFrame(list_cases)
    cases['country'] = df['country']
    cases_organized = cases.groupby('country').sum() # some countries have provinces available, in order to organize data
    return cases_organized

def plot_organized_historical_cases(cases_organized, query_country):
    if query_country in cases_organized.index:
        query_country_df = cases_organized.loc[query_country, :]
        query_country_df.transpose().plot(kind='line', subplots=True)
        return plt.show()
    elif query_country not in cases_organized.index:
        print('Query country is not available')

# 1.2 Historical data of deaths in each country
def organized_historical_deaths(historical_data):
    df = pd.DataFrame(historical_data)
    list_timeline = df['timeline'].values.tolist()
    timeline = pd.DataFrame(list_timeline)
    list_deaths = timeline['deaths'].values.tolist()
    deaths = pd.DataFrame(list_deaths)
    deaths['country'] = df['country']
    deaths_organized = deaths.groupby('country').sum()
    return deaths_organized

def plot_organized_historical_deaths(deaths_organized, query_country):
    if query_country in deaths_organized.index:
        query_country_df = deaths_organized.loc[query_country, :]
        query_country_df.transpose().plot(kind='line', subplots=True)
        return plt.show()
    elif query_country not in deaths_organized.index:
        print('Query country is not available')

# 1.3 Historical data of recovered in each country
def organized_historical_recovered(historical_data):
    df = pd.DataFrame(historical_data)
    list_timeline = df['timeline'].values.tolist()
    timeline = pd.DataFrame(list_timeline)
    list_recovered = timeline['recovered'].values.tolist()
    recovered = pd.DataFrame(list_recovered)
    recovered['country'] = df['country']
    recovered_organized = recovered.groupby('country').sum()
    return recovered_organized

def plot_organized_historical_recovered(recovered_organized, query_country):
    if query_country in recovered_organized.index:
        query_country_df = recovered_organized.loc[query_country, :]
        query_country_df.transpose().plot(kind='line', subplots=True)
        return plt.show()
    elif query_country not in recovered_organized.index:
        print('Query country is not available')



