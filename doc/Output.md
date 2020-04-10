# CS 1440 Assignment 5 Sample output


### When no parameters are supplied

```
$ python src/crawler.py
Error: no URL supplied
```

### When the program detects that a relative URL is given instead of an absolute URL

```
$ python src/crawler.py cs.usu.edu
Error: Invalid URL supplied.
Please supply an absolute URL to this program
```

### A correct invocation of the program
*Note: I specified following 0 links, so only the initial website's URL is displayed*

```
$ python src/crawler.py https://cs.usu.edu 0
Crawling from https://cs.usu.edu to a maximum distance of 0 links
https://cs.usu.edu
```

## For the following examples your output may vary from mine

What websites you are able to find will depend upon many factors outside of our
control.  Our program is running loose on the internet, which means that it is
crawling over a vast network that is constantly undergoing change, and which
can present different pathways depending upon when and how you connect to it.

* Don't expect that your program's output will exactly match mine!
* Don't be surprised if your program's output is different today than it was
  yesterday, even though you didn't change anything.


### Crawling to pages only 1 link away

```
$ python src/crawler.py https://cs.usu.edu 1
Crawling from https://cs.usu.edu to a maximum distance of 1 link
https://cs.usu.edu
	http://www.usu.edu
	http://usu.edu/azindex/
	http://usu.edu/myusu/
	https://cs.usu.edu/about/index.php
	https://cs.usu.edu/news/main-feed/2018/awards-banquet.php 
	https://engineering.usu.edu/news/main-feed/2019/a-pin.php
	https://engineering.usu.edu/news/main-feed/2019/student-awards.php
	https://cs.usu.edu/students/resources/microsoft-imagine.php
	https://cs.usu.edu/files/pdf/department-map.pdf
	https://appcamp.usu.edu
	https://cs.usu.edu/students/resources/why-comp-sci.php
	https://cs.usu.edu/employment/
	https://www.youtube.com/watch?v=CRYfNVlg4lE&feature=youtu.be
	http://a.cms.omniupdate.com/10?skin=usu&account=usu&site=Engineering_CS&action=de&path=/index.pcf
```

### Another correct invocation, this time letting the program use its default distance of 3 links

Notice the levels of indentation in the output that clearly indicate the depth
of recursion.  Your program must follow this format:

*   The initial URL supplied on the command line is at level 0
*   For each level of depth add 4 spaces
*   Use spaces, not tabs

Which URLs your program prints don't need to match this example.  Your program
may print a different set of URLs in a different order than my program did.
What links your program finds depends on circumstances outside of our control.

Today my program visited 418 URLs and took almost 4 minutes from my office in
Old Main.  Last semester this same command visited 939 URLs and only took 2.3
seconds when run from my home network.  Your results will vary with your
network conditions.

Your program may take an *extremely* long time to finish.  This is fine; you
are not being graded on how fast your solution is.

The presence of error messages/exceptions is allowed provided that your program
does *not* crash as a result of them.


```
$ python src/crawler.py http://cs.usu.edu (Links to an external site.)
Crawling from http://cs.usu.edu to a maximum distance of 3 links
https://cs.usu.edu
    http://www.usu.edu
        http://www.usu.edu/azindex/
            https://my.usu.edu
            http://directory.usu.edu
            http://www.usu.edu/about/
            http://usueastern.edu/about/
            http://www.usu.edu/aa/
            http://www.usu.edu/calendar/academic.cfm
            http://catalog.usu.edu/content.php?catoid=4&navoid=546
Requests or BeautifulSoup ctor() HTTPSConnectionPool(host='catalog.usu.edu', port=443): Max retries exceeded with url: /content.php?catoid=4&navoid=546 (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify       failed')])")))
            http://www.usu.edu/arc/tutoring/
            http://www.usu.edu/arc/
            http://banner.usu.edu
            https://id.usu.edu/Personal/Lookup
Requests or BeautifulSoup ctor() HTTPSConnectionPool(host='myid.usu.edu', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')])")))
    ...
```


### Crawling to 10 links

Be careful when you test depths beyond 2 or 3; depending on what site you aim
your crawler at, this could take a *very* long time!

```
$ python src/crawler.py http://unnovative.net/level0.html 10
Crawling from http://unnovative.net/level0.html to a maximum distance of 10 links
http://unnovative.net/level0.html
	http://unnovative.net/level1.html
		http://unnovative.net/level2.html
			http://unnovative.net/level3.html
				http://unnovative.net/level4.html
					http://unnovative.net/level5.html
						http://unnovative.net/level6.html
							http://unnovative.net/level7.html
								http://unnovative.net/level8.html
									http://unnovative.net/level9.html
										http://unnovative.net/level10.html
```


### Exhausting all possibilities

The document `level15.html` refers back to `level0.html`, and the crawler has
run out of new links to follow.  Because the crawler has already been to
`level0.html` and has no other links to follow it stops.

```
$ python src/crawler.py http://unnovative.net/level0.html 30
Crawling from http://unnovative.net/level0.html to a maximum distance of 30 links
http://unnovative.net/level0.html
	http://unnovative.net/level1.html
		http://unnovative.net/level2.html
			http://unnovative.net/level3.html
				http://unnovative.net/level4.html
					http://unnovative.net/level5.html
						http://unnovative.net/level6.html
							http://unnovative.net/level7.html
								http://unnovative.net/level8.html
									http://unnovative.net/level9.html
										http://unnovative.net/level10.html
											http://unnovative.net/level11.html
												http://unnovative.net/level12.html
													http://unnovative.net/level13.html
														http://unnovative.net/level14.html
															http://unnovative.net/level15.html
```
