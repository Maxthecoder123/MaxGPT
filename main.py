import curses
import maxGPT_m1

models = ["maxGPT m1", "maxGPT m2", "maxGPT m3"]

def select_model(stdscr):
  attributes = {}
  curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
  attributes['normal'] = curses.color_pair(1)

  curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
  attributes['highlighted'] = curses.color_pair(2)

  c = 0  # last character read
  option = 0  # the current option that is marked
  while c != 10:  # Enter in ascii
    stdscr.erase()
    stdscr.addstr("Select an AI model:\n", curses.A_UNDERLINE)
    for i in range(len(models)):
      if i == option:
        attr = attributes['highlighted']
        stdscr.addstr("> ", attr)
      else:
        attr = attributes['normal']
        stdscr.addstr("  ", attr)
      stdscr.addstr(models[i] + '\n', attr)
    c = stdscr.getch()
    if c == curses.KEY_UP and option > 0:
      option -= 1
    elif c == curses.KEY_DOWN and option < len(models) - 1:
      option += 1

  return option

def main(stdscr):
  choice = select_model(stdscr)
  return choice

if __name__ == "__main__":
  try:
    choice = curses.wrapper(main)

    if choice == 0:
      maxGPT_m1.run()
    elif choice == 1:
      #maxGPT_m1.run_model_b()
      print("Model m2 is not available.")
    elif choice == 2:
      #maxGPT_m1.run_model_c()
      print("Model m3 is not available.")
    else:
      print("Invalid choice. Please select a valid option.")
  except KeyboardInterrupt:
    pass
