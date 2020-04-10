# CS 1440 Assignment 5 Hints

*   Study the supplied demonstration programs to answer your questions about
    how to use the code libraries.
*   Get an early start on this program so you have enough time to answer questions before the final lecture.
*   Leave yourself plenty of time for testing
*   Identify the base case(s) and handle these at the top of `crawl()`.
    *   *Do not* make a recursive call to `crawl()` when a base case is reached
    *   Do make a recursive call to `crawl()` otherwise
*   It is very possible for your program to get into an infinite recursive
    loop.  Watch your program carefully to guard against this!
*   Try [Exception Handling](https://wiki.python.org/moin/HandlingExceptions)
    when you run into errors.
*   Test your program against http://cs.usu.edu/ or another website you
    control.  Some sites consider automated crawlers like this to be a
    nuisance, or worse.  Be respectful of others' bandwidth.
*   Python functions accept arguments via pass-by-reference.  When your `visited`
    set is modified within a function call, the caller will see that its
    contents have been updated.  This means that you don't need to return
    anything from `crawl()`.
*   If you encounter any web pages which cause your crawler to hang, you may
    avoid them by hard-coding their URLs to the `visited` set at the top of your
    program.
*   Don't expect that your program's output will exactly match my sample
    output.  What websites you are able to find will depend upon many factors
    outside of our control.  Our program is running loose on the internet,
    which means that it is crawling over a vast network that is constantly
    undergoing change, and which can present different pathways depending upon
    when and how you connect to it.
*   Don't be surprised if your program's output is different today than it was
    yesterday, even though you didn't change anything.
