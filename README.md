This is a quick mock-up of Instagram using Django. It was among the first web projects for The Iron Yard's Data Science class.





# Django Social Site (data)

## Description

Structure and store "social" information into Django models.

## Learning Objectives

After completing this assignment, you should be able to:

 - Design the structure and relations of Django data models
 - Understand the importance of well structured data
 - Demonstrate knowledge of basic application model structure by mimicing how
 popular "social" sites may store their data.


## Details

### Deliverables

* A Git repo called django-movies containing at least:
  * a `requirements.txt` file
  * a `README.md` file
  * a Django project called whatever you want to name your application

### Normal Mode

VIDEO: Watch this video - https://www.youtube.com/watch?v=Sadng6tR7Q4

Django can be used in many ways - one particular way we've been demonstrating is by building a social
site similar to Twitter.  There are an incredible amount of web applications that could be considered
"social".  Your task is to mimic how you think a popular website has structured it's data so it can
operate.

A large element to this project is to think critically about "how" the application is storing it's data.
Take for example Facebook's wall - questions you may ask yourself when getting to the bottom of your design are:

 - How does an update relate to a user?
 - How does a user make comments tied to an update?
 - How can a user tag another user to an update?
 - How can you only see updates for people you follow?
 - How do you follow other people?

There are an infinite amount of questions you can ask yourself about how each social site works, your task
is to ask yourself these questions - and come to some conclusions.  And then design a models.py that
will back a potential "site clone" of the site you choose.

Make sure you use Managers and methods on your class in order to help the relations exist.  The more helpful
your data "layer" is to your application, the easier your application will be to write.

Come prepared to give a 5 minutes presentation on your structure.

Remember this tweet: https://twitter.com/taddeimania/status/565614127008464896

> "Database designed to application specification"

### Hard Mode

Fill your database with data either by using a data migration or by manually entering data through
a Django shell. Demonstrate how the relations work. Show how the managers and model methods help you
work with your data.
