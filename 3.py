from collections import Counter
def remov_duplicates(st):
   st = st.split(" ")
   for i in range(0, len(st)):
      st[i] = "".join(st[i])
   dupli = Counter(st)
   s = " ".join(dupli.keys())
   print (s)


st = input("Enter the sentence")
remov_duplicates(st)
