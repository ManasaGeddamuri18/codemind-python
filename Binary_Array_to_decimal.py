n=int(input())
s=list(map(int,input().split()))
# a=sum(s)
# c=a//n
# h=0
for i in range(len(s)):
    s[i]=str(s[i])
a="".join(s)
print(int(a,2))
#         h+=1
# print(h)        
#         c.append(k[i])
# if(len(c)==0):
#     print(-1)
# else:
#     print(max(c))