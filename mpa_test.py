import itertools
import posixpath
import csv
import collections
from facebookads import FacebookSession
from facebookads import FacebookAdsApi
from facebookads import specs
from facebookads.specs import (
    ObjectStorySpec,
    LinkData,
    AttachmentData
)
from facebookads.objects import (
    AdUser,
    AdCampaign,
    AdSet,
    AdImage,
    AdCreative,
    AdGroup,
    TargetingSpecsField,
)

from facebookads import objects
import configparser
import os
import time
import pprint
import fb_helper


config = fb_helper.open_config('fb_config.cfg')

app_id = '826090954086728'
app_secret = 'bcaf6d6eb26bbc824fa33a6527863ea7'
access_token = 'CAALvU0ne2UgBAOZCLefaNxbx7qjnOLfRttKOVZCDRMsscZABTjumWDW4ogyDvA7KWYUfk8dH0NMbTxXRz0iSI8S8Y7MLy5JdtM2ZCtWb6ZCxq6EONpX5neTU6nwDZCCZA1hzmH6vbIgqfCLgD6p4JYTC5uZANiTxQ64ENZA5eLpAOXo3hJSF71QATbfgS9lVmt6ZAHZCa92nP7oV6pIJ9Dygd0B'
FacebookAdsApi.init(app_id, app_secret, access_token)

pp = pprint.PrettyPrinter(indent=4)

act_id = config.get('Defaults', 'ad_account')

csvfilename = posixpath.join('c:', 'Users', 'Christopher Scanlin', 'assorted_python', 'csvfilename.csv')

input_file = open(csvfilename, 'rb')

input_fields = (
'CLUSTER',
'PARENT_URL',
'CAPTION',
'NAME_ONE',
'DESCRIPTION_ONE',
'IMG_ONE',
'URL_ONE',
'NAME_TWO',
'DESCRIPTION_TWO',
'IMG_TWO',
'URL_TWO',
'NAME_THREE',
'DESCRIPTION_THREE',
'IMG_THREE',
'URL_THREE',
'AD_NAME',
'MESSAGE',
'PIXEL_ID',
'BID',
'BUDGET',
'ADSET_ID',
)

#img = AdImage(parent_id=my_account.get_id_assured())
#img[AdImage.Field.filename] = posixpath.join('c:', 'Users', 'Christopher Scanlin', 'Anaconda', 'fb', 'TCRK_collage_v1_8.jpg')
#img.remote_create()
#print("**** DONE: Image uploaded:")
#pp.pprint(img)  # The image hash can be found using img[AdImage.Field.hash]

def get_csv_data(csvfilename):
    with open(csvfilename, 'r') as csvfile:
        csv_rows = list(csv.reader(csvfile, delimiter=','))
    return csv_rows


with open('csvfilename.csv','rb') as f:
    r = csv.reader(f)
    od = collections.OrderedDict((row[0], row[1:]) for row in r)
print od

with open('csvfilename.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row)
