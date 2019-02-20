def remove_duplicates(lst):
  newList=[]
  for i in range(len(lst)):
    if(lst[i] not in newList):
      newList.append(lst[i])
  return newList