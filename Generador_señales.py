def Generado_de_señales(x,f,A,duty,offset):
  print("Bienvenido, ofrecemos señales: cuadrada, triangular, cosenosoidal")
  Tipo_señal=String(input("¿Qué tipo de señal desea"))
  t=(1/512)*x
  if Tipo_señal=="Cuadrada":
    T=1/f
    t_pos<= t%T
    if t_pos<=(duty/100)*T :
      y=A/2 + offset
    else:
      y=-A/2 + offset
  elif Tipo_señal=="trianfular":
    señal=(t%T)/T
    señal=(A/T)*t - A/2
    y= señal + offset
  elif Tipo_señal == "cosenosoidal":
    y=A*cos(2*pi*f*t)
    y= y + offset
  else:
    print("funcion no conocida")
  PY=-6.4*y+64
  Voltaje = PY
  return Voltaje
  
Generador_de_señales(1,1,1,1,1)
    
    
  


  
  
