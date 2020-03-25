#Codeforces Contest Round #618 Div 2 Problem A: Non-zero
#Accepted

from sys import stdout

def multzero(listnums):
    total = 0
    for i in range(len(listnums)):
        if listnums[i]==0:
            listnums[i] +=1
            total +=1
    return total

def sumzero(listnums):
    sum = 0
    highest = 0
    lowest = 0
    for i in range(len(listnums)):
        if listnums[i]>listnums[highest]:
            highest = i
        if listnums[i]<listnums[lowest]:
            lowest = i
        sum += listnums[i]
    if sum==0:
        if listnums[highest]>=0:
            return 1
        return 2
    return 0

def main():
    total = 0
    repeat = int(input())
    listnums = []
    for x in range(repeat):
        length = int(input())
        stringnums = input()
        listnums = stringnums.split()
        listnums = [int(i) for i in listnums]
        total = multzero(listnums)
        total += sumzero(listnums)

        print(total)
        stdout.flush()

main()