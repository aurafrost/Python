def reverse(text):
  n=len(text)-1
  reversed=""
  while(n>=0):
    reversed+=text[n]
    n-=1
  return reversed