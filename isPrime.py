def is_prime(x):
  if(x<=1):
    return False
  n=2
  while(n<=x-1):
    if(x%n==0):
      return False
    n+=1
  return True