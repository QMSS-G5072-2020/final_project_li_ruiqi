from organized_coronavirus_info import __version__
from organized_coronavirus_info import organized_coronavirus_info
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

def test_version():
    assert __version__ == '0.1.0'

historical_data = organized_coronavirus_info.obtain_historical_data()

# Adding unit test corresponding to functions in package
# For functions in part 1
def test_obtain_historical_data():
    historical_data = organized_coronavirus_info.obtain_historical_data()
    assert type(historical_data) == list

def test_organized_historical_cases():
    cases_organized = organized_coronavirus_info.organized_historical_cases(historical_data)
    assert type(cases_organized) == pd.core.frame.DataFrame

def test_organized_historical_deaths():
    deaths_organized = organized_coronavirus_info.organized_historical_deaths(historical_data)
    assert type(deaths_organized) == pd.core.frame.DataFrame

def test_organized_historical_recovered():
    recovered_organized = organized_coronavirus_info.organized_historical_recovered(historical_data)
    assert type(recovered_organized) == pd.core.frame.DataFrame

# For functions in part 2
def test_obtain_global_data():
    global_data = organized_coronavirus_info.obtain_global_data()
    assert type(global_data) == pd.core.frame.DataFrame

def test_obtain_continent_data():
    continent_data = organized_coronavirus_info.obtain_continent_data()
    assert type(continent_data) == pd.core.frame.DataFrame