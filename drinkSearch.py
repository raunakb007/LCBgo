from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


def drink_search(searchterm):
    """
    Returns the results from a search on the LCBO website
    :param searchterm: (string) Search term/key words
    :return: A results object containing a list of the search results.
    """

    searchterm = re.sub(' ', '%20', searchterm)

    url = 'https://www.lcbo.com/webapp/wcs/stores/servlet/SearchDisplay?storeId=10203&searchTerm={}'.format(searchterm)
    try:
        res = {'result': []}
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        webpage = urlopen(req).read()

        soup = BeautifulSoup(webpage, 'lxml')
        product_ref = soup.find('div', class_='product_listing_container')
        product_names = product_ref.findAll('div', class_='product_name')
        product_prices = product_ref.findAll('div', class_='product_price')

        for product in product_names:
            try:
                product_name = product.find('a').contents[0]
                product_link = product.find('a').attrs.get('href', None)
            except:
                print('drink data not available')
                continue
            data = {'name': product_name, 'link': product_link}
            res['result'].append(data)

        for i in range(len(product_prices)):
            try:
                price = product_prices[i].find('span').contents[0]
            except Exception as e:
                print('price data not available')
                print(e)
                continue

            res['result'][i]['price'] = price.strip('\t\n')

    except Exception as e:
        print('failed to get page')
        print(e)
        res = None

    return res
