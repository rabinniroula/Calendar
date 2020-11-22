import math
from tabulate import tabulate

mLen = {3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31, 1:31, 2:28}

def isLeapYear(year):
    if year % 400 == 0 or year % 4 == 0:
        return True
    else:
        return False

def weekday(year, month, day, century):
    n = ((13 * month - 1) // 5 + year // 4 + century // 4 + day + year - 2 * century)
    if n > 0:
        return n % 7
    else:
        #print("neg")
        return (n + (7 * math.ceil(abs(n)/7))) % 7

def parseYear():
    print('Enter the Year and Month (separated by space) you want to see the calendar for: ', end='')
    date = list(input().strip().split(' '))

    #print(int(date[0]))

    # For leap Year
    if isLeapYear(int(date[0])):
        mLen[2] = 29

    cent = date[0][:2]
    date[0] = date[0][2:]
    date.append(cent)
    return date

def calendarMain(date):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    dateList = [[], [], [], [], []]
    d = 1

    year, month, cent = list(int(d) for d in date)
    print("\n The calendar for {} - {}: \n\n".format(year, month))
    if month <= 2:
        year -= 1
    month = month - 2 if (month > 2 and month <= 12) else month + 10
    wDay = weekday(year, month, d, cent)

    for _ in range(wDay):
        dateList[0].append('')
    for _ in range(wDay, 7):
        dateList[0].append(d)
        d = d + 1

    for i in range(1, 5):
        for _ in range(7):
            dateList[i].append(d)
            d = d + 1
            if d > mLen[month]:
                break
    print(tabulate(dateList, days, tablefmt='pretty'))
        

if __name__ == "__main__":
    while True:
        try:
            calendarMain(parseYear())
        except KeyboardInterrupt:
            exit()