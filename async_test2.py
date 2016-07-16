import requests
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'https://httpbin.org/delay/3',  # long request
    'https://httpbin.org/delay/1',  # short request
]

pool = ThreadPool(4)
results = pool.map(requests.get, urls)
print(results)
pool.close()
pool.join()
