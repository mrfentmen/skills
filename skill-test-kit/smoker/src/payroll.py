def weekly_pay(hours: float, rate: float) -> float:
    # time and a half beyond 40 hours
    if hours > 40:
        return hours * rate * 1.5
    return hours * rate
