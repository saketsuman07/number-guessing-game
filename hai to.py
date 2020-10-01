import random
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spvoice")
    speak.Speak(str)


if __name__ == '__main__':

    speak("this is a number gussing game made by Mr saket suman in python programming")

print("number gussing game chaliye suru karte hai")
speak("number gussing game chaliye suru karte hai")
number=random.randint(1,19)
chance=0
print("guess the number between 1 to 19")
speak("guess the number between 1 to 19")
while chance<5:
    guess=int(input())
    speak(guess)
    if guess==number:
        print("you won")
        speak("you won")
        break
    elif guess<number:
        print("you guess too low: guess higher no than",guess)

        speak("you guess too low: guess higher no than that")

    else:
        print("you guess too high:guess a number lower than",guess)
        speak("you guess too high:guess a number lower than that")
    chance +=1
    if not chance<5:
        print("you lose the number is",number)
        speak("you lose the answer is 1")
        speak(number)
