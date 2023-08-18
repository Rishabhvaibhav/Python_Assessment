def fibo(x):
    a = 1
    b = 1
    if x == 1:
        print("0")
    elif x == 2:
        print('0' , "1")
    else:
        print("0",a,b,end = " ")
        
        for i in range (x-3):
            result = a + b
            b = a 
            a = result
            print(result , end = " ")
            
fibo(12)
