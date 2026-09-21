def ask_for_language_count():
    """Keep asking until the user enters a valid non-negative number."""
    while True:
        try:
            language_count = int(input("How many languages can you speak? "))
            if language_count < 0:
                print("Please enter zero or a positive number.")
                continue
            return language_count
        except ValueError:
            print("Please enter a whole number.")


def run_interaction():
    print("\nWelcome to Kika's short but simple interactive code.\n")

    while True:
        name = input("What is your name? ").strip()
        if name:
            break
        print("Please enter your name so we can get started.")

    print(f"\nHello, {name}!\n")
    language_count = ask_for_language_count()

    if language_count == 1:
        print(f"1 is more than enough, {name}!")
    elif language_count == 2:
        print(f"Very impressive, {name}!")
    elif language_count == 0:
        print(f"Everyone starts somewhere, {name}!")
    else:
        print(f"OMG! You are on fire, {name}!")

    language = input(
        "If you could learn one language, what would it be? "
    ).strip()
    if language:
        print(f"Wow, {language} is a great choice, {name}!")
    else:
        print("That is okay, you can choose one later!")


if __name__ == "__main__":
    run_interaction()
