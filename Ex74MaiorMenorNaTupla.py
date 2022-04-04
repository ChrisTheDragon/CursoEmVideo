from random import randint

num = tuple(randint(0, 10) for i in range(0, 5))

print(num)

print(f'O maior numero é: {max(num)}')
print(f'O menor numero é: {min(num)}')