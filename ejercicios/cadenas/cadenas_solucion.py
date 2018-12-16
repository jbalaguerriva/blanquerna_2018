
# A. donuts
# Devuelve (si count < 10) la cadena 'Número de donuts: x', siendo x el número que se le pasa en count (p.ej, para 5 ==> "Número de donuts: 5')
# Si count >= 10, devuelve: 'Número de donuts: muchos'
def donuts(count):
  if count < 10:
    return 'Número de donuts: ' + str(count)
  else:
    return 'Número de donuts: muchos'


# B. principio_y_fin
# Dada la cadena 's', devuelve una cadena 'hecha' de los 2 primeros y los 2 últimos caracteres de la cadena original
# P.ej: "primavera" devuelve "prra"
def principio_y_fin(s):

  return s[:2] + s[-2:]


# C. cambia_segun_comienzo
# Dada una cadena 's', devuelve una cadena donde todas las 'ocurrencias' del primer carácter
# se cambian por '*' (NO cambiar el primer carácter)
# P.ej: 'atalaya' se convierte en 'at*l*y*'
def cambia_segun_comienzo(s):
  front = s[0]
  back = s[1:]
  fixed_back = back.replace(front, '*')
  return front + fixed_back


# D. mezcla
# Dadas las cadenas 'a' y 'b' devuelve una sola cadena con 'a' y 'b' concatenadas, pero 'cambiando' los dos caracteres de cada cadena
# por los de la otra
# Ejemplo:
# 'mesa', 'silla' ==> 'sisa mella'
# 'sol', 'luna' ==> 'lul sona'
def mezcla(a, b):
  a_swapped = b[:2] + a[2:]
  b_swapped = a[:2] + b[2:]
  return a_swapped + ' ' + b_swapped


# Compara 'got' con 'expected' y devuelve OK o 'X' (erróneo) y lo que obtiene vs lo esperado
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s salida real: %s esperado: %s' % (prefix, repr(got), repr(expected)))


print('donuts')
test(donuts(4), 'Número de donuts: 4')
test(donuts(9), 'Número de donuts: 9')
test(donuts(10), 'Número de donuts: muchos')
test(donuts(99), 'Número de donuts: muchos')

print()
print('principio_y_fin')
test(principio_y_fin('primavera'), 'prra')
test(principio_y_fin('Hola'), 'Hola')
test(principio_y_fin('Por'), 'Poor')


print()
print('cambia_segun_comienzo')
test(cambia_segun_comienzo('atalaya'), 'at*l*y*')
test(cambia_segun_comienzo('sonrisa'), 'sonri*a')
test(cambia_segun_comienzo('donut'), 'donut')

print()
print('mix_up')
test(mezcla('mesa', 'silla'), 'sisa mella')
test(mezcla('sol', 'luna'), 'lul sona')

