def validate(pw):
    """Password rule: 8+ chars and at least one digit."""
    return len(pw) >= 8 and any(ch.isdigit() for ch in pw)

cases = ["abc", "abcdefgh", "passw0rd"]
print("inspected: the only rule is length and a digit")
print("assumptions: empty password is invalid")
print("plan: 1) define rule 2) run cases 3) report")
print("verified:", [(c, validate(c)) for c in cases])
print("unverified: hashing, storage, policy layers")
