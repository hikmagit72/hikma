


n=int(input("inter how many terms:"))
fibo= [0,1]
for i in range(2,n):
    fibo.append (fibo[i-1]+fibo[i-2])
    print(fibo)