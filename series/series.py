def slices(series, length):
    if not 0 < length <= len(series):
        raise ValueError('length should be in (0; len(series)] range')
    result = []
    for i in range(len(series)-length+1):
        result.append(list(map(int, series[i:length+i])))
    return result
