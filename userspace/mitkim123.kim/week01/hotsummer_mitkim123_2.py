# -*- conding: utf-8 -*-
'''
Created on 2016. 5. 16.

@author: mitkim123
'''


def main():
    print("Input number repeat count...")
    result = []
    
    a = input() #�ݺ�Ƚ��
    for x in range(int(a)):
        b = input() # ��ǥ ���� ��뷮
        c = input() # 9���� ���� ��뷮
        
        total = 0
        for i in c.split(" "):
            total = total + int(i)
        if(total <= int(b)):
            result.append("YES")
        else:
            result.append("NO")
    
    for each_result in result:
        print (each_result) # ��� �� ���




if __name__ == "__main__":
    main()
