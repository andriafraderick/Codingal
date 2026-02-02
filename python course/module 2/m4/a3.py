#Input a number 
num = int(input("Enter the number : "))
t = num
numLen = 0
#iterate the loop
while t>0: 
  numLen = numLen+1
  t = int(t/10)

if numLen>=4: #condition 1
  numLen = int(numLen/2)
  chk = 0
  while num>0: #iterate loop
    rem = num%10
    if chk==numLen: #nested condition 1
      midOne = rem
    elif chk==(numLen-1): 
      midTwo = rem
    num = int(num/10)
    chk = chk+1
  prod = midOne*midTwo #product of middle digits
  #display the result
  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)

else:
  print("\nIt's not a 4 or more than 4-digit number!")