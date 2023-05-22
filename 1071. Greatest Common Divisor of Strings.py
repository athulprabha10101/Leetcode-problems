
def gcdOfStrings(str1, str2):
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    max_len = len(str1)
    min_len = len(str2)

    output = ""  # Initialize the variable outside the loop

    for i in range(min_len, 0, -1):
        if max_len/i == max_len//i and min_len/i == min_len//i:
            output = str2[:i]
        if output * (max_len//i) == str1 and output * (min_len//i) == str2:
            return output

    return ""
