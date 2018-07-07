import csv
import random
from datetime import datetime, timedelta

schema = ['Date', 'Region','Size','Ad Slot', 'Price Point', 'Media Type', 'Device Type', 'Earnings', 'Impressions', 'eCPM']
region = ['APAC', 'EU', 'US']
size = ['300x250', '970x250', '300x600', '320x50']
ad_slot = ['dtb_buy_248', 'dtb_buy_300', 'dtb_buy_180']
device_type = ['PC', 'Other', 'Phone', 'Tablet']

with open('test_data.csv', 'wb') as csv_file:
    file_writer = csv.writer(csv_file, delimiter=',',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow([g for g in schema])

    for x in range(90):
        date_N_days_ago = datetime.now() - timedelta(days=x)
        for y in range(5000):
            file_writer.writerow([date_N_days_ago.date(),
                                  random.choice(region),
                                  random.choice(size),
                                  "dtb_buy_" + str(random.randint(1, 99999)),
                                  (random.randint(155, 389)/100.0),
                                  'D',
                                  random.choice(device_type),
                                  random.randint(155, 256) / 100.0,
                                  random.randint(10, 600),
                                  random.randint(155, 389)/100.0])

