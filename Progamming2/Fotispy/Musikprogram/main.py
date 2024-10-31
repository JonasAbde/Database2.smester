import os
import shutil
from playlist import Playlist
from song import Song

def ensure_file_in_folder(file):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    destination = os.path.join(current_folder, os.path.basename(file))

    if not os.path.exists(destination):
        try:
            shutil.copy(file, destination)
            print(f"Copied {file} to project folder.")
        except FileNotFoundError:
            print(f"File {file} not found. Please check the path.")
            return None
    return destination

def main_menu():
    playlist = Playlist()
    playlist.load_playlist()  # Indlæs gemt playliste, hvis tilgængelig

    while True:
        print("\n1. Add song")
        print("2. Remove song")
        print("3. Play all songs")
        print("4. Shuffle play")
        print("5. Show playlist")
        print("6. Save playlist")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            length = input("Enter song length (e.g., 3:45): ")
            file = input("Enter filename with path if outside folder (e.g., C:/path/to/1.wav): ")
            
            file_path = ensure_file_in_folder(file)
            if file_path:
                song = Song(title, artist, length, file_path)
                playlist.add_song(song)
        elif choice == "2":
            title = input("Enter song title to remove: ")
            playlist.remove_song(title)
        elif choice == "3":
            playlist.play_all()
        elif choice == "4":
            playlist.shuffle_play()
        elif choice == "5":
            playlist.show_playlist()
        elif choice == "6":
            playlist.save_playlist()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
