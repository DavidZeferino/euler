s = 0 
for i in range(999,100,-1):
  for b in range(999,i,-1):
    if i*b<s:
      break
    x = '%i'%(i*b)
    if x==x[::-1]:
      s = max(s,i*b)
      break
print s
