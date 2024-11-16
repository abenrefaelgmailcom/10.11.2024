import statistics
import random

from hw1 import half_max_value


#1 filter for random numbers between 50-100

def list_x_100(x: int) -> int:
    return  x + 100

list = lambda x: x + 100

numbers: list[int] =[random.randint (1,100) for _ in range(50)]
# bigger_50: list[int] = []
# for num in numbers:
#     if num > 50:
#         bigger_50.append(num)
# def is_bigger_50(x: int) -> int:
#     # 1
#     if x > 50:
#         return True
#     else:
#         return False
#     # 2
#     return x > 50

# print(list(filter(is_bigger_50, numbers)))

'''get numbers that bigger then 50'''
print(list(filter(lambda x: x > 50, numbers)))

'''numbers that devoted by 7'''
print(list(filter(lambda x: x % 7 == 0, numbers)))

'''two digit numbers'''
print(list(filter(lambda x: 10 <= x <= 99 , numbers)))

'''two digit numbers when the unity digit equal to the tens digit '''
print(list(filter(lambda x: 10 <= x <= 99 and \
                  x % 10 == x // 10, numbers)))

'''the sum of the numbers equal to 9'''
print(list(filter(lambda x: x % 10 // 10 == 9, numbers)))

'''bigger the avg'''
avg_num = statistics.mean(numbers)
print(list(filter(lambda x: x > avg_num, numbers)))

'''numbers that are bigger then half of the max number in the list'''
half_max = max(numbers) / 2
print(list(filter(lambda x: x > half_max, numbers)))
'''bool answer'''
print(list(filter(lambda x: random.choice([True, False]),numbers)))


#2 use filter for word list
games = ["Grand Theft Auto V", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
'''print words that vahe more then 8 chars'''
print(f"bigger 8 {list(filter(lambda char: len(char) > 8, games))}")

'''only starts with F'''
print(f"only starts with F {list(filter(lambda char: char.startswith('F') , games))}")

'''games with two words title'''
print(f"games with two words title {list(filter(lambda char: len(char.split()) == 2, games))}")

'''title contain the letter v'''
print(f"title contain the letter v {list(filter(lambda char: 'V' in char.upper(), games))}")

#3 map use origin number
nums: list[int] = [random.randint(-50, 50) for _ in range(50)]
print(nums)

'''Any number to the power of 3'''
print(list(map(lambda  x: x ** 3, nums)))

'''Just the unity digit of each number.'''
print(list(map(lambda  x: abs(x) % 10, nums)))

'''Any number in Fahrenheit. That is, multiply by 9/5 and add 32'''
print(list(map(lambda  x: x * (9/5) +32, nums)))

'''* Bonus: Every positive number will become a "positive" word and any negative number will become a word-
"negative"'''
print(list(map(lambda  x: 'positive/zero' if x >= 0 else 'negative' , nums)))

#4 list as string

fruits = ["Apple", "Banana", "Orange", "Mango", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print(fruits)

'''reverse letters for every fruit'''
print(list(map(lambda fruits: fruits [::-1], fruits)))
'''first letter off every fruit'''
print(list(map(lambda fruits: fruits [0], fruits)))

'''fruit name in uppercase'''
print(list(map(lambda fruits: fruits.upper(), fruits)))

'''mid letter of every fruit'''
print(list(map(lambda fruits: fruits[len(fruits) //2], fruits)))

'''Bonus: if fruit name ends with "s" add ! else keep as is'''
print(list(map(lambda fruits: fruits + '!' if fruits[-1] == 's' else fruits, fruits)))

# 5 המילה global בפייתון מאפשרת לפונקציה לגשת ולשנות משתנה שהוגדר מחוץ
# לפונקציה (משתנה גלובלי). כלומר, כאשר משתמשים במילה global, המשתנה שייך
# למרחב הגלובלי של התוכנית, ולא למרחב הלוקלי של הפונקציה.

def print_x() -> None:
    # global x
    # x += 1
    print(x)

x: int = 10  # global x
print_x()
print(x)  # 11