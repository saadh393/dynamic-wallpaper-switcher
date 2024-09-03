import datetime


def getDateText():
    currentDate = datetime.date.today()
    formatedDate = currentDate.strftime("%d %B %Y")

    # Calculating Remaining days
    nextMonthNum = currentDate.month + 1
    if nextMonthNum > 12:
        nextMonthNum = 1

    nextYearNum = currentDate.year
    if nextMonthNum < currentDate.month:
        nextYearNum = nextYearNum + 1


    nextMonth = datetime.date(nextYearNum, nextMonthNum, 1)
    reminingDays = (nextMonth - currentDate).days
    remingStr = f"{reminingDays} Days left to Start {nextMonth.strftime('%B')}"

    return f"{formatedDate} | {remingStr}"


getDateText()