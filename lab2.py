import string
from collections import Counter

# Алфавіт для задачі шифру Цезаря
using_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ .,;-'")


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().replace('\r', '').replace('\n', '')


def count_chars(text):
    return dict(Counter(text))


def count_ngrams(text, n):
    return dict(Counter([text[i:i + n] for i in range(len(text) - n + 1)]))


def sort_map_by_value(map_data):
    return dict(sorted(map_data.items(), key=lambda item: -item[1]))


def sort_map_by_key(map_data):
    return dict(sorted(map_data.items()))


def caesar_cipher(text, alphabet, key):
    decoded_text = ''
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            decoded_text += alphabet[(index - key) % len(alphabet)]
        else:
            decoded_text += char
    return decoded_text


def main():
    file_content = read_file("2.txt")

    print(f"Символи (по спаданню частоти):\n")
    char_counts = count_chars(file_content)
    for key, value in sort_map_by_value(char_counts).items():
        print(f"{key}: {value}")

    print(f"\nСимволи (в алфавітному порядку):\n")
    for key, value in sort_map_by_key(char_counts).items():
        print(f"{key}: {value}")

    print(f"\nБіграми:\n")
    bigram_counts = count_ngrams(file_content, 2)
    for key, value in list(sort_map_by_value(bigram_counts).items())[:15]:
        print(f"{key}: {value}")

    print(f"\nТриграми:\n")
    trigram_counts = count_ngrams(file_content, 3)
    for key, value in list(sort_map_by_value(trigram_counts).items())[:15]:
        print(f"{key}: {value}")

    print(f"\nЧотириграми:\n")
    fourgram_counts = count_ngrams(file_content, 4)
    for key, value in list(sort_map_by_value(fourgram_counts).items())[:15]:
        print(f"{key}: {value}")

    print(f"\nАлфавіт для задачі шифру Цезаря: {using_alphabet}\n")

    decoded_caesar = caesar_cipher(file_content, using_alphabet, 8)
    print(f"Decoded Caesar Cipher Text:\n{decoded_caesar}\n")

    print(f"Символи після дешифрування (по спаданню частоти):\n")
    decoded_char_counts = count_chars(decoded_caesar)
    for key, value in sort_map_by_value(decoded_char_counts).items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
