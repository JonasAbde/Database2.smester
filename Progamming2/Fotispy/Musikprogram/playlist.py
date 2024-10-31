import random
from song import Song

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added {song.title} to the playlist.")

    def remove_song(self, title):
        self.songs = [song for song in self.songs if song.title != title]
        print(f"Removed {title} from the playlist.")

    def play_all(self):
        print("Playing all songs:")
        for song in self.songs:
            print(f"Playing {song}")
            song.play()

    def shuffle_play(self):
        print("Playing songs in shuffle mode:")
        shuffled_songs = random.sample(self.songs, len(self.songs))
        for song in shuffled_songs:
            print(f"Playing {song}")
            song.play()
