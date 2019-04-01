# Jane.ai Take Home

1. Design a set of SQL tables for a blog. Include users, comments, blog posts, and any other objects you feel are
   relevant. Please include comments for fields that might be unclear. MySQL is the ideal database to target, but if
   you're not familiar with it, others are also acceptable.

2. Using http://jsonplaceholder.typicode.com, write a script to get the 200 most recent TODOs, create a TODO,
   and delete a TODO given an ID.

3. Write a script which prints all the permutations of a string in alphabetical order. We consider that digits < upper
   case letters < lower case letters. The sorting should be performed in ascending order.
   Your program should accept a file as its first argument. The file contains input strings, one per line. Print to
   stdout the permutations of the string separated by comma, in alphabetical order.
   Contents of sample input file:

## Tech Used

---

I use pyenv and pipenv in all of my python enviornments for python version selection as well as pipenv to make the process easier on virtual env management

https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c

You can follow the install directions found in the article above or you can just look at the imports and create a requirements.txt and install from there. If you like pipenv benefits of pipfile.lock you can visit: https://pipenv.readthedocs.io/en/latest/basics/ and then search the page for the heading, `Importing from requirements.txt` and follow those directions to install from a requirements.txt with pipenv.

## Explanation for Blog.py

---

The task required me to design some sql tables with relationships. I elected to use SQLAlachemy for this creation as if I was writting a flask application. I felt like this was within the scope of the task so I used that ORM for the creation. I did write a complete application and can include that if more perspective is needed.
