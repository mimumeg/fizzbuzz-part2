def fizzbuzz_convert(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        # 整数型から文字列型に変換
        print(str(number))


for number in range(1, 101):
    fizzbuzz_convert(number)
