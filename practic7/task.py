import string
import os


def create_first_file(filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            print(f"Creating file {filename}. Type strings (empty string for finishing):")
            while True:
                line = input("> ")
                if not line:
                    break
                f.write(line + '\n')
        print(f"File {filename} created.")
    except IOError as e:
        print(f"Error with creating the file: {e}")


def process_files(source_file, target_file):
    vowels = "аеєиіїоуюяaeiouy"

    try:
        with open(source_file, "r", encoding="utf-8") as src, \
                open(target_file, "w", encoding="utf-8") as tgt:

            for line in src:
                translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
                clean_line = line.translate(translator)

                words = clean_line.split()
                for word in words:
                    if word[0].lower() in vowels:
                        tgt.write(word + '\n')

        print(f"Everything ok. Target file: {target_file}.")
    except FileNotFoundError:
        print(f"File {source_file} doesn't exist.")
    except IOError as e:
        print(f"Something went wrong: {e}")


def print_file_content(filename):
    try:
        if not os.path.exists(filename):
            print(f"File {filename} not created.")
            return

        print(f"\n!{filename}!")
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())
        print("-!Finish!")
    except IOError as e:
        print(f"Something went wrong: {e}")


def main():
    f1 = "TF13_1.txt"
    f2 = "TF13_2.txt"

    create_first_file(f1)

    process_files(f1, f2)

    print_file_content(f2)


if __name__ == "__main__":
    main()
