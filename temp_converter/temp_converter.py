#!/usr/bin/python3
def f2c(f):
    return f - 32 * 5 / 9
def main(fah):
    return f2c(fah)
if __name__ == "__main__":
    fah = 100         # input
    print(main(fah))  # output
