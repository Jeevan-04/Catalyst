#the main file where the code is gonna be executed.
#import all the necessary bunch of code for execution.
import threading
from song import *
from login import *

#the main first question which gonna start analyze about the user's mindset and current emotion.
def ask():
    a = (int(input("""What's your energy level like right now?
1.I'm ready to conquer the world!
2.I am not in for a pancake !!
3.I might just be in for a pancake 
""")))
    if a==1:
        from high import High_Questions
        p=High_Questions()
    elif a==2:
        from low import Low_Questions
        p=Low_Questions()
    elif a==3:
        from Moderate import Moderate_Questions
        p=Moderate_Questions()
    else:
        ask()

#Threading for te music to go on side by side alng with the flow for the mood and setting.
song_thread = threading.Thread(target=song)
ask_thread = threading.Thread(target=ask)
print()
song_thread.start()
ask_thread.start()

song_thread.join()
ask_thread.join()
