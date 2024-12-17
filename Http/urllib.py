import urllib.request

response = urllib.request.urlopen('http://httpbin.org/user-agent')
print(response.read().decode())