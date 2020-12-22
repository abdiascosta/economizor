'''This code will help users to economize money arriving daily goals'''

from tabulate import tabulate

from sty import fg, bg, rs

def choise_method():

#This function works with the method which the user choose
      print(''
            ''
            'Choise between two methods. In the method 1 you start with a steady amount for economize monthly. In the option'
            ' 2 you calculate this amount from the monthly costs.\n\n-If you wanna economize 200 of cash(for example), choise the option 1'
            '\n-If you wanna calculate the amount using your monthly costs choise the option 2. ')

      method=(input("Which method you want? 1 or 2? "))

      return method




def method_1(wage):

      saving = float(input('How much do you want to save? '))

      monthly_expense = wage - saving

      month_days = int(input('How many days is this month? '))

      return monthly_expense, month_days


def method_2(wage):

      month_days = int(input('How many days is this month?'))

      monthly_expense = 0

      monthly_expense_sum = 0

      stop_counting=False

      while stop_counting==False:

            monthly_expense_unit = input('Add a monthly expense: ')

            if monthly_expense_unit != 'end' and monthly_expense_unit != 'End' and monthly_expense_unit != 'END' and monthly_expense_unit != '':

                  monthly_expense_unit=int(monthly_expense_unit)

                  monthly_expense_sum+=monthly_expense_unit

            if monthly_expense_unit == 'end' or monthly_expense_unit == 'End' or monthly_expense_unit == 'END' or monthly_expense_unit == '':

                  stop_counting=True

                  return monthly_expense_sum, month_days





def collect_moment_spent():

      moment_spent_list_list = ''

      moment_spent_to_sum = []

      endday = False


      while endday==False:

            moment_spent_list=[]

            moment_spent=input("How much have you spent now? (Day ended: Type \"end\" if you will not spend anything else today) ")

            for i in moment_spent:

                  moment_spent_str=moment_spent+'\n'

            if moment_spent != 'end' and moment_spent != 'END' and moment_spent != "End" and moment_spent != '':

                  moment_spent_int = float(moment_spent)
                  moment_spent_to_sum.append(moment_spent_int)
                  moment_spent_list.append(moment_spent_int)
                  moment_spent_list_list+=moment_spent_str


            if moment_spent =='end' or moment_spent =='END' or moment_spent =="End" or moment_spent =='':

                  endday=True

                  return moment_spent_list_list, moment_spent_to_sum, moment_spent_str

def column_elaborator(moment_spent_list_list, moment_spent_to_sum, max_to_spend_daily, corrent_balance):

      expent_sum = sum(moment_spent_to_sum)

      daily_balance = max_to_spend_daily - expent_sum

      corrent_balance += daily_balance

      if corrent_balance > 0:
            daily_balance_string = str(corrent_balance)
            daily_balance_string = fg(34) + daily_balance_string + rs.fg

      if corrent_balance < 0:
            daily_balance_string = str(corrent_balance)
            daily_balance_string = fg(88) + daily_balance_string + rs.fg

      endday = True

      return moment_spent_list_list, expent_sum, max_to_spend_daily, daily_balance_string, corrent_balance







####################### START HERE ############################



wage = float(input('What is your wage? '))

choise=choise_method()

tablelist=[]

if choise == '1':

      method_1=method_1(wage)

      month_days=method_1[1]

      monthly_expense=method_1[0]

      day = 0

      endmonth = False

      corrent_balance = 0

      lines = ['Momentary spending ', 'Momentary spending sum', 'Max to spend daily', 'Balance']

      line_moment_spent = [lines[0]]

      line_spent_sum = [lines[1]]

      line_max_to_spend_daily = [lines[2]]

      line_balance = [lines[3]]

      while endmonth != True:

            table = []

            day += 1

            max_to_spend_daily = monthly_expense / month_days

            collect_spent = collect_moment_spent()

            daily_column = column_elaborator(collect_spent[0], collect_spent[1], max_to_spend_daily, corrent_balance)

            line_moment_spent.append(daily_column[0])

            line_spent_sum.append(daily_column[1])

            line_max_to_spend_daily.append(daily_column[2])

            line_balance.append(daily_column[3])

            corrent_balance = daily_column[4]

            table_headers = ['']

            if month_days == 31 or month_days == 30 or month_days == 29 or month_days == 28:
                  for i in range(int(month_days)):
                        if i >= 1:
                             table_headers.append('Day %d' % i)

            table_headers.append('Day %d' % month_days)

            table.append(line_moment_spent)

            table.append(line_spent_sum)

            table.append(line_max_to_spend_daily)

            table.append(line_balance)

            print(table)
            print(tabulate(table, headers=table_headers, tablefmt="grid"))
            print('')

            if day == month_days:
                 endmonth = True

if choise == '2':

      method_2=method_2(wage)

      month_days=method_2[1]

      day = 0

      endmonth = False

      corrent_balance = 0

      lines = ['Momentary spending ', 'Momentary spending sum', 'Max to spend daily', 'Balance']

      line_moment_spent = [lines[0]]

      line_spent_sum = [lines[1]]

      line_max_to_spend_daily = [lines[2]]

      line_balance = [lines[3]]

      while endmonth == False:

            table = []

            day += 1

            max_to_spend_daily=method_2[0]/month_days

            collect_spent = collect_moment_spent()

            daily_column = column_elaborator(collect_spent[0], collect_spent[1], max_to_spend_daily, corrent_balance)

            line_moment_spent.append(daily_column[0])

            line_spent_sum.append(daily_column[1])

            line_max_to_spend_daily.append(daily_column[2])

            line_balance.append(daily_column[3])

            corrent_balance = daily_column[4]

            table_headers = ['']

            if month_days == 31 or month_days == 30 or month_days == 29 or month_days == 28:
                  for i in range(month_days):
                        if i >= 1:
                             table_headers.append('Day %d' % i)

            table_headers.append('Day %d' % month_days)

            table.append(line_moment_spent)

            table.append(line_spent_sum)

            table.append(line_max_to_spend_daily)

            table.append(line_balance)

            print('')
            print(table)
            print(tabulate(table, headers=table_headers, tablefmt="grid"))
            print('')

            if day == month_days:
                 endmonth = True


