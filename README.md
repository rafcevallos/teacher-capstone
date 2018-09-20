# G.R.E.A.T. - Guided Reading Elementary Assessment Tracker
Back-end Capstone Project

## About This Repo

This application is intended to replace a physical binder used by elementary school teachers that tracks student reading levels. It is used for creating and handling the database for a teacher: students, books, skills, observations, and conference logs. It is built using Python, Django, SQLite, and styled with Bulma.

## Table of Contents

[Installation](#installation)  
[Tables](#tables)  
[Usage](#usage)  


# Installation

## Requirements
1. Python3
1. SQLite3
1. Django
1. Bulma

## PIP dependencies for this app
1. django
1. django_seed (if you intend to seed the database for testing)
1. multiselectfield
1. pillow
1. widget_tweaks

## Steps
1. download or clone the repository
1. to run the server cd into the root 'readapi' directory and run `python manage.py runserver`
1. Visit the [application url/register](http://127.0.0.1:8000/register "Default Django local URL") specified by the terminal

# Tables

## Student
* teacher | Foreign Key to user table
* first_name | String
* last_name | String
* student_photo | File Field
* notes | String
* reading_level | String
* skills | String

## Book
* book_photo | File Field
* title | String
* author | String
* level | String
* word_count | Integer
* unit | String
* genre | Foreign Key to genre table
* notes | String

## Conference Log
* date | Date formated as 'yyyy-mm-dd'
* student | Foreign Key to student table
* book | Foreign Key to book table
* strategy | Join table with strategy table
* observation | Join table with observation table
* reading_level | Foreign Key to readinglevel table
* comments | String

## Training
* name | String
* description | String
* start_date | Date formated as 'yyyy-mm-dd'
* end_date | Date formated as 'yyyy-mm-dd'
* max_attendees | Integer
* attendees | Join table wth Employees

## Genre
* name | String

## Observation
* name | String

## Profile
* user | One to One field on user table
* classroom | String
* phone | String

## ReadingLevel
* level | String

## Skill
* name | String
* is_reader | Boolean
* reading_level | Foreign Key on readinglevel table

## Strategy
* name | string


# Usage
after opening the [application url/register](http://127.0.0.1:8000/register "Default Django local URL") to reach the main page of the application, there will be various navigation buttons to reach the different components for each feature. From the separate pages users are able to perform the following tasks:

## Search
1. Search by student reading levels
1. Be presented with all the students for a level e.g. Level A

## Index and Student
1. Add new students
1. View the list of all students
1. View the details of individual students which should also list all conference logs for that student.
1. Edit/Update student info
1. Remove a student

## Books
1. Create new books
1. View the list of all books
1. View the details of individual books
1. Edit the book details
1. Delete a book

## Conference Log
1. Create a new conference log for a student
1. View the list of all conference logs for a student in their detail view
1. View the details of individual training programs which should also provide information about which student and which book and the date
1. Edit the details of a conference log
1. Delete conference logs

## Reading Levels
1. View characteristics of texts at levels A-F
1. View characteristics of readers at levels A-F

## Profile
1. Will display a teachers classroom number and classroom phone **(not yet implemented)**
