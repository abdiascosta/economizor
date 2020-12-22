from datetime import date
from calendar import monthrange
from tabulate import tabulate


class Table:
    def __init__(self):
        self.lines = [['Momentary spending '], ['Momentary spending sum '], ['Max to spend daily'], ['Balance']]


    def choise_method(self, wage):  # This function works with the method which the user choose

        self.wage = wage

        print(''
              ''
              'Choise between two methods. In the method 1 you start with a steady amount for economize monthly. In the option'
              ' 2 you calculate this amount from the monthly costs.\n\n-If you wanna economize 200 of cash(for example), choise the option 1'
              '\n-If you wanna calculate the amount using your monthly costs choise the option 2. ')

        method = input("Which method you want? 1 or 2? ")

        while method != '1' and method != '2':

            method = input("Which method you want? 1 or 2? ")

        method = int(method)

        if method == 1:

            month_days = int(input('How many days is this month? '))

            saving = float(input('How much do you want to save? '))
            
            monthly_expense = wage - saving

            max_to_spend_daily = monthly_expense / month_days




            return monthly_expense, month_days, max_to_spend_daily


        if method == 2:

            month_days = int(input('How many days is this month? '))

            monthly_expense = 0

            stop_counting = False

            while stop_counting == False:

                monthly_expense_add = input('Add a monthly expense: ')

                if monthly_expense_add != 'end' and monthly_expense_add != 'End' and monthly_expense_add != 'END' and monthly_expense_add != '':

                    monthly_expense += int(monthly_expense_add)

                if monthly_expense_add == 'end' or monthly_expense_add == 'End' or monthly_expense_add == 'END' or monthly_expense_add == '':

                    stop_counting = True

                    max_to_spend_daily = monthly_expense / month_days

                    return monthly_expense, month_days, max_to_spend_daily

    def collect_spend(self, momentary_spend, momentary_spend_list):

        self.momentary_spend=momentary_spend
        momentary_spend_list.append(momentary_spend)

        return momentary_spend_list

    def put_in_table(self, momentary_spend_list_list):

        self.lines[0].append(momentary_spend_list_list)

        return self.lines

    def calculation(self, momentary_spend_list_list, max_to_spend_daily, current_balance):

        momentary_spend_list_string=momentary_spend_list_list

        momentary_spend_list_list=list(map(int, momentary_spend_list_list))

        momentary_spend_sum = sum(momentary_spend_list_list)

        self.lines[1].append(momentary_spend_sum)

        self.lines[2].append(max_to_spend_daily)

        daily_balance = max_to_spend_daily-momentary_spend_sum

        current_balance += daily_balance

        self.lines[3].append(current_balance)

        return self.lines,current_balance

    def make_headers(self, month_days):

        namecolumns = ['']

        for i in range(1, 31):
            namecolumns.append(f'Day {i}')

        self.namecolumns = namecolumns

        return namecolumns


    def print_table(self, namecolumns):
        #print(namecolumns)
        #print(self.lines)
        print(tabulate(self.lines, headers=namecolumns, tablefmt="grid"))