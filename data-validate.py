import requests
from time import sleep

DEBUG = True

# A list of DE ZIP codes from https://www.unitedstateszipcodes.org/de/
# Can be scraped if necessary
ZIP_CODES_DE = [
    19701,
    19702,
    19703,
    19706,
    19707,
    19708,
    19709,
    19710,
    19711,
    19712,
    19713,
    19714,
    19715,
    19716,
    19717,
    19718,
    19720,
    19721,
    19725,
    19726,
    19730,
    19731,
    19732,
    19733,
    19734,
    19735,
    19736,
    19801,
    19802,
    19803,
    19804,
    19805,
    19806,
    19807,
    19808,
    19809,
    19810,
    19850,
    19880,
    19884,
    19885,
    19886,
    19887,
    19889,
    19890,
    19891,
    19892,
    19893,
    19894,
    19895,
    19896,
    19897,
    19898,
    19899,
    19901,
    19902,
    19903,
    19904,
    19905,
    19906,
    19930,
    19931,
    19933,
    19934,
    19936,
    19938,
    19939,
    19940,
    19941,
    19943,
    19944,
    19945,
    19946,
    19947,
    19950,
    19951,
    19952,
    19953,
    19954,
    19955,
    19956,
    19958,
    19960,
    19961,
    19962,
    19963,
    19964,
    19966,
    19967,
    19968,
    19969,
    19970,
    19971,
    19973,
    19975,
    19977,
    19979,
    19980
]


def validate_zip():
    """
    Checks the list of ZIP codes to see if
    myhealthycommunity.dhss.delaware.gov
    offers info about that code.
    """
    valid_codes = []
    invalid_codes = []
    url_start = 'https://myhealthycommunity.dhss.delaware.gov/locations/zip-code-'
    url_end = '/download_covid_19_data'

    # If response.url leads to invalid_redirect_url, then it's
    # probably not a valid ZIP with COVID results for DE
    invalid_redirect_url = 'https://myhealthycommunity.dhss.delaware.gov/locations/state'

    for code in ZIP_CODES_DE:
        code = str(code)
        print("On code: " + code)
        sleep(1)
        final_url = url_start + code + url_end
        request = get_url(final_url)
        print('Request URL for code ' + code + ': ' + request.url)
        if request.url == invalid_redirect_url:
            print('ZIP code ' + code + ' invalid?')
            invalid_codes += [code]
        else:
            print('ZIP code ' + code + ' valid?')
            valid_codes += [code]

    print('Suspected valid codes: ')
    print(valid_codes)
    print('Suspected invalid codes: ')
    print(invalid_codes)


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


def main():
    """
    Starts the program.
    """
    print('Options...')
    print('1: Begin ZIP code validation')
    choice = input('Enter what you want to do: 1 ')

    if choice == '1':
        validate_zip()
    else:
        print('Invalid input...')

    print('End of program')
    print()


if __name__ == '__main__':
    main()
