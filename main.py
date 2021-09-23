from pynput.keyboard import Key, Listener
from pygame import mixer

drum1 = Key.left  # Assign the left arrow key to a variable named drum1
drum2 = Key.right  # Assign the right arrow key to a variable named drum2

pitch_up = Key.up  # Assign the up arrow key to a variable named pitch_up

pitch = 0
mixer.init()
media = mixer.Sound("drums/startup")
media.play()


def check_key(key):
    global pitch
    if key == drum1:
        print("Drum 1 Activated")
        media = mixer.Sound(f'drums/pitches/{pitch}/tom1')
        media.play()
    elif key == drum2:
        print("Drum 2 Activated")
        media = mixer.Sound(f'drums/pitches/{pitch}/tom2')
        media.play()
    elif key == pitch_up:
        print(f"Pitch Changed")
        if pitch + 1 > 5:
            media = mixer.Sound(f'drums/{pitch}')
            media.play()
            pitch = 0
        else:
            media = mixer.Sound(f'drums/{pitch}')
            media.play()
            pitch = pitch + 1


while True:
    # Collect all event until released
    with Listener(on_press=check_key) as listener:
        listener.join()
