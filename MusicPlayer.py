import json
import random
import time

import pygame


class MusicPlayer:
    def __init__(self):
        # read the music file
        with open("music_sheets.json") as input_file:
            sheets = json.load(input_file)

        # pick a random song
        song = random.choice(list(sheets.keys()))
        print(song)
        # list of all the keynotes
        self.keynotes = sheets[song]
        # index of current note being player
        self.current_note = 0

        # load all sound files
        self.sounds = {}
        for music_note in self.keynotes:
            note_path = f"Sounds/{music_note}.ogg"
            self.sounds[music_note] = pygame.mixer.Sound(note_path)
            self.sounds[music_note].set_volume(0.5)

    def play_notes(self):
        # get current note being player and the path to file
        music_note = self.keynotes[self.current_note]
        note_path = f"Sounds/{music_note}.ogg"
        # set volume and play sound
        self.sounds[music_note].play()
        # increment current note and wrap around the notes
        self.current_note += 1
        self.current_note = self.current_note % len(self.keynotes)
        print(note_path)


pygame.init()
mp = MusicPlayer()
while True:
    mp.play_notes()
    time.sleep(1)
