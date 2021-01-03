# Python Class 2532
# Lesson 3 Problem 2
# Author: riatalwar (486154)
# Finish the go_to_next_day() method, which should increase the date by 1 day.
class Date:
    '''class to represent a date'''

    def __init__(self,month,day,year):
        '''Date(month,day,year) -> Date'''
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        '''str(Date) -> str
        returns date in readable format'''
        # list of strings for the months
        months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul',
                  'Aug','Sep','Oct','Nov','Dec']
        output = months[self.month] + ' ' # month
        output += str(self.day) + ', '  # day
        output += str(self.year)
        return output

    def go_to_next_day(self):
        '''Date.go_to_next_day()
        advances the date to the next day'''
        daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        isLeapYear = self.year % 4 == 0 and \
                     (self.year % 100 != 0 or self.year % 400 == 0)
        if isLeapYear:
            daysInMonth[2] = 29
        self.day = self.day % daysInMonth[self.month] + 1
        if self.day == 1:
            self.month = self.month % 12 + 1
            if self.month == 1:
                self.year += 1

def test():
    date1 = Date(1, 1, 1)
    date2 = Date(1, 31, 1)
    date3 = Date(2, 28, 4)
    date4 = Date(2, 28, 1)
    date5 = Date(12, 31, 1)
    for date in [date1, date2, date3, date4, date5]:
        date.go_to_next_day()
    print((date1.month, date1.day, date1.year) == (1, 2, 1))
    print((date2.month, date2.day, date2.year) == (2, 1, 1))
    print((date3.month, date3.day, date3.year) == (2, 29, 4))
    print((date4.month, date4.day, date4.year) == (3, 1, 1))
    print((date5.month, date5.day, date5.year) == (1, 1, 2))
test()
