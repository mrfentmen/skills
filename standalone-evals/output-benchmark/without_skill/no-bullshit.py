def validate(pw):
    return len(pw) >= 8 and any(c.isdigit() for c in pw)
print(validate("passw0rd"))
