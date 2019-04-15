# Instructions:

 - This program was compiled and ran on python 3.7.1. The libraries used were csv and numpy. Both files need to be ran separately, although classification.py should only need to be run once for a given test size.

 - Training and validation files are given at 80/20 separation to see how program works

Classification.py:

This file separates the main data file into two separate files for training and validation.

NaiveBayesClassifier.py:

All computational work for categorizing emails is done within this file.

This file uses Naive Bayes classification to categorize emails into spam or no spam.  The precision, recall, and accuracy are all calculated within this file.

The user only needs to change the parameters that are passed to the convertDataSet method, as has to be called on both test and training files to convert them.
