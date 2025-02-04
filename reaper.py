import webbrowser
import time

# Define the shortcut URL for the final trigger
shortcut_url = "https://drive.google.com/file/d/1xh-9rrHQrMw9lqgxbb-YDIh6hreNA31x/view?usp=sharing"


art = '''
    █    ███████ █ ███   █       █   ████    ██        
   █ ███▓          ██  █           █  ██ ██ ██         
   █  █      ██████   █  ████████   █  ░██             
   ██ ██   ██    █   █  ███████████  █   ███            
    █  ████     █     ██     ██    ██     ████         
     █  ██      █           ███       ▒   ████  █      
      █ ██     █   █ █     ██ ██     █ █   ███         
      █ ██    ██  █  █  ████   ████  █     ██          
       █ █     █  █   ███  █ █ █ ▓███   █  ████        
       █ ██   ██    ███  █████████ ████    ████        
        █ █   █  █       ████ ███   █    █  █          
        █  █ ██ ██      █ █     █ █      █  ███        
         █ █ █   █   █              █    █   ███       
         █  ██   █    █           █ █    █   ██▓       
         ██ ██   █ ▓   ██ █     █ ██   █ █   ████░     
         ████    █      █▒▓███▓█ ██      █    ██  █    
          ██ █▒   █     █ █     ███     █   ████           
'''


introduction = [
    art,
    "\n\nWelcome, insects.",
    "Through this terminal, I'll waste your time with a few games.",
    "Maybe... you'll make it out alive.",
    "If you are ready to proceed, hit [ENTER]. There's no turning back...",
]

# Define the scavenger hunt missions
missions = [
    {
        "riddle": "Echoes of cheer fill the air, ants climb these dunes as they dare, find me not and meet your despair..... What did you find?",
        "correct_answer": "scroll",
        "clue": "Good.... Here's your gift: sixTeEN.",
        "trigger": "voyager"
    },
    {
        "riddle": "I stand tall but I am not a tree, under my gaze you all may see. My arms stretch wide, embracing all, seek me out before the nightfall. What did you find?",
        "correct_answer": "statue",
        "clue": "Good.... Here's your gift: SeVenTy.",
        "trigger": "ember"
    },
    {
        "riddle": "Under the stars, where stories are told, my light glows warm, but my heart is cold. Flames dance within, shadows may play, find me quick before they fade away. What did you find?",
        "correct_answer": "lantern",
        "clue": "Good.... Here's your gift: FoRtY-Two.",
        "trigger": "revelation"
    }
]

for i in introduction:
    time.sleep(3)
    print(i)
input("")

# Start the scavenger hunt loop
for mission in missions:
    # Loop until the correct item is found
    while True:
        answer = input(mission["riddle"] + " ").strip().lower()
        if answer == mission["correct_answer"]:
            print(mission["clue"])
            print("I'll hear from you soon.")
            break
        else:
            print("Try again.")

    # Wait for the correct trigger word to proceed
    while True:
        trigger_input = input("Speak the words to continue... ").strip().lower()
        if trigger_input == mission["trigger"]:
            print("Understood. We continue...")
            break
        else:
            print("That is not the word. Try again.")

# Trigger the final video
print("You've completed all the missions. The truth awaits...")
time.sleep(3)  # Small delay for effect
print("Do you want to know what the first level of Hell looks like?")
answer = input(" ").strip().lower()
if answer.strip().lower() == "yes":
    time.sleep(2)  # Small delay for effect
    print("Let me show you...")
    time.sleep(2)  # Small delay for effect
    webbrowser.open(shortcut_url)
else:
    print("Try again.")
print("Opening the final message now...")
webbrowser.open(shortcut_url)
