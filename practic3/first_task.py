def string_slicing():
    text = "London is the capital of Gret Britain. I want to see this city, because it will be so interesting"

    print(f"Main string (Lenght: {len(text)}):")
    print(f"'{text}'")

    required_start_index = 18
    required_step = 4

    if len(text) < required_start_index + 1:
        print("\nThe string is so short.")
        return

    sliced_result = text[required_start_index::required_step]

    print(f"Start index {required_start_index} (19 symb), step {required_step}:")
    print(f"'{sliced_result}'")

string_slicing()
