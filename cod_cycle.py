import itertools

def multiply(p, q):
  r = []
  deg = len(p)+len(q)-1

  for i in range(deg):
    coef = 0

    p_aux = p + list(itertools.repeat(0, deg-len(p)))
    q_aux = q + list(itertools.repeat(0, deg-len(q)))

    for k in range(i+1):
      coef += p_aux[k]*q_aux[i-k]
    r.append(coef%2)
  return r


n = 8
k = 5
g = [1, 1, 1, 1]

U = [list(u) for u in itertools.product([0, 1], repeat=k)]
for u in U:
  print(u)
print()

V = []
for u in U:
  V.append(multiply(g, u))

for v in V:
  print(v)
print(len(V))
