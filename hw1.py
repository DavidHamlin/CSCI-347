import math

import numpy as np
np.set_printoptions(suppress=True)

#PROBLEM A)
def sampleMean(df, column):
    column = column-1
    #I do this at the start so i can enter
    # column 1 because index of array starts at 0
    sum = 0
    for row in df:
        sum += row[column]
    #Adds up values in the column number and divides it by total number of rows
    mean = sum/len(df)
    return mean

#PROBLEM B)
def sampleCovariance(df, col1, col2):
    sum = 0
    mean1 = sampleMean(df, col1)
    mean2 = sampleMean(df, col2)
    col1 = col1 - 1
    col2 = col2 - 1

    for row in df: #formula for sample covariance
        sum+=((row[col1] - mean1) * (row[col2] - mean2))

    return sum/(len(df)-1)

#PROBLEM C)
def totSampleMean(df):
    return str(sampleMean(df, 1)) +"   " \
           +str(sampleMean(df, 2)) + "   "+str(sampleMean(df, 3))

#PROBLEM D)
def sampleVariance(df, col):
    return sampleCovariance(df, col, col)

#PROBLEM E)
def covarianceMatrix(df):
    s = np.zeros(shape=(len(df[0]),len(df[0])))
    #s is our covariance matrix, that populates it with 0s

    # and this populates it with the sample covariance
    for row in range (len(s[0])):
        for col in range (len(s[0])):
            s[row][col] = sampleCovariance(df, row+1, col+1)
            #its expecting human vals so i have to add one
    return s

#PROBLEM F)
def correlation(df, col1, col2):
    col1 = col1-1
    col2 = col2-1 #formula for correlation
    return sampleCovariance(df, col1, col2)/(math.sqrt(sampleVariance(
        df, col1))*math.sqrt(sampleVariance(df, col2)))

#PROBLEM G)
def totVariance(df):
    sum = 0
    for row in range(len(df)):
        sum+=sampleVariance(df, row)
    return sum

def main():

    #Create data matrix
    d = [[.3, 23, 5.6],
         [.4, 1, 5.2],
         [1.8, 4, 5.2],
         [6, 50, 5.1],
         [-.5, 34, 5.7],
         [.4, 19, 5.4],
         [1.1, 11, 5.5]]

    print("Data Matrix D =")
    for row in d:
        print()
        for element in row:
            print(str(element) + " ", end='')

    #Prints out answers by calling methods with appropriate params
    print()
    print()
    print("A) Sample Mean= "  + str(sampleMean(d, 3)))
    print()
    print()
    print("B) Sample Covariance= " + str(sampleCovariance(d, 1, 3)))
    print()
    print()
    print("C) Sample Mean of data set= " + "("+ totSampleMean(d) + ")")
    print()
    print()
    print("D) Sample Variance= " + str(sampleVariance(d, 2)))
    print()
    print()
    print("E) Covariance Matrix= ")
    print((covarianceMatrix(d)))
    print()
    print()
    print("F) Correlation= " + str(correlation(d, 1, 3)))
    print()
    print()
    print("G) Total Variance= " + str(totVariance(d)))



main()