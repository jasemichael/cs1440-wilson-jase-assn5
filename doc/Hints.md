# CS 1440 Assignment 5 Hints

*   Study the supplied demonstration programs to answer your questions about
    how to use the code libraries.
*   Get an early start on this program so you have enough time to ask questions
    before the final lecture.
*   Leave yourself plenty of time for testing.
*   Identify the base case(s) and handle these at the top of `crawl()`.
    *   *Do not* make a recursive call to `crawl()` when a base case is
        reached.
    *   Do make a recursive call to `crawl()` otherwise.
*   It is very possible for your program to get into an infinite recursive
    loop.  Watch your program carefully to guard against this!
*   Try [Exception Handling](https://wiki.python.org/moin/HandlingExceptions)
    when you run into errors.
*   You can test your program against `http://cs.usu.edu/`,
    `http://unnovative.net/level0.html`, or another website you control.  Some
    sites consider automated crawlers like this to be a nuisance, or worse.  Be
    respectful of others' bandwidth.
*   Python functions accept arguments via pass-by-reference.  When your
    `visited` set is modified within a function call, the caller will see that
    its contents have been updated.  This means that you don't need to return
    anything from `crawl()`.
*   If you encounter web pages which cause your crawler to hang, you can avoid
    them by hard-coding their URLs to the `visited` set before your program
    begins.
*   Don't expect that your program's output will exactly match my sample
    output.  What websites you are able to find will depend upon many factors
    outside of our control.  Our program is running loose on the internet,
    which means that it is crawling over a vast network that is constantly
    undergoing change, and which can present different pathways depending upon
    when and how you connect to it.
*   Don't be surprised if your program's output is different today than it was
    yesterday, even though you didn't change anything.
*   Most websites treat URLs with a trailing slash `/` the same as without (for
    example, `http://example.com` vs. `http://example.com/` are the same page).
    Other websites may serve different content from both addresses.  It's
    really not worth the hassle to try to figure this one out.  Google's own
    crawler regards slashed and un-slashed URLs as [different
    pages.](https://webmasters.googleblog.com/2010/04/to-slash-or-not-to-slash.html).
    If it's good enough for Google, it's good enough for your crawler.


## Testing server

You will find a program called [testing_server.py](../demos/testing_server.py)
in the starter code repository.  This is a little HTTP server that can run on
your own computer.  It makes up new webpages as you browse and counts every
visited page, displaying a report when it shuts down.  Because infinite loops
can easily occur in recursive programs it shuts itself down after a few
seconds.

This program lets you work on the assignment when the internet is unavailable
as well as helps you troubleshoot tricky crawler problems.


### Quickstart

In one Bash console run:

```
$ python demos/testing_server.py
Serving from http://localhost:8000/ for 3 seconds after first contact
Press Ctrl-C or visit http://localhost:8000/shutdown/ to quit
```

In another console run your crawler directed at the URL indicated:

```
$ python src/crawler.py http://localhost:8000/
```


### Command line arguments

`testing_server.py` can take up to three arguments on the command line:

```
$ python testing_server.py [address=localhost] [port=8000] [timeout=3]
```

The first two arguments set the address and port the server listens on.  The
third argument lets you control how long the server remains running after being
visited for the first time.  Set this argument to `0` to tell the server to run
forever.  The server may be shut down with `Ctrl-C` or by visiting any URL
ending in `shutdown`.


#### Specify a different address and port on the command line:

If port `8000` is unavailable on your computer you will get an `OSError`:

```
OSError: [Errno 98] Address already in use
```

This happens when another program on your computer is using that port.  Try
other port numbers until you find one that is available.  Valid port numbers
run from `1024` to `65535`.

```
$ python demos/testing_server.py localhost 4321
Serving from http://localhost:4321/ for 3 seconds after first contact
Press Ctrl-C or visit http://localhost:4321/shutdown/ to quit
```


#### Make the server run forever

This testing server shuts itself down after a few seconds.  Specify a timeout
of `0` and you can explore it yourself in your browser.  This will help you
understand what your crawler sees and how it should behave.

```
$ python demos/testing_server.py localhost 8000 0
Serving from http://localhost:8000/ forever
Press Ctrl-C or visit http://localhost:8000/shutdown/ to quit
```


### Understanding the report

After the server shuts down it prints a report of pages visited with the number
of times each was visited.  Your crawler should visit each page once and *only*
once.  Your crawler *cannot* visit every link it sees.  It must respect its
base case and quit at some point.

This is what a visit by a good crawler to `http://localhost:8000/` will look
like (notice the trailing `/` in the URL):

```
41 pages were visited exactly once

81 pages were not visited at all
```

Because URLs that don't end in `/` can mean the same thing as URLs that do,
this is also good output from a crawler to `http://localhost:8000`:

```
4 pages were visited exactly once

9 pages were not visited at all

1 page was visited many times
	/: 2
```

The page `/` is visited twice is because your crawler thinks
`http://localhost:8000` and `http://localhost:8000/` are different pages while
the server thinks they are the same.  Don't worry about this, life is too short
and precious to waste on this inconsistency.

If your crawler just doesn't know when to quit you'll see output like this:

```
81 pages were not visited at all

41 pages were visited many times
	/: 68
	/deadend: 67
	/a: 20
	/b: 20
	/c: 20
	/aa: 8
	/ab: 8
    ...
```

If your crawler is just wildly guessing URLs it will visit pages before they
exist.  If you see `N pages were visited before they were created` you need to
seriously re-think your approach.
