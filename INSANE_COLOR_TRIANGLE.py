def triangle(row):
    reduce=[3**i+1 for i in range(10) if 3**i<=100000][::-1]
    for length in reduce:
        while len(row)>=length:
            row=[row[i] if row[i]==row[i+length-1] else ({"R","G","B"}-{row[i],row[i+length-1]}).pop() for i in range(len(row)-length+1)]
    return row[0]



# pattern
# a      b         c        d
#  2(a+b)   2(b+c)   2(c+d)
#    4(a+2b+c) 4(b+2c+d)
#      8(a+3b+3c+d)


# formula 
# 2^n*(Sum((n,k)*xk))
# where (n,k) is binomial coefficient


# finally
# if n%3==0, any k, (n,k)%3==0
