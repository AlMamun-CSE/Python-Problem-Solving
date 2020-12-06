def count_substring(s, sb):
    results = 0
    sub_len = len(sb)
    for i in range(len(s)):
        print(s[i:i + sub_len])
        if s[i:i + sub_len] == sb:
            results += 1
    return results


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
