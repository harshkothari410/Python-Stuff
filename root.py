#Creater : Harsh Kothari
number = float (raw_input("Enter the Number:"))
a = number/4;
count = 0
while(1):
    temp = a * a;
    count = count +1
    temp = round(temp,2)
    if temp>(number + number*(0.001)) or temp<(number - number*(0.001)):
        #print "%d a:%f" % (count,a)
        b = number/a
        a = (a+b)/2
        a = round(a,2)
        #print a
    
    else:
        print "Root is :",a
        break