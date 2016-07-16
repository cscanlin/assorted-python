import collections
from python_vlookup import python_vlookup


array = python_vlookup.get_csv_data('shareasale_lookup.csv')
print array



#Return a dictionary
def get_credentials():
    host = 'hostname'
    un = 'username'
    pw = 'password'
    credentials = {'hostname':host,'username':un,'password':pw}
    return credentials

credentials = get_credentials()
print credentials['password']

#Return a named tuple
def get_credentials():
    host = 'hostname'
    un = 'username'
    pw = 'password'
    credentials = collections.namedtuple('credentials', ['host', 'un', 'pw'])
    return credentials(host,un,pw)

credentials = get_credentials()
print credentials.host

#Return a regular tuple
def get_credentials():
    host = 'hostname'
    un = 'username'
    pw = 'password'
    return host,un,pw

host,un,pw = get_credentials()
print un

#Return a single value
def get_credentials(field):
    if field == 'host': return 'hostname'
    if field == 'un': return 'username'
    if field == 'pw': return 'password'

host = get_credentials('host')
print host
