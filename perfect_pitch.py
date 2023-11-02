import random
import pyaudio
import numpy as np
import time

# Define the eight notes as frequency values in Hz
C = 261.63
D = 293.66
E = 328.63
F = 349.23
G = 392.00
A = 440.00
B = 493.88
C5 = 523


# Create a list of the eight notes
notes = [C, D, E, F, G, A, B, C5]

# Define a dictionary mapping frequency values to note names
note_names = {
    261: "C",
    293: "D",
    328: "E",
    349: "F",
    392: "G",
    440: "A",
    493: "B",
    523: "C5"
}

p = pyaudio.PyAudio()
volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1.2   # in seconds, may be float

#preload audio data
note_samples = {}
for note in notes:
    frequency = int(note)
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * frequency / fs)).astype(np.float32)
    note_samples[frequency] = samples

# Play all the notes in the list
def play_notes(notes, fs, duration, volume):
    p = pyaudio.PyAudio()
    for note in notes:
        frequency = int(note)
        samples = (np.sin(2 * np.pi * np.arange(fs * duration) * frequency / fs)).astype(np.float32)
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)
        stream.write(volume * samples)
        stream.stop_stream()
        stream.close()

# function to play random note
def play_random(frequency):
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * frequency / fs)).astype(np.float32)
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)
    stream.write(volume * samples)
    stream.stop_stream()
    stream.close()

# Score counter/ streak counter

correct_count = 0
round_count = 0

print("\nThis is a pitch test\n\nAn 8 note scale will be played")
print("followed by a random note immediately after.")
print("\nMatch the last note")
print("get 3 in a row to win.")
ready = input("\n(Type tutorial for tutorial)\nReady? ").upper()

#  Tutorial
if ready == "TUTORIAL":
    tutorial = True

    while tutorial == True:

        print("\n*Welcome to the tutorial*")
        print("Listen to the scale then match the last note\n")
        print("Note bank: C D E F G A B C5\n")

        # Choose a random note from the list
        random_note = random.choice(notes)
        frequency = int(random_note)

        # Plays scale
        play_notes(notes, fs, duration, volume)

        # Play the random note
        play_random(frequency)
        guess = input("Guess the note (type exit to exit tutorial): ").upper()

        if guess == "EXIT":
            tutorial = False

        #Check if the user's guess is correct
        elif note_names[frequency] == guess.upper():
            print("Correct!\n")

        else:
            print("Incorrect. The note was", note_names[frequency],"\n")
            correct_count = 0

        input("I hope you got your practice in, ready? ")

elif ready =="YES":
    print("--> (>v<) <--")

else:
    print("no owl for you")

#Round 1 game play
start_time = int(time.time())  # get the current time in seconds

while correct_count < 3: # or can be used to add time variable
    restart = 0
    round_count += 1
    print(f"\nRound {round_count}\n")
    print("Note bank: C D E F G A B C5\n")

    # Choose a random note from the list
    random_note = random.choice(notes)
    frequency = int(random_note)

    #Plays scale
    play_notes(notes,fs,duration,volume)

    # Play the random note
    play_random(frequency)

    #Erase # for answer, testing
    #print(note_names[frequency])
    # Ask the user to guess the name of the note

    while restart == 0:
        guess = input("Guess the note, press r to replay: ").upper()
        if guess == "r".upper():
            play_notes(notes, fs, duration, volume)
            play_random(frequency)
        else:
            restart = 1

    # Check if the user's guess is correct
    if note_names[frequency] == guess.upper():
        print("Correct!\n")
        correct_count += 1
    else:
        print("Incorrect. The note was", note_names[frequency])
        correct_count = 0

# Calculate and print the total elapsed time
end_time = int(time.time())
elapsed_time = end_time - start_time
print("Total elapsed time:", elapsed_time, "seconds")
print("You Won in " + str(round_count) + " rounds\n")

times_up = 150

correct_count = 0
round_count = 0


# Round 2

print("\nRound 2\n")
print("This time you will match 2 notes")
print("Win two rounds to win the game")
input("Ready? ")

start_time = int(time.time())  # get the current time in seconds

#Start of game
while correct_count < 2:
    round_count += 1
    print(f"\nRound {round_count}\n")
    print("Note bank: C D E F G A B C5")
    restart = 0

    #Plays 8 notes
    play_notes(notes, fs, duration, volume)
    # Select first random note + assigns frequency to note
    random_note = random.choice(notes)
    frequency = int(random_note)

    # Plays first random note
    play_random(frequency)

    # Selects second random note as long as it does not equal first
    random_note2 = random.choice(notes)
    while random_note2 == random_note:  # Check if the second random note is the same as the first one
        random_note2 = random.choice(notes)
    frequency2 = int(random_note2)

    play_random(frequency2)

    # Combines the frequency of the two notes
    randomtotal = frequency + frequency2

    #Erase # to provide answers for testing
    #print(note_names[frequency])
    #print(note_names[frequency2])

    while restart == 0:
        guess_notes = input("Enter the notes separated by a space: ").upper()
        if guess_notes == "r".upper():
            play_notes(notes, fs, duration, volume)
            play_random(frequency)
            play_random(frequency2)
        else:
            split = guess_notes.split(" ", 1) #Stores split answer for processing
            restart = 1

    # Get the user's guess and convert the note names to their corresponding frequencies
    guess_freqs = [key for key, value in note_names.items() if value in split]
    guesstotal = sum(guess_freqs)

    # Check if the guess matches the randomly generated total
    if guesstotal == randomtotal:
        print("You guessed correctly!")
        correct_count += 1
    else:
        print("Incorrect, notes were " + str(note_names[frequency]) + " " + str(note_names[frequency2]))

# Calculate and print the total elapsed time
end_time = int(time.time())
elapsed_time = end_time - start_time
minutes = 0

while elapsed_time > 60:
    minutes += 1
    elapsed_time -= 60
print("Total elapsed time:", minutes, ":", elapsed_time)
print("You Won in " + str(round_count) + " rounds\n")





