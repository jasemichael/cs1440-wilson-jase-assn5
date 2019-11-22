#!/bin/env python3

# if this doesn't work because of a missing package, `pip3 install --user requests`
import requests


def demo(url):
    try:
        # TODO: what if an error happens?
        response = requests.get(url)
        print(f"[{response.status_code} '{response.reason}'] {response.url}")
        i = 5
        for line in response.text.split('\n'):
            if i == 0:
                print('\t...')
                break
            print(f"\t{line}")
            i -= 1
        print()


    except Exception as e:
        print(f"Failed to get {url} because {e}")


demo('http://example.com')
demo('https://cs.usu.edu/about/contact')
demo('http://unnovative.net/does-not-exist.html')
demo('ftp://unnovative.net/does-not-exist.html')
