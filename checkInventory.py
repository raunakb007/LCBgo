from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import smtplib
import ssl
import os

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""  # Enter your address
receiver_email = ""  # Enter receiver address
password = os.environ.get('GPASS') # Sending email password


context = ssl.create_default_context()

""" A few bottles that I have been interested in..."""

# Hibiki
url = 'https://www.lcbo.com/webapp/wcs/stores/servlet/PhysicalStoreInventoryView?langId=-1&storeId=10203&catalogId=10051&productId=61344'

# Glenmorangie 18 year

# url = 'https://www.lcbo.com/webapp/wcs/stores/servlet/PhysicalStoreInventoryView?langId=-1&storeId=10203&catalogId=10051&productId=58987'

# The Dalmore 12

# url = 'https://www.lcbo.com/webapp/wcs/stores/servlet/PhysicalStoreInventoryView?langId=-1&storeId=10203&catalogId=10051&productId=54365'


message = """\
Subject: Hibiki Alert

Change detected on LCBO Website. Check Hibiki Stock.

Link: {}

This message was sent using Python.
""".format(url)

try:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'lxml')

    inventory_check = soup.find('div', class_='col-xs-12 col-md-6 col-md-offset-4').contents[0]

    message = inventory_check.strip('\n\t')
    if message == "Sorry, the item you're searching for is not available at any stores.":
        print('Not Available')
except:
    print('Change Detected')
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
