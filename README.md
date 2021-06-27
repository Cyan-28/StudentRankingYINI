# StudentRankingYINI
StudentRankingYINI Test


Student Ranking YINI final.py is the final version. PLEASE USE THIS.

At first in version 1, I created a simple class called score which takes in 7 different parameters and calculates the average and progress score. These functions
are in the same class, which is different to what was asked. This version was merely a test to see how I could potentially use classes in the problem.

In version 2, I separted out into 2 different classes and now the only thing left was to import the test data from the xl file. I started experimenting with the openpyxl
library and found that there many different ways of apporach. Learning this, I decided to start on version 3. 

In version 3 (aka Student Ranking YINI final.py), I first import the libraries I am going to use, openpyxl. I create a few arrays which will store the data from the xl file.
My method of approach was to separate each indivdual needed colunmn into an array where I can potentially use a for loop to calculate the average and progress average then compare. Similar to before I have 2 classes, average and progress, which will calculate the needed outcome. I also have a function called getData which will get all the needed data from the xl file and sorts into respective array. An instance of a class can be made and the respective arrays can be fed through and the answer can be calculated by using the right function. 
