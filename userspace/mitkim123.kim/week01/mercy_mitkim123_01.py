# -*- conding: utf-8 -*-
'''
Created on 2016. 5. 16.

@author: mitkim123
'''


def main():
    print("Input number ...")
    a = input()
    count = int(a)
    if(count>0):
        print("Hello Algospot!\n" * count)
    else:
        print("[Warning]Input number should be > 0")




if __name__ == "__main__":
    main()
