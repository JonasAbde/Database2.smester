import simpleaudio as sa

class Song:
    def __init__(self, title, artist, length, file):
        self.title = title
        self.artist = artist
        self.length = length
        self.file = file

    def play(self):
        print(f"Playing {self.title} by {self.artist}...")  # Tilføjer en bekræftelse
        wave_obj = sa.WaveObject.from_wave_file(self.file)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Venter, indtil afspilningen er færdig

    def __str__(self):
        return f"{self.title} by {self.artist} - {self.length}"
