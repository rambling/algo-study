# -*- conding: utf-8 -*-
'''
Created on 2016. 5. 16.

@author: mitkim123

@note: 

When transmitting *URI*s through the Internet, we escape some special characters in 
*URI*s with percent-encoding. Percent-encoding encodes an ASCII character into a percent 
sign ("%") followed by a two-digit Hexadecimal representation of the ASCII number. 
The other characters are not touched in the encoding process. 
The following table shows the special characters and their corresponding encodings:

Special Character

Encoded String

" " %20 
"!" %21 
"$" %24 
"%" %25 
"(" %28 
")" %29 
"*" %2a 

Note that the quotes are for clarity only.

Write a program which reverses this process.

입력

The first line of the input file will contain the number of test cases C  (1≤C≤100) . 
The following C  lines will each contain a test case — which is the percent-encoded URI. 
Their length will be at most 80.

출력

Print one line for each test cases — the decoded original URI.

예제 입력
2
Happy%20Joy%20Joy%21
http://algospot.com/%2a

예제 출력
Happy Joy Joy!
http://algospot.com/*

'''
resultUrl = []
maxLength = 80

def main():
    print("Input the number of test cases C  (1≤C≤100)......")
    initUri = input()
    
    if(int(initUri) <= 0 or int(initUri) > 100):
        print("[Warning] the number of test cases C  (1≤C≤100)")
        return

    for x in range(int(initUri)):
        print("Input any URI for decoding....")
        initUri = input()
        decodedUri = decodingUri(initUri)
        resultUrl.append(decodedUri)

    printDecodedUri()
    

def decodingUri(init_uri):
    decodedUri = init_uri.replace("%20", " ").replace("%21", "!").replace("%24", "$").replace("%25", "%").replace("%28", "(").replace("%29", ")").replace("%2a", "*")
    return decodedUri

def printDecodedUri():
    print ("[OUTPUT] ==> ")
    for x in resultUrl:
        if(len(x) > 80):
            print ("[Warning] Their length will be at most 80.")
            print (x)
            print ("##########################################################")
        else:
            print (x)
    

if __name__ == "__main__":
    main()
