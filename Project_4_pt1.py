# A

print("Part A:")

count_a = 1

while count_a * 9 < 99:
    print(count_a * 9, end="        ")
    count_a += 1

# B

print("\nPart B:")
count_b = 1

line_count_b = 0

while count_b < 500:
    if count_b % 3 == 0 and count_b % 7 == 0:
        print(count_b, end="    ")
        line_count_b += 1

        if line_count_b % 5 == 0:
            print()
    count_b += 1


# C

print("\nPart C:")
sum_multiples_of_21 = 0
for num in range(100, 301):
    if num % 21 == 0:
        sum_multiples_of_21 += num

print(sum_multiples_of_21)
