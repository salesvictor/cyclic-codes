def degree(v):
  deg = -1;
  
  for i in range(len(v)):
    if v[i] != 0:
      deg = i

  return deg


def syndrome(v, g):
  q = []
  r = v.copy()

  for i in reversed(range(len(g))):
  

