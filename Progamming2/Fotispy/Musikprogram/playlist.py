import random
from song import Song

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added {song.title} by {song.artist} to the playlist.")
        print("Current playlist:")
        for s in self.songs:
            print(f"- {s.title} by {s.artist} [{s.length}] ({s.file})")

    def remove_song(self, title):
        self.songs = [song for song in self.songs if song.title != title]
        print(f"Removed {title} from the playlist.")

    def play_all(self):
        if not self.songs:
            print("Playlist is empty. Add some songs first.")
        else:
            print("Playing all songs:")
            for song in self.songs:
                print(f"Playing {song}")
                song.play()

    def shuffle_play(self):
        if not self.songs:
            print("Playlist is empty. Add some songs first.")
        else:
            print("Playing songs in shuffle mode:")
            shuffled_songs = random.sample(self.songs, len(self.songs))
            for song in shuffled_songs:
                print(f"Playing {song}")
                song.play()

    def show_playlist(self):
        if not self.songs:
            print("Playlist is empty.")
        else:
            print("Current songs in playlist:")
            for song in self.songs:
                print(f"- {song.title} by {song.artist} [{song.length}] ({song.file})")
