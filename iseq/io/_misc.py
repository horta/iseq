def decomment(rows):
    for row in rows:
        if row.startswith("#"):
            continue
        yield row
