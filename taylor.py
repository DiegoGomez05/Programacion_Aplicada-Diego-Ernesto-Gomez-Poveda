def log(x,I):
  n=2
  acc=1
  p=x
  signo=1
  for n in range(I):
    L=P/n
    if L <0.01:
      break
    acc=acc + L*signo
    P=P*x
    signo = signo*-1
  return(acc)

log(1,10)
