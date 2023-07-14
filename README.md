# Diamondprediction
Searching for a sparkling diamond? 
Selecting a diamond starts by understanding the unique characteristics of each stone. Diamonds are graded based off the 4Cs - cut, colour, clarity and carat weight. 
The 4Cs of diamonds impact the stone’s beauty and value. 
Each of the individual 4Cs of diamonds may interact with one another to impact a stone’s overall appearance.

### Problem statement:
            To predict diamonds prices based on following features.

### About the dataset:

            This data includes information for over 54,000 diamonds, revealing the secrets of their prices and 9 other fascinating attributes. From the carat weight to the diamond's cut, color, and clarity, we'll explore every facet of these precious stones in our quest for knowledge. Let's get started!

### Features :

1. price: price is in US dollars . I have taken this as the target column for analysis. 

2. carat : Weight of a diamond between (0.2 to 5.01)

3. cut : Quality of the cut (Fair, Good, Very Good, Premium, Ideal). The more precise the diamond is cut, the more captivating the diamond is to the eye.  

4.color: Diamond color from J(worst) to D(best)

5.clarity : Measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))  

6.x : length in mm (0--10.74)

7.y : width in mm (0--58.9)

8. z : depth in mm (0--31.8)

9.depth % : The height of a diamond, measured from the culet to the table, divided by its average girdle diameter. Total depth percentage(43 to 79) = z/mean(x,y) = 2*z/(x+y)

10.table :Width(43 to 95) of the top of diamond relative to widest point

## Data Gathering :
The dataset has  53940 rows  and 10 columns. 
![image](https://github.com/GayatriBJ/Diamondpredict/assets/125629830/b03686d2-d7a6-4eb7-8c97-fd529ac856a9)

## EDA & Feature Engineering :
Encoding object columns into categorical columns.


