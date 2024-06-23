import sys
import requests

search = 'https://raw.githubusercontent.com/github/gitignore/main/'
params = sys.argv[1:]

contents = ''

for param in params:
    contents += '\n' + requests.get(search + param + '.gitignore').text


with open('.gitignore', 'w') as file:
    file.write(contents)
