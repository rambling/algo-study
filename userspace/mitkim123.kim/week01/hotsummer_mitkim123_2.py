# -*- conding: utf-8 -*-
'''
Created on 2016. 5. 16.

@author: mitkim123
'''


def main():
    print("Input number repeat count...")
    result = []
    
    a = input() #반복횟수
    for x in range(int(a)):
        b = input() # 목표 전력 사용량
        c = input() # 9개의 전력 사용량
        
        total = 0
        for i in c.split(" "):
            total = total + int(i)
        if(total <= int(b)):
            result.append("YES")
        else:
            result.append("NO")
    
    for each_result in result:
        print (each_result) # 결과 값 출력




if __name__ == "__main__":
    main()
