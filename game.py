import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_fails = 10
# Errores cometidos en 0
fails = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []
#Vocales
vowels = ["a","e","i","o","u","á","é","í","ó","ú"]
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Solo tienes {max_fails} vidas!")

# Menu de dificultades
menu = """ Seleccione el número de dificultad:
                1--> Facil (Vocales descubiertas)
                2--> Medio (Primer y ultima letra descubierta)
                3--> Dificil (Ninguna letra descubierta)
    """
difficulty = input(menu)

match difficulty:
    case "1":
        guessed_letters.extend(vowels)
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
    case "2":
        revelated_words = (secret_word[0],secret_word[-1])
        word_displayed= (revelated_words[0] + "_" * (len(secret_word)-2)+revelated_words[1])
    case "3":
        word_displayed = "_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while fails < max_fails:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    while letter == "":            # En caso de no insertar letra, insisto al usuario sin contarlo como intento
        letter = input("Valor inválido, por favor ingrese otro: ").lower()
  
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        if (difficulty == "1") and (letter in vowels):
            print("¡ TODAS las vocales ya estan descubiertas en esta dificultad!")    
        else:
            print("Ya has intentado con esa letra. Intenta con otra.")
        fails +=1
        print(f"¡Has perdido una vida! Te quedan {max_fails - fails} restantes.")
        continue

    # Agregar la letra a la lista de letras adivinadas

    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:   
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fails +=1
        print(f"¡Has perdido una vida! Te quedan {max_fails - fails} restantes.")

    # Mostrar la palabra parcialmente adivinada
    letters = []
    count = 0
    for i,letter in enumerate(secret_word):
        if letter in guessed_letters:
            letters.append(letter)
        elif difficulty == "2" and (i == 0 or i == (len(secret_word)-1)):  #Evaluo si estoy parado en la primera o ultima palabra, para mostrarla
            letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_fails} vidas.")
    print(f"La palabra secreta era: {secret_word}")