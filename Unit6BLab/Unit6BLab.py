Weekend = {'Jan 2018' : [6,7,13,14,20,21,27,28],
           'Feb 2018' : [3,4,10,11,17,18,24,25],
           'Mar 2018' : [3,4,10,11,17,18,24,25,31],
           'Apr 2018' : [1,7,8,14,15,21,22,28,29],
           'May 2018' : [5,6,12,13,19,20,26,27],
           'Jun 2018' : [2,3,9,10,16,17,23,24,30],
           'Jul 2018' : [1,7,8,14,15,21,22,28,29],
           'Aug 2018' : [4,5,11,12,18,19,25,26],
           'Sep 2018' : [1,2,8,9,15,16,22,23,29,30],
           'Oct 2018' : [6,7,13,14,20,21,27,28],
           'Nov 2018' : [3,4,10,11,17,18,24,25],
           'Dec 2018' : [1,2,8,9,15,16,22,23,29,30]}

d = 1
x = input("Enter birthday month - ")
y = int(input("Enter brthday date - "))
for b in Weekend :
    if b==x :
        for c in Weekend[b] :
             if c==y :
                print("Your Birthday is on a weekend!")
if d==1 :
    print("Your birthday isn't a weekend!")
