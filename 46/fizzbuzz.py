from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
        div_5 = num % 5 == 0
        div_3 = num % 3 == 0
        if div_5 and div_3:
            return "Fizz Buzz"
        elif div_3:
            return "Fizz"
        elif div_5:
            return "Buzz"
        else:
            return num

if __name__ == "__main__":
    for i in range(1, 20+1):
        print(fizzbuzz(i))