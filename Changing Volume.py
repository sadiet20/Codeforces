t=int(input());
for x in range(t):
    aandb=(input());
    a, b=aandb.split();
    a=int(a);
    b=int(b);
    dif=b-a;
    changes=0;
    while (dif!=0):
        if (dif>=20 or dif<=-20):          #shortcut for huge differences
            if (dif%5==0):
                changes+=abs(int(dif/5));      #absolute value in case difference is negative
                break
            elif ((dif+2)%5==0):
                dif+=2;
                changes+=abs(int(dif/5)) +1;
                break
            elif ((dif-2)%5==0):
                dif-=2;
                changes+=abs(int(dif/5)) +1;
                break
            elif ((dif+1)%5==0):
                dif+=1;
                changes+=abs(int(dif/5)) +1;
                break
            else:
                dif-=1;
                changes+=abs(int(dif/5)) +1;
                break
        elif (dif>0):      #volume must go up
            if (dif>=4):
                a+=5;
                dif-=5;
            elif (dif>=2):
                a+=2;
                dif-=2;
            else:
                a+=1;
                dif-=1;
        else:              #volume must go down
            if (dif<=-4 and a>=5):
                a-=5;
                dif+=5;
            elif (dif<=-2):
                a-=2;
                dif+=2;
            else:
                a-=1;
                dif+=1;
        changes+=1;

    print(changes)

