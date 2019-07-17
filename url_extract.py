
option#1:
uri = 'http://stackoverflow.com/questions/1234567/blah-blah-blah-blah'
domain=uri.split("//")[-1].split("/")[0]

option#2:
from urllib.parse import urlparse
uri = 'http://stackoverflow.com/questions/1234567/blah-blah-blah-blah'
domain=urlparse(uri)
print(domain)
print('{uri.scheme},{uri.netloc}'.format(uri=domain))

