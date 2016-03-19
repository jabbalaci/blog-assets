#!/usr/bin/env python

"""
Random Python projects from GitHub.
The first one is a popular one from the Top 100.
The second one is from the rest. 
Gist:   https://gist.github.com/2716997
Reddit: http://www.reddit.com/r/learnpython/comments/trb4j/if_you_are_looking_for_python_projects_to/
"""

import json
import random
import textwrap
try:                 # Python 3
    from urllib.request import urlopen
except ImportError:  # Python 2
    from urllib2 import urlopen

MAX = 10
PAGE = random.randint(1, MAX)
URL_POP = 'https://api.github.com/legacy/repos/search/python?language=Python'
URL_ALL = URL_POP + '&start_page={page}'.format(page=PAGE)
WIDTH = 78

def remove_non_ascii(text): 
    return ''.join(c for c in text if ord(c) < 128)

def process(r):
    fmt = '{owner}/{name}   (watchers: {watchers}, forks: {forks}, updated: {pushed:.10})'
    print(fmt.format(**r))
    print('\n'.join(textwrap.wrap(remove_non_ascii(r['description']), WIDTH)))
    print(r['url'])
    homepage = r.get('homepage', None)
    if homepage:
        print(homepage)

def choose_from(url):
    repos = json.loads(urlopen(url).read().decode('utf-8'))['repositories']
    process(random.choice(repos))

def main():
    choose_from(URL_POP)
    print('=' * 10)
    choose_from(URL_ALL)
    print('=' * 20)
    
#############################################################################

if __name__ == "__main__":
    main()
