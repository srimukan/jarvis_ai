
import pyttsx3

# Create Jarvis voice engine
engine = pyttsx3.init()

# Set speaking speed
engine.setProperty("rate", 150)

# Set voice volume
engine.setProperty("volume", 1.0)

# Jarvis speaking function
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# Start Jarvis
print("================================")
print("       JARVIS AI")
print("================================")

speak("Hello machan!")
speak("I am Jarvis, your personal assistant.")
speak("My voice system is now activated.")


