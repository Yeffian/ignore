import sys
import requests

search = 'https://raw.githubusercontent.com/github/gitignore/main/'
params = sys.argv[1:]

contents = ''


def generate_ignore(languages):
    for lang in languages:
        global contents
        contents += '\n' + requests.get(search + lang + '.gitignore').text


generate_ignore(params)


with open('.gitignore', 'w') as file:
    file.write(contents)
