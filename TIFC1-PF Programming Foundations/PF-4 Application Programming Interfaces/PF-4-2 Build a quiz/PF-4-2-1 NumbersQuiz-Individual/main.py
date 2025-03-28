import json  # Usamos json para manejar la respuesta que viene en formato JSON (como un diccionario en Python).
import requests  # requests es la herramienta que usamos para pedir datos a la API de Numbers API.

# Esta función recibe un número y trae la trivia (información curiosa) sobre ese número desde la API.
def trivia_fetch(num):
    # Aquí le pedimos a la API que nos dé la trivia para el número que el usuario haya introducido.
    response = requests.get(f"http://numbersapi.com/{num}?json")
    
    # Convertimos la respuesta en formato JSON (como un diccionario) para que podamos trabajar con ella.
    trivia = json.loads(response.content)
    
    # Devolvemos el diccionario con la trivia.
    return trivia

# Esta es la función principal donde el programa interactúa con el usuario.
def main():
    print("Hello learners!")
    
    # Usamos try/except para asegurarnos de que el usuario ingrese un número válido.
    try:
        # Pedimos al usuario que ingrese un número.
        num = int(input("Please enter a number to get trivia: "))
        
        # Llamamos a la función trivia_fetch para obtener la trivia sobre ese número.
        trivia = trivia_fetch(num)
        
        # Mostramos la trivia que obtuvimos de la API.
        print(f"Here's some trivia about the number {num}:")
        # Usamos .get() para asegurarnos de que la trivia exista y si no, mostramos un mensaje por defecto.
        print(trivia.get('text', 'No trivia found'))
    
    # Si el usuario no ingresa un número válido, mostramos un mensaje diciendo que está mal.
    except ValueError:
        print("That's not a valid number. Please try again.")

# Este código asegura que main() solo se ejecute si este archivo se corre directamente,
# no cuando se importe en otro archivo.
if __name__ == "__main__":
    main()
