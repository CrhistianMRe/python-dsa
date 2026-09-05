def backoff_delays(base: int):
    delay = base

    while True:
        yield delay
        delay = delay * 2

