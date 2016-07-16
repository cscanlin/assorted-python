import csv
import urllib
import lxml.etree as etree
from unidecode import unidecode

rss_url = 'http://www.dotandbo.com/products.rss'
rss_ns = 'http://base.google.com/ns/1.0'
csv_file_path = 'broken_images_2015-02-19.csv'

def get_text(element, node):
    try:
        node_text = element.find(node).text
    except:
        node_text = ''
    else:
        if node_text: return unidecode(node_text)


if __name__ == '__main__':


#    image_link = urllib.urlopen('http://d10125bvdzznt0.cloudfront.net/products/80289/original/IWy6Pyk5em_Lone_Star_Marquee0.jpg').read()
#    html = urllib.urlopen(image_link).read()
#    print html

    rss = etree.parse(urllib.urlopen(rss_url))

    for element in rss.findall('channel/item'):
        sku = get_text(element, '{%s}id' % rss_ns)
        product_name = get_text(element, 'title')
        link = get_text(element, 'link')
        image_link = get_text(element, '{%s}image_link' % rss_ns)
        print product_name

        if image_link:
            html = urllib.urlopen(image_link).read()

        if 'Access Denied' in html:
            broken_row = [link, sku]
            print broken_row

            with open(csv_file_path,'a') as output:
                writer = csv.writer(output)
                writer.writerow(broken_row)
