
numberinputs=int(input());
for x in range(numberinputs):
    length=int(input());
    telenumber=input();
    found=False;
    for i in range(length):
        if telenumber[i]=="8":
            found=True;
            if length-i-1>=10:
                print("YES");
                break
            else:
                print("NO");
                break
    if not(found):
        print("NO");