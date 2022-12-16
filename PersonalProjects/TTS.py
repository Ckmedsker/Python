import pyttsx3
engine = pyttsx3.init()
user_input = input("Enter in the text to be spoken to you!: ")
engine.say(user_input)
engine.runAndWait()