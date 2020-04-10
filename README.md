# CS 1440 Assignment 5: Recursive Web Crawler

* [Instructions](doc/Instructions.md)
* [Rubric](doc/Rubric.md)
* [Hints](doc/Hints.md)
* [Sample output](doc/Output.md)


## Overview

Pleased with the success of your fractal visualizer, your client recommended
DuckieCorp to a friend who is conducting research into the structure of the
World Wide Web (something to do with Russians and fake news, sounds like a scam
if you ask me!).  Given the time constraints we must work under, it seems
prudent to leverage existing solutions instead of re-inventing the wheel.

Your task is to use software libraries to write a recursive web crawler which,
given a starting URL, will visit all web pages reachable from that page, then
visit all pages reachable from those pages, etc., up to a specified maximum
depth.  Once a URL has been visited it must not be re-visited.  Due to the
World Wide Web's structure as an undirected graph of hyperlinks, a recursive
algorithm is the natural choice to traverse it.


## Objectives

*   Use recursion to solve a real-world problem
    *   Identify base cases
    *   Avoid infinite recursion
*   Leverage 3rd party libraries instead of re-inventing wheels
    -   urllib
    -   Requests
    -   BeautifulSoup
*   Understand how URLs are constructed
*   Design robust software by handling exceptions instead of crashing
