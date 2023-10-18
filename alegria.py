import winsound
import time

# Definir las notas y duraciones
melody = [
    ("E5", 800),
    ("E5", 800),
    ("F5", 800),
    ("G5", 800),
    ("G5", 800),
    ("F5", 800),
    ("E5", 800),
    ("D5", 800),
    ("C5", 800),
    ("C5", 800),
    ("D5", 800),
    ("E5", 800),
    ("E5", 800),
    ("D5", 800),
    ("D5", 800),
    ("E5", 800),
    ("E5", 800),
    ("F5", 800),
    ("G5", 800),
    ("G5", 800),
    ("F5", 800),
    ("E5", 800),
    ("D5", 800),
    ("C5", 800),
    ("C5", 800),
    ("D5", 800),
    ("E5", 800),
    ("E5", 800),
    ("D5", 800),
    ("D5", 800),
]

# Función para reproducir la melodía
def play_melody():
    for note, duration in melody:
        frequency = 440 * 2 ** ((ord(note[0]) - ord('A')) / 12.0)
        winsound.Beep(int(frequency), duration)
        time.sleep(0.4)  # Pequeño descanso entre notas

# Llamar a la función para reproducir la melodía
play_melody()
