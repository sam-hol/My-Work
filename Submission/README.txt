Details:
VAMSIKRISHNA NEELAM - neelam.11@wright.edu - U01074399

Explanation of the Program and Algorithm:
Initially we all read the data from the input file and assume that all men and women are free
Now we will pickup a free men who has not proposed to any women and select his highest preferred women
We will check if the selected women is free, if she is free we will engage them to be a pair
if the selected woman is not free then we will check her preference to current partner and proposed partner
if she prefers the current partner than engaged partner then she will reject the proposing partner 
else she prefers the proposing partner than the current partner then their current engagement will be broken and 
the woman will be engaged to the new proposing partner.
This process continues untill all the men and engaged with all the women.

Steps to run the program:
when trying to run the program it is must to provide the input arguments as shown below

  py assignment1.py INPUT_ARGUMENT(your input argument goes here)

We must provide only one argument as shown here, if we provide no arguments or provide more than one argument
the python program will not execute and print an alert on the console window.