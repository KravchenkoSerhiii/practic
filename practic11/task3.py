import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
import string

nltk.download("gutenberg")
nltk.download("punkt")
nltk.download("stopwords")


def main():
    file_id = "chesterton-brown.txt"
    words = gutenberg.words(file_id)

    total_words_count = len(words)
    print(f"Number of words '{file_id}': {total_words_count}")

    words_lower = [w.lower() for w in words]
    counts_raw = Counter(words_lower)
    most_common_raw = counts_raw.most_common(10)

    print("\nTop 10 used words (Before cleaning):")
    for word, count in most_common_raw:
        print(f"{word}: {count}")

    plot_most_common(most_common_raw, "Top 10 used words before cleaning(Chesterton)")

    stop_words = set(stopwords.words("english"))
    punctuation = set(string.punctuation)

    filtered_words = [w for w in words_lower if w.isalpha() and w not in stop_words and w not in punctuation]

    counts_clean = Counter(filtered_words)
    most_common_clean = counts_clean.most_common(10)

    print("\nTop 10 used words (After cleaning):")
    for word, count in most_common_clean:
        print(f"{word}: {count}")

    plot_most_common(most_common_clean, "Top 10 used words after cleaning (Chesterton)")


def plot_most_common(data, title):
    words = [item[0] for item in data]
    counts = [item[1] for item in data]

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color="skyblue", edgecolor="navy")
    plt.title(title)
    plt.xlabel("Words")
    plt.ylabel("Usability")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    main()
