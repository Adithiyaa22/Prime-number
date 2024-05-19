N = int(input("Enter a  Number : "))
#Intialize a Variable to 0 to make a prime number
Flag = 0
for i in range (1,N+1):
    if(N%i==0):
        Flag+=1 #increment value to flag variable 
if(Flag==2):
    print(N,"is a Prime number")  #when the input number is dvided by the range , totally prime is when only two num's are divided (number by itself and 1 always)
else:
    print(N,"is not a Prime number")