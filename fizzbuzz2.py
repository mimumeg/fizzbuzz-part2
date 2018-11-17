def fizzbuzz_convert(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"

    if number % 5 == 0:
        return "Buzz"

    # 整数型から文字列型に変換
    return str(number)


for number in range(1, 101):
    print(fizzbuzz_convert(number))
