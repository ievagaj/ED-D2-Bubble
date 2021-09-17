def pirms():
  print("Ieva")
s= [73, 101, 118, 97]
def sort(s):
  for i in range(len(s)-1,0,-1):
    for j in range (i):
      if s[j]>s[j+1]:
         temp=s[j]
         s[j]=s[j+1]
         s[j+1]=temp
         
s= [73, 101, 118, 97]  
sort (s)   
  
def pec():
  print("Iaev")

pirms()
print(s)
pec()