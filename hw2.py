import copy
import numpy as np
import math
from scipy.spatial import distance
np.set_printoptions(suppress=True)

## PROBLEM 1

def ohc(d, j): #a recursive method to transform any df into quantitative

    check = [] #empty list that holds categorical variables

    for i in range(1, len(d)):
        if(d[i][j] not in check): #if variable is unique, add it to check
            check.append(d[i][j])

    for k in range(0, len(check)):
        d[0].insert(k+1+j, str(d[0][j]) + check[k]) #adds a new column

    for i in range(1, len(d)): #fills in a a new column with either 1s or 0s
        for l in range(len(check)):
            if(d[i][j] == check[l]): #if it is the variable, 1
                d[i].insert(j+l+1, 1)
            else: #else add a 0 to the column
                d[i].insert(j + l + 1, 0)
        d[i].pop(j) #remove the categorical values

    d[0].pop(j) #removes the original x1, x2 etc
    j += len(check) #iterate however many cat variables there were
                    #over to move on to the next categotical column

    if(j == len(d[0])): #if were at the end, do fancy formatted printing
        s = [[str(e) for e in row] for row in d]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))
        print()
        # https://stackoverflow.com/questions/13214809/pretty-print-2d-python-list

        return d
    else: #else keep on going in the column
        ohc(d, j)
        return d


def sampleMean(d, column):


    sum = 0
    for row in d:

        sum += round(row[column], 2)
    #Adds up values in the column number and divides it by total number of rows


    mean = sum/len(d)
    return mean

def sampleVariance(d, col):
    sum = 0
    mean = sampleMean(d, col)

    for row in d: #formula for sample covariance
        sum+=((row[col] - mean) **2)
    return sum/(len(d)-1)


def main():

    # Create data matrix
    d = [["  ", "X1", "X2", "X3"],
         ["x1", "red", "yes", "North"],
         ["x2", "blue", "no", "South"],
         ["x3", "yellow", "no", "East"],
         ["x4", "yellow", "no", "West"],
         ["x5", "red", "yes", "North"],
         ["x6", "yellow", "yes", "North"],
         ["x7", "blue", "no", "West"]]

## PROBLEM 1
    print()
    y = ohc(d, 1)
    y.pop(0) #pop is to remove formatted row and column labels
    for row in y:
        row.pop(0)
        print(row)

## PROBLEM 2
    print()

    a = [] #a and b are our vectors
    b = []
    for i in range(len(y[2])): #creates vectors
        a.append(y[1][i])
        b.append(y[6][i])

    dst = distance.euclidean(a, b) #I know the formula, but np has
    print("Euclidian Distance: " + str(dst)) #a euclidian method

## PROBLEM 3
    print()

    #s/d, or
    #dot product/lengthA * lengthB

    #la, lb are length of vectors
    la = math.sqrt(np.dot(a, a))
    lb =math.sqrt(np.dot(b, b))

    d = (la * lb) #d = number of attributes
    s = np.dot(a, b) #s = number of matching attributes

    print("Cosine Similarity: " + str(s/d))


## PROBLEM 4
    print()

    #d - s
    # we already have s and d from problem 3, so...
    print("Hamming Distance: " + str(d-s))

## PROBLEM 5
    print()

    #s/(2d-s)
    #we already have s and d from problem 3, so...
    print("Jaccard coeficcent: " + str(s/(2*d - s)))

## PROBLEM 6
    print()

    means = [] #vector of each columns mean
    for i in range(len(y[0])):
        mean = sampleMean(y, i)
        means.append(mean)
    print("Mean of Y: " + str(means))


## PROBLEM 7
    print()
    sum = 0

    for row in y: #formula for sample variance
        sum+=((row[0] - sampleMean(y,0)))**2
    print("sample variance of col 1: " + str(sum/(len(y)-1)))


## PROBLEM 8
    print()
    z = copy.deepcopy(y)

    #formula= xi - mean / sd
    for i in range(len(z[0])):
        mean = sampleMean(y, i)
        sv = sampleVariance(y, i)
        for j in range(len(z)):
            z[j][i]=((z[j][i] - mean))/math.sqrt(sv)

    for row in z:
        print(row)

## PROBLEM 9
    print()

    means = [] #vector of each columns mean


    for i in range(len(z[0])):

        mean = sampleMean(z, i)

        means.append(mean)
    print("Mean of Z: " + str(means))


## PROBLEM 10
    print()
    a = []
    b = []
    for i in range(len(z[2])):
        a.append(z[1][i])
        b.append(z[6][i])

    dst = distance.euclidean(a, b)
    print("Euclidian Distance: " + str(dst))



main()