def last_work_experience(work_experiences: list[str]) -> str | None:
    listLength = len(work_experiences)
    if(listLength < 1): return None
    return work_experiences[listLength -1]

