voc = set(input().split())
text = input().split()

for i in range(len(text)):
    for j in range(1, min(101, len(text[i]))):
        part = text[i][:j]
        if part in voc:
            text[i] = part
            break

print(' '.join(text))
