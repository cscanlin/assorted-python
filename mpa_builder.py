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

csvfilename = posixpath.join('c:', 'Users', 'Christopher Scanlin', 'python_scripts', 'assorted_python', 'csvfilename.csv')

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

with open(csvfilename) as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        cluster = row['CLUSTER']
        parent_url = row['PARENT_URL']
        caption = row['CAPTION']
        name1 = row['NAME_ONE']
        description1 = row['DESCRIPTION_ONE']
        img1 = row['IMG_ONE']
        url1 = row['URL_ONE']
        name2 = row['NAME_TWO']
        description2 = row['DESCRIPTION_TWO']
        img2 = row['IMG_TWO']
        url2 = row['URL_TWO']
        name3 = row['NAME_THREE']
        description3 = row['DESCRIPTION_THREE']
        img3 = row['IMG_THREE']
        url3 = row['URL_THREE']
        ad_name = row['AD_NAME']
        message = row['MESSAGE']
        pixel_id = row['PIXEL_ID']
        bid = row['BID']
        budget = row['BUDGET']
        adset_id = row['ADSET_ID']


        print 'cluster'
        print cluster
        print 'parent_url'
        print parent_url
        print 'caption'
        print caption
        print 'name1'
        print name1
        print 'description1'
        print description1
        print 'img1'
        print img1
        print 'url1'
        print url1
        print 'name2'
        print name2
        print 'description2'
        print description2
        print 'img2'
        print img2
        print 'url2'
        print url2
        print 'name3'
        print name3
        print 'description3'
        print description3
        print 'img3'
        print img3
        print 'url3'
        print url3
        print 'ad_name'
        print ad_name
        print 'message'
        print message
        print 'pixel_id'
        print pixel_id
        print 'bid'
        print bid
        print 'budget'
        print budget
        print 'adset_id'
        print adset_id


        creative = AdCreative(parent_id='act_{}'.format(act_id))
        creative[objects.AdCreative.Field.name] = cluster

        story = specs.ObjectStorySpec()
        story[story.Field.page_id] = 480594848645810

        link = specs.LinkData()
        link[link.Field.link] = parent_url
        link[link.Field.caption] = caption
        link[link.Field.message] = message

        product1 = specs.AttachmentData()
        product1.update({
            specs.AttachmentData.Field.name: name1,
            specs.AttachmentData.Field.description: description1,
            specs.AttachmentData.Field.image_hash: img1,
            specs.AttachmentData.Field.link: url1,
        })

        product2 = specs.AttachmentData()
        product2.update({
            specs.AttachmentData.Field.name: name2,
            specs.AttachmentData.Field.description: description2,
            specs.AttachmentData.Field.image_hash: img2,
            specs.AttachmentData.Field.link: url2,
        })

        product3 = specs.AttachmentData()
        product3.update({
            specs.AttachmentData.Field.name: name3,
            specs.AttachmentData.Field.description: description3,
            specs.AttachmentData.Field.image_hash: img3,
            specs.AttachmentData.Field.link: url3,
        })

        link[link.Field.child_attachments] = [product1, product2, product3]
        story[story.Field.link_data] = link
        creative[creative.Field.object_story_spec] = story

        creative.remote_create()
        print("**** DONE: Creative created:")
        pp.pprint(creative.get_id_assured())

        ### Get excited, we are finally creating an ad!!!
        ad = AdGroup(parent_id='act_{}'.format(act_id))
        ad.update({
            AdGroup.Field.name: ad_name,
            # AdGroup.Field.objective : 'WEBSITE_CONVERSIONS',
            # AdGroup.Field.conversion_specs:{
            #     'action.type':'offsite_conversion',
            #     'offsite_pixel':pixel_id
            # },
            AdGroup.Field.campaign_id: adset_id,
            AdGroup.Field.status: 'PAUSED',
            AdGroup.Field.creative: {
                AdGroup.Field.Creative.creative_id: creative.get_id_assured(),
            },
        })
        ad.remote_create()
        print("**** DONE: Ad created:")
        pp.pprint(ad)
