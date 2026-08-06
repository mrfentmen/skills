def is_valid_email(email: str) -> bool:
    # naive: anything containing @ looks valid
    return "@" in email
