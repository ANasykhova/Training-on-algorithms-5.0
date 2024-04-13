width, first, second = map(int, input().split())
left_words = list(map(int, input().split()))
right_words = list(map(int, input().split()))


def get_len(words, w):
    lines = 0
    rem = 0
    for word in words:
        if word > w:
            return 1e9
        if word <= rem:
            rem -= word + 1
        else:
            lines += 1
            rem = w - word - 1
    return lines


def check(length):
    return get_len(left_words, length) < get_len(right_words, width - length)


left, right = 0, width
while left < right:
    middle = (left + right) // 2
    if check(middle):
        right = middle
    else:
        left = middle + 1

answer = min(max(get_len(left_words, left), get_len(right_words, width - left)),
             max(get_len(left_words, left - 1), get_len(right_words, width - left + 1)))
print(answer)
