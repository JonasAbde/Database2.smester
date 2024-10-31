from playlist import Playlist
from song import Song

def main_menu():
    playlist = Playlist()

    while True:
        print("\n1. Add song")
        print("2. Remove song")
        print("3. Play all songs")
        print("4. Shuffle play")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            length = input("Enter song length (e.g., 3:45): ")
            file = input("Enter filename (e.g., 1.wav): ")
            song = Song(title, artist, length, file)
            playlist.add_song(song)
        elif choice == "2":
            title = input("Enter song title to remove: ")
            playlist.remove_song(title)
        elif choice == "3":
            playlist.play_all()
        elif choice == "4":
            playlist.shuffle_play()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
