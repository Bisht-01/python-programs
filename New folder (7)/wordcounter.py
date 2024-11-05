def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            words = data.split()
            num_words = len(words)
            print(f"Total number of words in '{file_path}': {num_words}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

# Example usage
if __name__ == "__main__":
    file_path = "Aniketbisht.txt"  # Replace with your actual file path
    count_words_in_file(file_path)
