from speech import speech
from random import choice, randint
import time

niveles = {
    "1" : ["hello", "boys", "chair", "bottle", "reuse", "hat", "dog", "girl"],
    "2": ["schedule", "headphones", "fork", "sheet", "water", "house", "lights", "magic"],
    "3":["headlight", "accessory", "athlete", "candidate", "clothes", "deteriorate", "garbage", "language"],
    "4": ["acknowledge","architecture","mischievous","hyperbole","deforestation","greenhouse effect","awkward","characteristics"]
}

def play_game(nivel):
    word = niveles.get(nivel,[])
    print(word)
    print(nivel)
    random_word = choice(word)
    return random_word

def compara(random_word, respuesta):
    tipseco=["¿Sabias que plantar arboles produce más oxigeno, purifican el aire, forman suelos fértiles, en otras cosas? ¿Que esperas? ¡Planta el tuyo ahora! 🌳🌱", "Disminuye el tiempo de baño, el planeta te lo agradecerá. 🌊💧", "Disminuye progresivamente el uso de automóvil o sólo úsalo para recorridos largos, eso ayudará a disminuir la emision de monóxido de carbono que es el principal contaminante de la atmósfera. 🚲🌫", "Evita los plásticos de un solo uso. 🛍", "Procura no botar basura al suelo ni a las fuentes de agua 🗑", "Aprovecha la luz del día, ¡no hagas uso de la electricidad inecesariamente!🌞⚡",  "Pon tus computadora, celular y otros dispositivos electrónicos en modo ahorro. 👨‍💻🤳"]
    if random_word.lower() == respuesta.lower():
        if respuesta in ["bottle","reuse", "water", "lights", "deteriorate", "garbage", "deforestation", "greenhouse effect"]:
            return 2 , choice(tipseco)
        else:
            return 1 , None
    else:
        return 0 , None
    
def get_nivel(nivel):
    word = niveles.get(nivel,[])
    return len(word)

