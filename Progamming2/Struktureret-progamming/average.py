numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Definer find_average funktionen
def find_average(num):
    # Brug sum() til at finde summen og divider med længden af listen
    return sum(num) / len(num)

# Test find_average funktionen
average = find_average(numbers)
print("Average:", average)
