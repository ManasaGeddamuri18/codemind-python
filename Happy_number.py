n=int(input())
def man(n):
  s=0
  while(n!=0):
    r=n%10
    s+=r**2
    n=n//10
  return s
while(True):
 k=man(n)
 if(k==1):
   print("True")
   break
 else:
    n=k
 if(k>1 and k<10):
    print("False")
    break