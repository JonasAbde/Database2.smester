from create import create_maling
from read import read_maling
from update import update_maling
from delete import delete_maling

def show_menu():
    print("\n1. Opret måling")
    print("2. Læs måling")
    print("3. Opdater måling")
    print("4. Slet måling")
    print("5. Forlad program (EXIT)")

def main():
    while True:
        show_menu()
        choice = input("\nVælg en handling (1-5): ")
        if choice == '1':
            create_maling()
        elif choice == '2':
            read_maling()
        elif choice == '3':
            update_maling()
        elif choice == '4':
            delete_maling()
        elif choice == '5':
            print("Farvel!")
            break
        else:
            print("Ugyldigt valg, prøv igen.")

if __name__ == "__main__":
    main()
