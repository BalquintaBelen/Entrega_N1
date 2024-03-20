""" Modifique el juego para que en lugar de tener un número intentos se tenga un
número de fallos. En este caso el usuario pierde cuando el número de fallos es
alcanzado.
"""
import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
fallos = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print ("Ojo solamente contas con 10 Fallos.")

word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
i = 0
while (i < fallos) :                                                  
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()

     # punto 7 A fijarse que la el valor ingresado sea una letra
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
         print(f"Errores: {i}")
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
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