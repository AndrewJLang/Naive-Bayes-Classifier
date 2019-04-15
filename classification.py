#Andrew Lang

import numpy as np
import csv

#hard coded value for where data becomes spam afterwards
countNoSpam = 8788
countSpam = 6712

#writes the data to separate files for training and testing according to the desired training batch size
def writeFiles(trainingFile, validationFile, trainingSize):
    with open("SpamInstances.txt") as base:
        with open(trainingFile, "w") as training:
            with open(validationFile, "w") as validation:
                count1 = 0
                for line in base:
                    count1 += 1
                    if count1 < int(countNoSpam * trainingSize):
                        training.write(line)                
                    if count1 > countNoSpam and count1 < (countNoSpam + int(countSpam * trainingSize)):
                        training.write(line)
                    if count1 >= int(countNoSpam * trainingSize) and count1 < countNoSpam:
                        validation.write(line)
                    if count1 >= (countNoSpam + int(countSpam * trainingSize)):
                        validation.write(line)

#the trainingSize parameter takes a value between 0 - 1 to get a 'percentage' of the data

#commented out so it should only be run when user desires to write values to separate files
# writeFiles('./TrainingSets/training_80.txt', './ValidationSets/validation_20.txt', 0.8)