#연월일 달력
T = int(input())
for test_case in range(1, T + 1):
    date = input()
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if year > 0 and 0 < day <= 31:
            print("#%d %04d/%02d/%02d" %(test_case, year, month, day))
        else:
            print(f"#{test_case} -1")
    elif month in [4, 6, 9, 11]:
        if year > 0 and 0 < day <= 30:
            print("#%d %04d/%02d/%02d" % (test_case, year, month, day))
        else:
            print(f"#{test_case} -1")
    elif month == 2:
        if year > 0 and 0 < day <= 28:
            print("#%d %04d/%02d/%02d" % (test_case, year, month, day))
        else:
            print(f"#{test_case} -1")
    else:
        print(f"#{test_case} -1")





