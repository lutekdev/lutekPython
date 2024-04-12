count1 = 0

for count1 in range(1, 11):
    print(count1)
    if (count1 == 5):
        print("Parei no 5...")
        break

    count2 = 0

for count2 in range(1, 11):
    if count2 == 5:
        # print("Continua no 5...")
        continue
    print(count2)
