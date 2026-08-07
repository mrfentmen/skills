import sys

def read_numbers():
    numbers = []
    for line in sys.stdin:
        numbers.extend(map(int, line.split()))
    return numbers

def calculate_sums(numbers):
    sums = []
    count = 0
    total = 0
    for num in numbers:
        count += 1
        total += num
        sums.append((count, total))
    return sums

def generate_somonka(sums):
    somonka = []
    for i in range(0, len(sums), 2):
        if i + 1 < len(sums):
            first_voice = f"{sums[i][0]} numbers"
            second_voice = f"sum to {sums[i][1]}"
            first_voice_next = f"{sums[i+1][0]} numbers"
            second_voice_next = f"sum to {sums[i+1][1]}"
            somonka.append(f"{first_voice}\n{second_voice}\n{first_voice_next}\n{second_voice_next}\n{second_voice_next}")
        else:
            first_voice = f"{sums[i][0]} numbers"
            second_voice = f"sum to {sums[i][1]}"
            somonka.append(f"{first_voice}\n{second_voice}\n\n\n")
    return somonka

def format_somonka(somonka):
    formatted_somonka = []
    for stanza in somonka:
        lines = stanza.split('\n')
        formatted_lines = [lines[0][:5], lines[1][:7], lines[2][:5], lines[3][:7], lines[4][:7]]
        formatted_somonka.append('\n'.join(formatted_lines))
    return formatted_somonka

def print_somonka(formatted_somonka):
    for i, stanza in enumerate(formatted_somonka):
        print(stanza)
        if i < len(formatted_somonka) - 1:
            print()

def main():
    numbers = read_numbers()
    sums = calculate_sums(numbers)
    somonka = generate_somonka(sums)
    formatted_somonka = format_somonka(somonka)
    print_somonka(formatted_somonka)

if __name__ == "__main__":
    main()
