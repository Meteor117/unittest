import logging

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        a / b
        logging.info(f"Sucsessful divide {a} / {b}")
        return a / b
    except ZeroDivisionError as err:
        logging.error(f"На ноль делить нельзя!", exc_info=True)
        return 0


# def add(a, b):
#     return a**2 + b**2


def sqrt(a):#функция, которую добавил смежный разработчик
    return a**0.5

def pow(a, b):#функция, которую добавил смежный разработчик
    return a**b

if __name__ == '__main__':
    # print(add(100, 20))
    # print(sub(100, 20))
    # print(mul(100, 20))
    # print(div(100, 20))
    logging.basicConfig(level=logging.INFO,filemode="w", filename="py.log", format="%(asctime)s | %(levelname)s | %(message)s")
    # logging.debug("gf")
    # logging.info("j")
    # logging.warning("f")
    # logging.error("f")
    # logging.critical("a")

    print(div(3, 4))
    print(div(3, 0))
