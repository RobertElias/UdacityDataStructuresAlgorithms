def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    #Step 1: Make sure you you understand the problem
    # What are the inputs: your birthday and current date = 2 dates
    # and second date must not be before first date and check in code
    # Gregorian calendar 
    # inputs = daysBetweenDates(values)

    # Step 2: What are the outputs: calcualte your age in days.
    # Return a number giving the number of days between the first date
    # and the second date.


    #Step 3: Solve the problem
    # by working out some examples.
    # Understanidng the inputs, Understanding the outputs,
    # and understanding the relationships with the examples.

    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!

    # psuedo code
    """
    days = # of days in month1 - day1 31-24=7
    month1 +=1

    while month1 <  month2:
        days += # of days in month1
        month1 +=1
    days += day2
    while  year1 < year2
        days


    """
    
    return 0


def testDaysBetweenDates():

    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                            2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30,
                            2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30,
                            2018, 1,  1) == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                            2013, 6, 29) == 365)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


testDaysBetweenDates()
