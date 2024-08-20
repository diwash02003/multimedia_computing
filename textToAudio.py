import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties before adding anything to speak
engine.setProperty('rate', 150)   
engine.setProperty('volume', 0.9) 

# Text to be spoken
text = "Hello, I am Diwash pokhrel ."

# Queue the text
engine.say(text)

# Block while processing all the currently queued commands
engine.runAndWait()
