import
sys
data
= sys.stdin.read()
words
= data.split()
count
= len(words)
print
(count)
print(f"tokens {count}")
print(f"total tokens {count} found")