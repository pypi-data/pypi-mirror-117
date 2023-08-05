===================
databasebaseclass
===================


This is some boilerplate code that I commonly use in my database classes.


Description
===========

There are a handful of things that I commonly use in my database classes, and I decided to put them in one spot.

* insert_or_merge replicates the ``MERGE`` function in SQL. I mostly use SqlAlchemy in my database projects, and there is currently no ``MERGE`` function. This is really only tested in Sqlite and Sql Server. (https://github.com/sqlalchemy/sqlalchemy/issues/5441)
* Logic to determine which dates have mot been processed. This makes it easier to run the script on a large set of days, and process any unprocessed days. If the server goes down, or the data flow stops working for some reason, this will back fill days. It makes the code more flexible.

Note
====

This project has been set up using PyScaffold 4.0.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.
