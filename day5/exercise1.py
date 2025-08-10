import sys

def is_palindrome(word: str) -> bool:

    trimmed = word.strip()
    lower = trimmed.lower()
    return all(lower[i] == lower[-1 - i] for i in range(len(lower) // 2))

def process_palindromes(input_path="input_words.txt", output_path="palindromes.txt"):
    try:
        with open(input_path, 'r') as infile:
            lines = infile.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Can't open '{input_path}'. File not found.", file=sys.stderr)
        return
    except IOError as e:
        print(f"Error reading '{input_path}': {e}", file=sys.stderr)
        return

    palindromes = [line.strip().upper() for line in lines if line and is_palindrome(line)]

    try:
        with open(output_path, 'w') as outfile:
            for word in palindromes:
                outfile.write(word + "\n")
    except IOError as e:
        print(f"Error writing to '{output_path}': {e}", file=sys.stderr)
        return

    print(f"OK: found and wrote {len(palindromes)} palindrome(s) to '{output_path}'.")

if __name__ == "__main__":
    process_palindromes()
