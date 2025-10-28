"""
   CONSIGNA:
   El juego termina cuando el jugador acierta el numero o hace 5 intentos
   Cuando se pide ingresar el num se le debe indicar al jugado el rango maximo y minimo
   -si el jugador falla, se debe indicar si el num es mayor o menor
   al perder se le enviara un mensaje indicandole que ha perdido y cual era el numero
    Debe indicar si el nro ingresado es MAYOR o MENOR
    Si ingresa algo que no es un nro debe indicar error

  import random
  numero_secreto = random.randint(1,50)

  Mails del equipo:
       mandreamarcos@hotmail.com
       alexisjklm111@gmail.com
       gutierrezleoneltomas@gmail.com
       gustavocamussi@yahoo.com.ar
"""

import random
numero_secreto = random.randint(1,50)
#print(f'numero secreto: {numero_secreto}')
intento = 5
adivino = False

print(' ')
print('***********************************************')
print('TIENE 5 INTENTOS DE ADIVINAR UN NUMERO SECRETO!')
print('***********************************************')
print(' ')

while  intento > 0 and adivino == False:
    numero_ingresado = int(input('Ingrese un Nro del 1 al 50: '))
    if numero_secreto == numero_ingresado:
        print(' ')
        print('**************************************')
        print(f'Usted adivinó el NÚMERO SECRETO!!!!!')
        print('**************************************')
        adivino = True
        break
    elif  numero_secreto < numero_ingresado:
        print('El número secreto es MENOR al número ingresado')
    else: 
        print('El número secreto es MAYOR al número ingresado')
    
    intento = intento - 1

if adivino == False:
     print(' ')
     print(f'*** Usted perdió, el número secreto es: {numero_secreto} ***')
     print(' ')
        
"""
-- Por falta de tiempo nos falto:
      -- poner si esta fuera de rango
      -- Si es no es un número
"""