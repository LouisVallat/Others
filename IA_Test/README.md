# IA_Test.py

It looks like it is used to test and AI... But which one?

## A bit of background

In 2018 as I was doing my first Semester in the french "IUT d'informatique" in
Bordeaux, we had to code an AI, for a project we were working on. Basically it
was about a game where you had to respect some rules that were more and more
complex to implement and that was the first part of the project.
In the second part of this project, we had to code an AI that would be able to
compete against the ones coded by the other groups. It was a competition.
In order to test this AI we were working on, we all had the opportunity to
fight an AI made by the teacher that created this project.
This teacher-made AI had two difficulty levels: "lumberjack" (that was supposed
to be a stupid AI that just acts randomly) and "warrior" (that was a good
AI to fight against).

## Why this

In order to trigger the launch of the game, and the test of our AI against one of
the two ones named earlier, we had to delete the last game history, named
"partie2.log". Then after the game were played, we could see the result in a file
named "resultat". So in order to test my group's AI intensively, I created this
very little script (because I already saw before that Python was supported on
my School SSH server, and then I used no other libraries that the basic ones).

## How does it work

First of all this script is entering in a never-ending loop, waiting for the appearance
of the "resultat" file that contains what happened in the last game ("Win" or
"Loose" basically). Then after detecting that the last game is finished, it
increments the number of played games and prints it. Then it finds this file
and checks that it is not empty (ie. just created), and if it is not empty, then
it reads it and finds the line where there is my Uni e-mail adress, and prints
the game results ("Equality" being interpreted as a Win). Then it computes the
win/loose ration and prints it. Finally it moves the result file and keep it, and
deletes the partie2.log file so the test would start again and again, in a never-ending
loop.

## IA_Test_original.py

This is the first non-refactored version of this script, that was made by night
in an hour or two so yeah it has some weird things and dead code inside but I
needed sleep at this time, and wanted to code this little script quick and easy.
Dead code is a result from old methods and old ways to do what this script does
that were studied but later deleted.
