def isleap(year):
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0: 
                return(True)
            else:
                return(False)  
        else:
            return(True)
    else:
        return(False)

def ispali(year):
    year = str(year)
    if(year[::-1]==year):
        return(True)
    else:
        return(False)

def issumeven(year):
    sum = 0
    for digit in str(year):  
      sum += int(digit)       
    if(sum%2==0):
        return(True)
    else:
        return(False)

Y = int(input())


if(isleap(Y) and ispali(Y) and issumeven(Y)):
    print("YES")
else:
    print("NO")
    



