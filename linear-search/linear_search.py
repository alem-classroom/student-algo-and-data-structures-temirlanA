words = {"keyboard":"клавиатура","mouse":"мышка","computer":"компьютер","printer":"принтер","monitor":"монитор"}
def linear_search(lst, to_find):
  i=0#iterator starts from 0
  while (len(lst.keys()) > 0):
    if(list(lst.keys())[i] == to_find):
      return i
    i += 1
  return -1
