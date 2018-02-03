def transform(legacy_data):
    new_data = {}
    for point, letters in legacy_data.items():
        new_data.update({letter.lower(): point for letter in letters})
    return new_data
