monto = 900
es_cliente_vip = False
tiene_cupon = True

if monto > 1000 and es_cliente_vip or tiene_cupon:
    print("Se aplica descuento")
else:
    print("No hay descuento")


# En este caso nos muestra "Se aplica descuento. Para entender esto tenemos que tener en cuenta los operadores que tiene este codigo,
# ya que tenemos un and entre (if monto > 1000  y es_cliente_vip) pero para que se cumpla esta condicion ambas tiene que ser verdaderas si o si,
# como vemos ambas son falsas ya que el monto no supera los 1000 y tampoco es vip, esto no quiere decir que no se le aplique el--
# descuento ya que tiene un operador mas el cual es el or, una vez que se compararon las 2 falsas, se vuelve a comparar con el or --
#  el cual no requiere que ambas sean  verdaderas sino una de ellas, como vemos en la comparacion and nos dio false, pero en la variable--
# tiene_cupon, es igual a verdadera, por ende se cumple y aplica el descuento. podemos llevar este caso y verlo de una forma mas sencilla con numeros
# el and es como una (multiplicacion = numero * numero) y el or como una (suma = numero + numero) entonces:
# monto = 0 y es cliente_vip = 0, operacion = 0x0 = 0, tiene cupon = 1, (resultado final = 0 x 0 + 1 = 1) 