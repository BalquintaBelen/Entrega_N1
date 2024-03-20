""" Agregue al juego niveles de dificultad. La variación de la dificultad sería:
Fácil: En la palabra a adivinar se muestran todas las vocales por defecto.
Media: Se muestra la primer y la última letra de la palabra.
Difícil: No se muestra ninguna letra de la palabra. """

import random
import Niveles

# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo",
"inteligencia"]

vocales = ["a","e","i","o","u"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
fallos = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

print(f"Ingrese la dificultad del juego ")
print(f"1- Facil")   
print(f"2- Medio")
print(f"3- Dificil")
opcion = int(input("Ingrese la opcion: "))
if (opcion == 1):
    vocal = Niveles.NivelFacil(vocales,secret_word)
    print(f"palabra: {vocal}")
elif (opcion == 2):
    word_displayed = Niveles.NivelMedio(secret_word) 
    print(f"palabra: {word_displayed}")
elif (opcion == 3):
    word_displayed = Niveles.NivelDificil(secret_word)
    print(f"palabra: {word_displayed}")
else:
    print("Ingrese una opcion valida!.")

i = 0
while (i < fallos) :                                                     
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()

     if not letter.isalpha():
        print("Por favor, ingresa una letra válida.")
        continue

     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     # Agregar la letra a la lista de letras adivinadas                     
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         i = i +1
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         elif opcion == 1:
             if ((letter in secret_word) and (letter in vocal)): 
                 letters.append(letter)
             else: letters.append("_") 
         elif (opcion == 2):
             if ((letter in guessed_letters) or (letter == secret_word[0] or letter == secret_word[-1])):
                letters.append(letter)
             else: letters.append("_")    
         else:
             letters.append("_")           
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break

if (i == fallos):
     print(f"¡Oh no! Has agotado tus {fallos} Fallos.")
     print(f"La palabra secreta era: {secret_word}")