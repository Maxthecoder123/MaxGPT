import random
import time
import json
from colorama import Fore
from formatter import process_input

with open('maxGPT_data_m1.json', 'r') as file:
  maxGPT_data = json.load(file)

def clear_screen():
  print("\033[H\033[J", end="")

def typing_print(text):
  for char in text:
    print(char, end="", flush=True)
    time.sleep(random.uniform(0.005, 0.05))
  print()

def handle_message(message):
  _, closest_match, response = process_input(message)
  
  if closest_match:
    for category_name, category_data in maxGPT_data.items():
      if closest_match[0] in category_data['input'] and category_name != "farewell":
        if 'output' in category_data:
          typing_print(Fore.CYAN + random.choice(category_data['output']) + Fore.RESET)
          return True
  return False

def run():
  clear_screen()
  while True:
    message = input("Enter a message: ").lower()
    corrected_sentence, closest_match, response = process_input(message)

    if closest_match:
      message = closest_match[0]

    if handle_message(message):
      continue

    if message.isdigit():
      typing_print(Fore.CYAN + "That's a great number!" + Fore.RESET)
    elif message in maxGPT_data['clearScreen']['input']:
      clear_screen()
    elif message in maxGPT_data['time']['input']:
      typing_print(Fore.CYAN + "The time is: " + time.strftime("%I:%M %p") + Fore.RESET)
    elif message in maxGPT_data['farewell']['input']:
      typing_print(Fore.CYAN + random.choice(maxGPT_data['farewell']['output']) + Fore.RESET)
      break
    elif message:
      typing_print(Fore.CYAN + response + Fore.RESET)
      with open("messages.txt", "a") as file:
        file.write(f"{message}\n")

if __name__ == "__main__":
  run()
