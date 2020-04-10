# CS 1440 Assignment 5 Rubric

| Points | Criteria
|:------:|-----------------------------------------------------------------------------------------------------------
| 15     | Program runs without crashing<br/>Getting hung up (or freezing) on some websites is *not* penalized. Catch exceptions, print error messages and continue to the next URL instead of crashing
| 15     | Maximum recursion depth can be overridden from command line<br/>By default the maximum recursion depth is limited to 3 levels
| 15     | Visited URLs are printed to the screen<br/>Recursion Depth is indicated in program output by indenting with four spaces per level
| 20     | Visited URLs are recorded in a set and are not re-visited
| 25     | `crawl()` is recursively called from within itself up to `maxdepth` calls deep<br/>Base case(s) prevent unbounded recursive calls


**Total points: 90**


## Penalties

*   This assignment is *not* eligible for the grading gift.  This due date cannot be moved.
*   Review the Course Rules document to avoid general penalties which apply to all assignments.
    *   **10 point penalty** Pay attention to the name you give your repository on GitLab.
    *   **10 point penalty per file** Don't forget to include your *Software Development Plan* and *Sprint Signature* documents in the `doc/` directory.
    *   Verify your submission on GitLab.
*   Use only the libraries named in the [Instructions](Instructions.md).  If your code imports a library which your grader doesn't happen to have installed on that computer the resulting `ModuleNotFoundError` will be treated as a crash and penalized at 50% of the assignment's value.
