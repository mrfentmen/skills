import sys

def read_numbers():
    """Read numbers from stdin."""
    numbers = []
    for line in sys.stdin:
        numbers.extend(map(int, line.split()))
    return numbers

def calculate_sums(numbers):
    """Calculate cumulative sums."""
    sums = []
    total = 0
    for num in numbers:
        total += num
        sums.append(total)
    return sums

def generate_somonka(counts, sums):
    """Generate a two-voice somonka."""
    somonka = []
    for count, sum_ in zip(counts, sums):
        voice1 = f"{count} numbers"
        voice2 = f"sum to {sum_}"
        somonka.append(f"{voice1}\n{voice2}")
    return "\n\n".join(["\n".join([f"{count} numbers",
                                    f"counting up high",
                                    f"reaching for {count}",
                                    f"numbers all around",
                                    f"filling up the sky"]),
                         "\n".join([f"sums are my game",
                                    f"adding up fast",
                                    f"total is my aim",
                                    f"numbers all combine",
                                    f"result is my claim"])])
    # return "\n\n".join(["\n".join([f"{count} numbers",
    #                                 f"counting up high",
    #                                 f"reaching for {count}",
    #                                 f"numbers all around",
    #                                 f"filling up the sky"]),
    #                      "\n".join([f"sums are my game",
    #                                 f"adding up fast",
    #                                 f"total is my aim",
    #                                 f"numbers all combine",
    #                                 f"result is my claim"])])
    # return "\n\n".join(["\n".join([f"{count} numbers",
    #                                 f"counting up {count} high",
    #                                 f"reaching for {count} more",
    #                                 f"numbers all {count} around",
    #                                 f"filling up the {count} sky"]),
    #                      "\n".join([f"{sum_} sums",
    #                                 f"adding up {sum_} fast",
    #                                 f"total is my {sum_} aim",
    #                                 f"numbers all {sum_} combine",
    #                                 f"result is my {sum_} claim"])])
    # return "\n\n".join(["\n".join([f"{count} numbers",
    #                                 f"counting up to {count}",
    #                                 f"reaching for {count} more",
    #                                 f"numbers all around {count}",
    #                                 f"filling up the sky with {count}"]),
    #                      "\n".join([f"sums are {sum_}",
    #                                 f"adding up to {sum_}",
    #                                 f"total is {sum_}",
    #                                 f"numbers all combine to {sum_}",
    #                                 f"result is {sum_}"])])
    return "\n\n".join(["\n".join([f"{count} numbers",
                                    f"counting up to {count}",
                                    f"reaching for {count} more",
                                    f"numbers all around {count}",
                                    f"filling up the sky with {count}"]),
                         "\n".join([f"sums are {sum_}",
                                    f"adding up to {sum_}",
                                    f"total is {sum_}",
                                    f"numbers all combine to {sum_}",
                                    f"result is {sum_}")])

def main():
    numbers = read_numbers()
    counts = numbers[:5]
    sums = calculate_sums(numbers)[:5]
    somonka = generate_somonka(counts, sums)
    print(somonka)

if __name__ == "__main__":
    main()
