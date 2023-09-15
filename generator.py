import random

# Step 1: Take input for 'n' or specify it
n = int(input("Enter the value of 'n': "))

# Step 2: Generate random preference lists
def generate_preference_lists(n):
    men_preferences = {}
    women_preferences = {}

    for i in range(n):
        man = f'Man {i + 1}'
        woman = f'Woman {i + 1}'

        # Generate random preference orders
        man_preferences = random.sample(range(1, n + 1), n)
        woman_preferences = random.sample(range(1, n + 1), n)

        men_preferences[man] = woman_preferences
        women_preferences[woman] = man_preferences

    return men_preferences, women_preferences

men_preferences, women_preferences = generate_preference_lists(n)

# Step 3: Write data to an output file
output_filename = f'n{n}_men_women_problem.txt'

with open(output_filename, 'w') as file:
    file.write(f"{n}\n")

    for man, preferences in men_preferences.items():
        file.write(f"{man} {' '.join(map(str, preferences))}\n")

    for woman, preferences in women_preferences.items():
        file.write(f"{woman} {' '.join(map(str, preferences))}\n")

print(f"Data for {n}-men-{n}-women problem has been written to {output_filename}.")