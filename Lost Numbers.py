from sys import stdout

def possibilites(product, thelist):
    for k in numbers:
        if product%k==0:
            new=product/k
            if new in numbers:
                thelist.append(k)
                thelist.append(int(new))
                return

def overlap(list1, list2):
    for k in list1:
        if k in list2:
            second=k
            list2.remove(k)
            third=list2[0]
            numbers.remove(second)
            numbers.remove(third)
        else:
            first=k
            numbers.remove(first)
    return first, second, third

numbers=[16, 15, 23, 42, 8, 4];
poss1=[]
poss2=[]
poss4=[]
poss5=[]

print("? 1 2\n");
stdout.flush();
input1=int(input());
possibilites(input1, poss1)

print("? 2 3\n");
stdout.flush();
input2=int(input());
possibilites(input2, poss2)
first, second, third = overlap(poss1, poss2)

print("? 4 5\n")
stdout.flush()
input3=int(input())
possibilites(input3, poss4)

print("? 5 6\n")
stdout.flush()
input4=int(input())
possibilites(input4, poss5)
fourth, fifth, sixth = overlap(poss4, poss5)

print("! {} {} {} {} {} {}\n".format(first, second, third, fourth, fifth, sixth))
stdout.flush()