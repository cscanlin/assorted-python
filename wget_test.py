import wget
url = 'http://www.dotandbo.com/products.rss'
filename = wget.download(url)
print filename
