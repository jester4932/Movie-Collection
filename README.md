# Movie Collection
Allowing users to View, Add and Delete movie collection while also rating the top 5

>Files Needed:
>- Python 3.9
>- bottle
>- CherryPy
>- SQLAlchemy

### Where to see it
I have it up and running on AWS at http://ec2-18-209-172-166.compute-1.amazonaws.com

### A Brief Summary
I am using sqlalchemy to create a local database using sqlite, but you could spin up a postgres database to do the same 
thing by changing the 'engine' variable in the database.py module to point to it. When app is started it will create a 
file called moviecollection.db(this is the database) and put it in the working directory. The database will have 
3 entries in it that are hard coded in the utilities.py module. The database_reset function in utilities.py deletes all 
entries in the moviecollection.db file and resets it to original 3. This is done so that every time the app is restarted, 
it does not add 3 more of the original entries into the database making it grow by 3 every time. When a new feature 
suggestion is added, the priority level will be checked against the database and any with an equal or lower priority 
will be moved to the next priority level with 1 being the favorite and 5 being the least favorite.