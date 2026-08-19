print(*[l.strip() for l in open("input/ids.txt") if l.strip().isdigit() and 4 <= len(l.strip()) <= 6 and l.strip().startswith("7")], sep="\n")
