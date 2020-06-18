import re
s=input()
k=re.sub('[^aeiou]',"",s, flags=re.IGNORECASE)
print(k)
