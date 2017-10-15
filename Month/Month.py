def numberOfDaysIn(month, leap = False):
    if leap:
        monthsDictionary = {"January" : 31, "February" : 30, "March" : 31, "April" : 30, "May" : 31, "June" : 30, "July" : 31,
                        "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December" : 31}
    else:
        monthsDictionary = {"January" : 31, "February" : 28, "March" : 31, "April" : 30, "May" : 31, "June" : 30, "July" : 31,
                        "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December" : 31}

    print(monthsDictionary.get(month))

numberOfDaysIn("September", True)
