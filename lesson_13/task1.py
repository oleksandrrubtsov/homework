def detect_locals():
    m = 1203
    my = 'Ukraine'
    myn = {
        "Ukraine":"Kyiv",
        "England":"London",
        "Ireland":"Dublin"
    }
    local_variables = locals()
    count = len(local_variables)
    return count
result = detect_locals()
print(f"Number of local variables: {result}")