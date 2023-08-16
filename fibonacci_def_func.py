def fibo(n):
    a = 1
    b = 1
    
    if n == 1:
        print("0")
    elif n == 2:
        print("0","1")
    else:
        print("0",a,b, end = " ")
        
        for i in range (n-3):
            res = a + b
            b = a 
            a = res
            print(res, end = " ")
            
            
times = 0
while times < 10:
    try:    
        z = int(input("enter the number of terms fibo series : "))           
        fibo(z)
        print()
        times  += 1
    except ValueError:
        print('Invalid input ')
        

            