# def example():
#     a = -1
#     if a < 0:
#         print(a)
#         return
# # else: geen else nodig met een return
# #     print(a+1)
#     print(a + 1)
#
# if __name__ == '__main__':
#     example()



def countdown(n):
    if n <= 0:
        print("May and William's wedding day!")
    else:
        print(n)
        countdown(n-1)

if __name__ == '__main__':
    countdown(5)


# def fac(n):
#     def go(n, a):
#         if n == 1:
#             return a
#
#         return go(n-1, a*n)
#
#     return go(n, 1)
#
# def main():
#     print(fac(5))
#
# if __name__ == '__main__':
#     main()

# from time import time
# now = int(time())
# seconds_per_day = 24 * 60 * 60
#
# offset = 2 * 60 * 60  # 2 hours in seconds
# local_now = now + offset
#
# days_since_epoch = local_now // seconds_per_day
# seconds_today = local_now % seconds_per_day
#
# hours = seconds_today // 3600
# minutes = (seconds_today % 3600) // 60
# seconds = seconds_today % 60
#
# print("Days since Jan 1, 1970:", days_since_epoch)
# print("Local time of day: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))

def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print("No")
    elif a == b + c or b == a + c or c == a + b:
        print("Degenerate triangle")
    else:
        print("Yes")

is_triangle(2, 4, 2)

