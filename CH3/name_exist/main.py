def does_name_exist(
    first_names: list[str], last_names: list[str], full_name: str
) -> bool:

    for i in first_names:
        for a in last_names:
            concatenatedFullName = i + " " + a
            if concatenatedFullName == full_name:
                return True

    return False



