def count_marketers(job_titles: list[str]) -> int:

    count = 0

    for i in job_titles:
        if i.lower() == "marketer":
            count += 1

    return count

