def count_a_in_string(s):
    count = s.lower().count('a')
    return count

def main():
    text = input("Informe uma string: ")
    count = count_a_in_string(text)
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

if __name__ == "__main__":
    main()
