#Andrew Lang

import numpy as np

# -1 is a no spam email and 1 is a spam email

#converts the strings within the files into integer arrays, one for their label, one for their feature vector
def convertDataSet(dataset): #pass it the file that you wish to read values from
    stringTraining = []
    with open(dataset) as training_file:
        stringTraining = training_file.readlines()

    data = []
    for x in range(len(stringTraining)):
        split = stringTraining[x].split()
        data.append(split)

    label = [] #label of spam or not
    for x in range(len(data)):
        labelpoint = int(data[x][1])
        label.append(labelpoint)
        
    datapoint = [] #array of values 
    for x in range(len(data)):
        point = [int(i) for i in str(data[x][2])]
        datapoint.append(point)

    return label, datapoint

#the inputs will need to be changed according to what the training to validation size is desired to be
labels, datapoints = convertDataSet('training.txt') #values that will be used as base probabilities
validationLabels, validationData = convertDataSet('validation.txt') #the data that will be tested to see how classification goes

#count the amount of spam versus not spam
spamProb, noSpamProb = 0 , 0
for x in range(len(labels)):
    if labels[x] == -1:
        noSpamProb += 1
    if labels[x] == 1:
        spamProb += 1

#counting how many times each word appears in either spam or no spam
spamValues = np.zeros((spamProb))
noSpamValues = np.zeros((noSpamProb))
for x in range(len(datapoints)):
    for i in range(len(datapoints[x])):
        if labels[x] == 1: #if the email is spam
            if datapoints[x][i] == 1:
                spamValues[i] += 1
        if labels[x] == -1:
            if datapoints[x][i] == 1:
                noSpamValues[i] += 1

#calculate probability that it's spam
spamProbArray = []
for x in range(len(validationData)):
    probabilitySpam = 1
    for i in range(len(validationData[x])):
        if validationData[x][i] == 0:
            probabilitySpam *= (1 - (spamValues[i] / spamProb))
        if validationData[x][i] == 1:
            probabilitySpam *= (spamValues[i] / spamProb)
    spamProbArray.append(probabilitySpam)

#calculate probability that it's not spam
nospamProbArray = []
for x in range(len(validationData)):
    probabilitySpam = 1
    for i in range(len(validationData[x])):
        if validationData[x][i] == 0:
            probabilitySpam *= (1 - (noSpamValues[i] / noSpamProb))
        if validationData[x][i] == 1:
            probabilitySpam *= (noSpamValues[i] / noSpamProb)
    nospamProbArray.append(probabilitySpam)

#pick the higher probability (spam or not spam) and appoint it a label
classification = []
count = 0
for x in range(len(spamProbArray)):
    if spamProbArray[x] > nospamProbArray[x]:
        classification.append(1) 
    if spamProbArray[x] < nospamProbArray[x]:
        classification.append(-1)
    #if values are the same for prob, then assume that it is spam
    if spamProbArray[x] == nospamProbArray[x]:
        classification.append(1)

#computes the accuracy, recall, and precision for the test dataset
accuracy = 0
truePosSpam, truePosNoSpam = 0 , 0
falsePosSpam, falsePosNoSpam = 0 , 0
falseNegSpam, falseNegNoSpam = 0 , 0
for x in range(len(validationLabels)):
    if validationLabels[x] == classification[x]:
        accuracy += 1
        #need to calculate the precision
        if validationLabels[x] == 1:
            truePosSpam += 1
        if validationLabels[x] == -1:
            truePosNoSpam += 1
    if validationLabels[x] != classification[x] and validationLabels[x] == 1:
        falsePosNoSpam += 1
        falseNegSpam += 1
    if validationLabels[x] != classification[x] and validationLabels[x] == -1:
        falsePosSpam += 1
        falseNegNoSpam += 1

precisionSpam = float(truePosSpam / (truePosSpam + falsePosNoSpam))
precisionNoSpam = float(truePosNoSpam / (truePosNoSpam + falsePosSpam))

recallSpam = float(truePosSpam / (truePosSpam + falseNegNoSpam))
recallNoSpam = float(truePosNoSpam / (truePosNoSpam + falseNegSpam))

#report values
print("Accuracy: %f" % (float(accuracy / len(validationLabels))))
print("Precision Spam: %f\tPrecision No Spam: %f" % (precisionSpam, precisionNoSpam))
print("Recall Spam: %f\tRecall No Spam: %f" % (recallSpam, recallNoSpam))