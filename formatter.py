import json
from spellchecker import SpellChecker
from difflib import get_close_matches

def spell_checker(word, dictionary):
  spell = SpellChecker()
  spell.word_frequency.load_words(dictionary)
  corrected_word = spell.correction(word) or word
  return corrected_word

def process_input(user_input):
  response = "Sorry, I didn't understand that."
  # Load the data from maxGPT_data_m1.json
  with open('maxGPT_data_m1.json', 'r') as file:
    data = json.load(file)

  # Find the closest matching input from maxGPT_data_m1.json
  all_inputs = []
  for category in data.values():
    all_inputs.extend(category['input'])

  # Check spelling
  corrected_input = spell_checker(user_input, all_inputs)
  closest_match = get_close_matches(corrected_input, all_inputs, n=1)

  # Get the corresponding output
  if closest_match:
    for category, content in data.items():
      if closest_match[0] in content['input']:
        if 'output' in content:
          response = content['output'][0]  # You can implement a more sophisticated response selection if needed
        break

  return corrected_input, closest_match, response
