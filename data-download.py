from time import sleep
import requests
from datetime import datetime
import os

DEBUG = True

# A list of DE ZIP codes from data-validate.py
ZIP_CODES_DE = ['19701', '19702', '19703', '19706', '19707', '19709', '19710', '19711', '19713', '19716', '19717', '19720', '19730', '19731', '19732', '19733', '19734', '19735', '19736', '19801', '19802', '19803', '19804', '19805', '19806', '19807', '19808', '19809', '19810', '19901', '19902', '19904', '19930',
                '19931', '19933', '19934', '19936', '19938', '19939', '19940', '19941', '19943', '19944', '19945', '19946', '19947', '19950', '19951', '19952', '19953', '19954', '19955', '19956', '19958', '19960', '19962', '19963', '19964', '19966', '19967', '19968', '19970', '19971', '19973', '19975', '19977', '19979']


def get_per_zip_data():
    """
    Saves the data for every DE zip code from URLs in the form
    https://myhealthycommunity.dhss.delaware.gov/locations/zip-code-19734/download_covid_19_data.
    """
    url_start = 'https://myhealthycommunity.dhss.delaware.gov/locations/zip-code-'
    url_end = '/download_covid_19_data'

    if DEBUG:
        print('Running get_per_zip_data')
    for code in ZIP_CODES_DE:
        sleep(1)
        code = str(code)
        if DEBUG:
            print('On ZIP code: ' + code)
        url = url_start + code + url_end
        current_time = get_datetime()
        file_title = current_time + '.csv'
        partial_path = os.path.join(get_path(), 'data', 'DE-by-ZIP', code)
        final_path = os.path.join(partial_path, file_title)
        url_data = get_url(url).content
        if DEBUG:
            print('ZIP data final path: ' + final_path)

        # Check if the directory we wants exist,
        # if it doesn't then make it
        if not os.path.exists(partial_path):
            if DEBUG:
                print('Dir does not exist, making dir: ' + partial_path)
            os.makedirs(partial_path)
        else:
            if DEBUG:
                print('Dir exists: ' + partial_path)

        save_data(final_path, url_data, 'wb+')


def get_all_de_data():
    """
    Saves the CSV with all DE data from
    https://myhealthycommunity.dhss.delaware.gov/locations/state/download_covid_19_data.
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
    Given a path, returns the proper OS independent relative path.
    """
    current_folder = os.path.dirname(os.path.abspath(__file__))
    if DEBUG:
        print('Current folder: ' + current_folder)
    return current_folder


def get_url(url):
    """
    Given a URL, attempts to return the data from it.
    """
    value = ''
    try:
        print('Getting the URL ' + url)
        value = requests.get(url)
    except Exception as e:
        print('Error in get_url for ' + url)
        print(e)
    return value


def get_datetime():
    """
    Returns the current time as a string.
    Used to create file titles.
    """
    time = str(datetime.today().strftime('%Y%m%d-%H%M%S'))
    if DEBUG:
        print('Current time: ' + time)
    return time


def save_data(save_path, file_data, write_mode):
    """
    Saves data to a given path.
    Write mode should be 'wb+' for binary files
    and 'w+' for text data.
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
    Starts the program.
    """
    print('Options...')
    print('1: Save data for all of DE')
    print('2: Save ZIP code level data')
    choice = input('Enter what you want to do: 1, 2 ')

    if choice == '1':
        get_all_de_data()
    elif choice == '2':
        get_per_zip_data()
    else:
        print('Invalid input...')

    print('End of program')
    print()


if __name__ == '__main__':
    main()
