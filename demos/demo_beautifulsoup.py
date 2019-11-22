#!/bin/env python3

# if this doesn't work because of a missing package, `pip3 install --user beautifulsoup4`
from bs4 import BeautifulSoup


exampleDotCom = """<!doctype html>
    <html>
    <head>
        <title>Example Domain</title>

        <meta charset="utf-8" />
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
        body {
            background-color: #f0f0f2;
            margin: 0;
            padding: 0;
            font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
            
        }
        div {
            width: 600px;
            margin: 5em auto;
            padding: 50px;
            background-color: #fff;
            border-radius: 1em;
        }
        a:link, a:visited {
            color: #38488f;
            text-decoration: none;
        }
        @media (max-width: 700px) {
            body {
                background-color: #fff;
            }
            div {
                width: auto;
                margin: 0 auto;
                border-radius: 0;
                padding: 1em;
            }
        }
        </style>    
    </head>

    <body>
    <div>
        <h1>Example Domain</h1>
        <p>This domain is established to be used for illustrative examples in documents. You may use this
        domain in examples without prior coordination or asking for permission.</p>
        <p><a href="http://www.iana.org/domains/example">More information...</a></p>
    </div>
    </body>
    </html>
"""


# https://itty.bitty.site/#/data:text/html;charset=utf-8;bxze64,XQAAAAK0AAAAAAAAAAAeGgJD4X3uAKqNrCZTZ3f9OvXziRrZppgolF8SJZWN5h4V3kaQSjYZWlE8uP8JdY+pV+9Mv1JN98q0nA8b+A9ASkQQ6AaFTdhkC3//2OTgAA==
ittyBittyDotSite = """
<html>
    <head>
        <title>The Cheat</title>
    </head>
    <body>
        <h2>Hey! Listen!</h2>
        <ol>
            <li>Up</li>
            <li>Up</li>
            <li>Down</li>
            <li>Down</li>
            <li>Left</li>
            <li>Right</li>
            <li>Left</li>
            <li>Right</li>
            <li>B</li>
            <li>A</li>
            <li>Start</li>
        </ol>
    </body>
</html>
"""


def findElements(html, element):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all(element)
        if elements:
            print(f"{element}'s found in this document include:")
            for e in elements:
                print(f"\t{e}")
        else:
            print(f"No {element} elements were found in this document")
    except Exception as e:
        print(f"An exception occurred: {e}")
    print()



def findLinks(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        if links:
            print("URLs linked in this document are:")
            for a in links:
                print(f"\t{a.get('href')}")
        else:
            print("No hyperlinks were found in this document")
    except Exception as e:
        print(f"An exception occurred: {e}")
    print()

findElements(exampleDotCom, 'p')
findElements(exampleDotCom, 'h1')

findElements(ittyBittyDotSite, 'p')
findElements(ittyBittyDotSite, 'li')

findLinks(exampleDotCom)
findLinks(ittyBittyDotSite)
