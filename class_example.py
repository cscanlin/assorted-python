from datetime import datetime, timedelta
import csv
import json
import requests

MY_TOKEN = 'put api token here'

class MyApiWrapper(object):

    def __init__(self, fields, url='https://api.example.com/', date=datetime.now()):
        self.fields = fields
        self.url = url
        self.date = date

    def formatted_date(self):
        return self.date.strftime('%Y-%m-%d')

    @property
    def request_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def generate_body(self):
        return json.dumps({
            "token": MY_TOKEN,
            "date": self.formatted_date(),
            "fields": self.fields,
        })

    def report_stats(self):
        req = requests.get(self.url, headers=self.request_headers, data=self.generate_body())
        return json.loads(req.content)

    def download_report(self):
        with open('my_api_output_' + self.formatted_date(), 'wb') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=self.fields)
            dict_writer.writerows(self.report_stats())

if __name__ == '__main__':
    fields = [
        'spend',
        'clicks',
        'impressions',
    ]
    yesterday = datetime.now() - timedelta(days=1)
    MyApiWrapper(fields, date=yesterday).download_report()
