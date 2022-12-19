# def GreeterFun():
# 	print("Hey there!")
# 	return 'Hi there from pipeline app!'

# if __name__ == '__main__': GreeterFun()


import datetime
#Перевірити теперішню дату
current_date = datetime.date.today()
print(current_date)

# вказана теперішня дата
my_date = datetime.date(2022, 12, 19)
# визначення номеру тижня
week_number = my_date.isocalendar()[1]

# Виводить номер тижня
print(week_number)

# функція для визначення парності числа
def getParity( n ):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return parity
 
# програма для вивдення парності тижня
n = week_number
print ("Parity of the week number" , n, "from beginning of the year is",
     ( "odd" if getParity(n) else "even"))
 
def printParity():
	return "Parity of the week number from beginning of the year is even"