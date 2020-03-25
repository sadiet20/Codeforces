t=int(input());     #number of trials
for x in range(t):
    num=int(input());        #number of boards
    lengthlist=[];
    lengthstring=input();         #all the lengths of the boards with spaces in between
    lengthlist=list(lengthstring.split());     #splits lengths at each space into different indices
    for i in range(num):
        lengthlist[i]=int(lengthlist[i])      #must be integers in order to sort correctly
    lengthlist.sort(reverse=True);       #sorts from biggest to smallest
    biggest=(lengthlist[0]);           #first index has the biggest possible square side
    for i in range(len(lengthlist)):        #take the biggest length with length k, then look out k-1 indices to see if that board has the same length (can make a square) if not, go out one less index (k-1-1) and see if it has one less than the biggest (k-1)
        if ((lengthlist[biggest-i-1])>=(biggest-i)):   #(biggest-i) is the width of all the boards (# of boards); lengthlist[biggest-i-1] is the length of the shortest board that we're looking at
            print(biggest-i);            #the width will potentially be smaller than the length, so in order for it to be a square, we must use the width
            break
