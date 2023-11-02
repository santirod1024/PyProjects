# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
import pyaudio
import numpy as np

# Define the eight notes as frequency values in Hz
NOTES = [261.63, 293.66, 328.63, 349.23, 392.00, 440.00, 493.88, 523.25]

p = pyaudio.PyAudio()
VOLUME = 0.5
FS = 44100
DURATION = 1.0

# Play a single note
def play_note(frequency):
    samples = (np.sin(2 * np.pi * np.arange(FS * DURATION) * frequency / FS)).astype(np.float32)
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=FS,
                    output=True)
    stream.write(VOLUME * samples)
    stream.stop_stream()
    stream.close()

# Play a list of notes
def play_notes(note_list):
    for note in note_list:
        play_note(note)

# Game loop
def play_game(correct_needed):
    correct_count = 0
    round_count = 0
    while correct_count < correct_needed:
        round_count += 1
        print(f"\nRound {round_count}\n")

        # Play the guide notes
        play_notes(NOTES)

        # Choose a random note from the list
        random_note = random.choice(NOTES)

        # Play the random note
        play_note(random_note)

        # Get the user's guess
        guess = input("Guess the note: ").upper()

        # Check if the user's guess is correct
        if guess == chr(65 + NOTES.index(random_note)):
            print("Correct!\n")
            correct_count += 1
        else:
            print("Incorrect. The note was", chr(65 + NOTES.index(random_note)))
            correct_count = 0

    print("You won in " + str(round_count) + " rounds\n")

# Round 1
print("\nMatch the last note")
print("Get 3 in a row to win")
print("Note bank: C4 D4 E4 F4 G4 A4 B4 C5\n")
input("Ready? ")
play_game(3)

# Round 2
print("\nRound 2\n")
print("This time you will match 2 notes")
print("Win two rounds to win the game")
input("Ready? ")
print("Note bank: C4 D4 E4 F4 G4 A4 B4 C5")
play_game(2)
