import simpleaudio as sa
import time
from mutagen.wave import WAVE

class Song:
    def __init__(self, title, artist, length, file):
        self.title = title
        self.artist = artist
        self.length = length  # Længde i formatet 'mm:ss'
        self.file = file
        self.play_obj = None
        self.metadata = self.get_metadata()

    def get_metadata(self):
        try:
            audio = WAVE(self.file)
            return audio.info.length  # Returnerer længden i sekunder
        except:
            return None

    def play(self):
        # Start afspilning af lydfil
        wave_obj = sa.WaveObject.from_wave_file(self.file)
        self.play_obj = wave_obj.play()
        
        # Udregn længden i sekunder
        total_seconds = int(self.metadata) if self.metadata else 0
        print(f"Playing {self.title} by {self.artist}...")

        # Tidsløb for at vise sekunderne
        start_time = time.time()
        while self.play_obj.is_playing():
            elapsed_time = int(time.time() - start_time)
            remaining_time = total_seconds - elapsed_time
            print(f"\rTime elapsed: {elapsed_time} s / {total_seconds} s", end="")
            time.sleep(1)

        # Udskriv besked, når sangen er færdig
        print("\nSong finished playing.")

    def stop(self):
        if self.play_obj:
            self.play_obj.stop()
            self.play_obj = None

    def __str__(self):
        return f"{self.title} by {self.artist} - {self.length} ({self.file})"
