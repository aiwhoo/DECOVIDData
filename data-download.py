import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

from requests.api import get

DEBUG = True


def get_all_de():
    """
    Saves the CSV with all DE data from
    https://myhealthycommunity.dhss.delaware.gov/locations/state/download_covid_19_data
    """
    current_time = get_datetime()
    file_title = current_time + '_ALL.csv'
    final_path = os.path.join(get_path(), 'data', 'DE-all', file_title)
    url = 'https://myhealthycommunity.dhss.delaware.gov/locations/state/download_covid_19_data'
    url_data = get_url(url).content
    if DEBUG:
        print('All data final path: ' + final_path)
    save_data(final_path, url_data, 'wb+')


def get_path():
    """
    Given a path, returns the proper OS independent relative path
    """
    current_folder = os.path.dirname(os.path.abspath(__file__))
    if DEBUG:
        print('Current folder: ' + current_folder)
    return current_folder


def get_url(url):
    """
    Given a URL, attempts to return the data from it
    """
    value = ''
    try:
        print('Getting the URL ' + url)
        value = requests.get(url)
    except Exception as e:
        print('Error in get_url')
        print(e)
    return value


def get_datetime():
    """
    Returns the current time as a string
    Used to create file titles
    """
    time = str(datetime.today().strftime('%Y%m%d-%H%M%S'))
    if DEBUG:
        print('Current time: ' + time)
    return time


def save_data(save_path, file_data, write_mode):
    """
    Saves data to a given path
    Given write mode should be 'wb' for binary files
    and 'w' for text data
    """
    try:
        with open(save_path, write_mode) as p:
            if DEBUG:
                print('Trying to write to: ' + save_path)
                print('Write mode: ' + write_mode)
            p.write(file_data)
    except Exception as e:
        print('Error in save_data')
        print(e)


def main():
    """
    Starts the program
    """
    get_datetime()
    print('Options...')
    print('1: Save data for all of DE')
    print('2: Save ZIP code level data')
    choice = input('Enter what you want to do: 1, 2 ')

    if choice == '1':
        get_all_de()
    else:
        print('Invalid input...')

    print('Ending program...')
    print()


if __name__ == '__main__':
    main()
