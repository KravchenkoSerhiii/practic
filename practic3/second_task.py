def check_letters_presence():
    main_word = "Definistration"

    user_input = input(f"Which letters you want to find? ").strip().lower()

    main_set = set(main_word.lower())
    user_set = set(user_input)

    is_present = user_set.issubset(main_set)

    print(f"Letters in word: {sorted(list(main_set))}")
    print(f"User letters: {sorted(list(user_set))}")

    if is_present:
        print(f"\nSuccess")
    else:
        missing_letters = user_set - main_set
        print(f"\n❌ In the '{main_word}' absent letters: {sorted(list(missing_letters))}")


check_letters_presence()
