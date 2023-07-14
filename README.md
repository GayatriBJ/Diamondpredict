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

In this step, we have to analyze the data. We check for :
1) checking & handling missing values
2) identify outliers
3) remove outliers
4) encoding of categorical variables
5) Feature Transformation
6) Scaling

## Feature Selection / Feature Extraction :

The goal of feature selection techniques in machine learning is to find the best set of features that allows one to build optimized models of studied phenomena.
It helps Improves Model Performance
It helps Optimizes Model Training Time

Feature Selection Methods : 
1) Filter Method      
2) Wrapper Method
3) Embedded Method  

## Model Training :

In this step, Model is train using different machine learning techniques. I have used Linear Regression.

After performing standardization, dataset is splited with a ratio of 0.2 that means 80% data for training and 20% data for validation process.

## Model Evaluation : 

To check model is performing well on training data set as well as testing data data we need evaluate the model using metrics 

Metrics used are : 
1) Mean Square error
2) Mean Absolute error
3) Squareroot of Mean Square error
4) R2 score
5) Adjusted R2 score


## Web development Framework :
In this project flask method is used to write API's for the project so that user can interacte with help of html web to input the value and to get the output

## Deployment on AWS :
For public access we have used AWS service, so that anyone can access the website and can use to get the results.

## Important Files

### interface.py :-

In this file we have write the API's and by running this file you can start server.

### util.py :-

This file contains the basic function that will help to interface file to get the results

### config.py :-

In this file you can change the file path for the pickle file and json file. Also, you can change the port number according to the requirement

### requirement.txt :-

This file contain necessary libraries and its version, user need to install this libraries while running this project.

### source.html :-

This html file, contain website page coding.

