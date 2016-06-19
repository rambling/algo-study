# -*- conding: utf-8 -*-
'''
Created on 2016. 6. 19.

@author: mitkim123

@note: 


문제



In mathematics, weird numbers are natural numbers that are abundant but not semiperfect. 
In other words, a natural number N is a weird number if and only if:
Sum of its proper divisors (i.e. less than N ) is greater than the number.
No subset of its divisors sum to N.

For example, the set of proper divisors of 12 is { 1, 2, 3, 4, 6 } . 
The sum of these numbers exceed 12, however, 12 is not a weird number since 1 + 2 + 3 + 6 = 12.
 However, 70 is a weird number since its proper divisors are {1, 2, 5, 7, 10, 14, 35} and no subset sums to 70 .

Write a program to determine if the given numbers are weird or not.



입력



In the first line of input, the number of test cases C ( <= 200 ) is given. 
In each of the following C lines, a natural number N_i is given. 
All input numbers are greater than 1, and less than or equal to 500,000 .



출력



Output will consist of C lines, each line containing either weird or not weird , 
denoting the weird-ness of the corresponding input.

'''
import copy

result_target = []

def main():
    print("Input the number of test cases C  (1�돞C�돞100)......")
    repeatCount = input()
    repeatTestCase(repeatCount)
    
def repeatTestCase(repeatCount):
    if(int(repeatCount) <= 0 or int(repeatCount) > 200):
        print("[Warning] the number of test cases C  (1<C<=200)")
        return

    for x in range(int(repeatCount)):
        print("Input number for weird....")
        inputNumber = input()
        
        if(int(inputNumber) <= 0 or int(inputNumber) > 500000):
            print("[Warning] the number of test cases C  (1<N<=500000")
            return
        resultNumbers = calculateWeirdNumber(int(inputNumber))
        printWeirdNumber(int(inputNumber), resultNumbers)
        

def calculateWeirdNumber(inputNumber):
    resultNumbers = [1]
    for i in range(2, inputNumber):
        if(inputNumber%i == 0):
            resultNumbers.append(i)
    return resultNumbers

def printWeirdNumber(inputNumber, resultNumbers):
    summary = 0
    for x in resultNumbers:
        summary = summary + x
    
    target = []
    combinations(target,resultNumbers, inputNumber)
    
    
    result = False
    for x in result_target:
        sumComp = 0
        for l in x:
            sumComp = sumComp + l
            if(sumComp == inputNumber):
                #print(sumComp)
                #print ("=============")
                #print(inputNumber)
                result = True
                break
           
    if(summary > inputNumber and not result):
        print("[OUTPUT] ==>  Weird Number")
    else:
        print("[OUTPUT] ==>  Not weird Number")

def combinations(target,data,inputNumber):
    for i in range(len(data)):  
        new_target = copy.copy(target)
        new_data = copy.copy(data)
        new_target.append(data[i])
        new_data = data[i+1:]
        #print (new_target)
        result_target.append(new_target)
        combinations(new_target,
                     new_data,inputNumber)

if __name__ == "__main__":
    main()
