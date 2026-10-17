s = "aabbccc"

maximum = 0
answer = ""

for i in s:
    count = s.count(i)

    if count > maximum:
        maximum = count
        answer = i

print(answer)