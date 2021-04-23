<h1 align=center><font size = 5>SIX DEGREES OF SEPARATION </font></h1>

# Introduction

According to the Six Degrees of Kevin Bacon game, anyone in the Hollywood film industry can be 
connected to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.

We’re interested in finding the shortest path between any two actors by choosing a sequence of movies that connects them. 
For example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: 
Jennifer Lawrence is connected to Kevin Bacon by both starring in “X-Men: First Class,” and Kevin Bacon is connected to Tom Hanks by both starring in “Apollo 13.”


# Data
There are three files in the folder imbd
- people.csv: 3 columns -  Id, Name and Birth
- movies.csv: 3 columns - Id, title, year
- stars.csv: 2 columns - person id, movie id

# Method

We will use
- depth-first search algorithm that always expands the deepest node in the frontier 
- breadth-first search algorithm that always expands the shallowest node in the frontier

# What's in the Repo?

 - util.py - logic to build a depth-first and breadth-first search alogrithm.
 - degrees.py - takes input of two stars and computes the shortest path between the two people, and prints out the path.
 
 # To Test
 
 run python degrees.py large
