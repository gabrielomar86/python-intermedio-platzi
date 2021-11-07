from os import system, name
import time
import pyfiglet
import random
import unicodedata

'''
  Funciones para graficar partes de Arrow Man
'''

HEAD = [
  "  -----",
  " /     \\",
  "| - | - |",
  " \\ ___ /",
  "  -----"
]

def draw_line(vertical_position, horizontal_position, value):
  return print("\033[{};{}H{}".format(vertical_position, horizontal_position, value))

def draw_head(horizontal_position):
  vertical_position = 6
  for line in HEAD:
    draw_line(vertical_position, horizontal_position, line)
    vertical_position += 1

def draw_body(horizontal_position):
  for x in range(11, 16):
    draw_line(x, horizontal_position, "    |")

def draw_right_hand(horizontal_position):
  draw_line(11, horizontal_position, "    |     /")
  draw_line(12, horizontal_position, "    |----/")

def draw_left_hand(horizontal_position):
  draw_line(11, horizontal_position, "\     |")
  draw_line(12, horizontal_position, " \----|")

def draw_right_foot(horizontal_position):
  draw_line(16, horizontal_position, "     \\")
  draw_line(17, horizontal_position, "      \\/")

def draw_left_foot(horizontal_position):
  draw_line(16, horizontal_position, "     /")
  draw_line(17, horizontal_position, "   \\/")

def draw_pallet(horizontal_position):
  for x in range(18, 20):
    draw_line(x, horizontal_position, "="*35)

def draw_arrow(horizontal_position, avance = 0):
  draw_line(7, horizontal_position, " "*avance+">>----------->")

def draw_arrow_man(part_number):
  for x in range(1, part_number + 1):
    if (x == 1):
      draw_pallet(17)
    elif (x == 2):
      draw_head(30)
    elif (x == 3):
      draw_body(30)
    elif (x == 4):
      draw_right_hand(30)
    elif (x == 5):
      draw_left_hand(28)
    elif (x == 6):
      draw_right_foot(30)
    elif (x == 7):
      draw_left_foot(28)
    elif (x == 8):
      draw_arrow(10)
    elif (x > 8):
      draw_arrow(10, 17)
      raise Exception("Juego Terminado...!")
    time.sleep(0.1)

'''
  Funciones Generales
'''
def clear_screen():
  # for windows
  if name == 'nt':
    _ = system('cls')

  # for linux
  else:
    _ = system('clear')

def verify_letter(letter, word):
  return letter in word

def draw_word_mask(word, matched_letter):
  word_list = list(map(lambda letter: letter if verify_letter(letter, matched_letter) else '_', word))

  for index,value in enumerate(word_list):
    draw_line(25, 20+(index+1)*3, value)

  return list(word) == word_list

def print_banner(vertical_position, horizontal_position, mensaje):
  ascii_banner = pyfiglet.figlet_format(mensaje)
  draw_line(vertical_position, horizontal_position, ascii_banner)

def play_arrow_man(word):
  matched_letter = []
  error_number = 0

  try:

    while(True):
      clear_screen()
      print_banner(0, 0, "ARROW-MAN")
      
      if (draw_word_mask(word, matched_letter)):
        print_banner(27, 0, "GANASTE GUAMBRA.....! ")
        break

      draw_arrow_man(error_number)

      letter_input = input("\033[23;%dH"%23+"Ingrese una letra:")
      
      if verify_letter(letter_input.lower(), word):
        matched_letter.append(letter_input.lower()) 
      else: 
        error_number += 1

  except Exception as ex:
    print_banner(27, 0, "PERDISTE GUAMBRA.....! ")

def get_random_word():
  DATA = []
  word = ""
  with open("./data.txt", "r", encoding='utf8') as f:
    for line in f:
      text = unicodedata.normalize('NFD', line.replace("\n", ""))
      text = text.encode('ascii', 'ignore')
      text = text.decode("utf-8")    
      DATA.append(text)
    word = random.choice(DATA)

  return word

def run():
  word = get_random_word()
  play_arrow_man(word)
  print("\n"*12)

if __name__ == '__main__':
    run()