import os, time
import main
import uuid

path_to_watch = "uploads/"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])

while 1:
  time.sleep(3)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]


  if added:
      print("Added: ", ", ".join (added), '... Processing...')
      res = main.run_board(path_to_watch + added[0], "processed/processed_" + added[0])

  if removed: print("Removed: ", ", ".join (removed))
  before = after


print(res)
