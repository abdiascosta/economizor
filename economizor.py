import economizor_table
from datetime import date


################## TABLE OBJECT ###################

table=economizor_table.Table()

###################################################

month = 1

day = 0

current_balance = 0

wage = float(input('What is your wage? '))

method=table.choise_method(wage)

headers=table.make_headers(method[1])

while day!=int(method[1]):

        stopped_spending = False

        momentary_spend_list=[]

        while stopped_spending == False:

            momentary_spend = input("How much have you spent now? (Day ended: Type \"end\" if you will not spend anything else today) ")

            momentary_spend_list_list = table.collect_spend(momentary_spend, momentary_spend_list)

            if momentary_spend == 'end' or momentary_spend == 'END' or momentary_spend == "End" or momentary_spend == '':

                stopped_spending = True

                del momentary_spend_list_list[-1]


        table.put_in_table(momentary_spend_list_list)

        calculation_results = table.calculation(momentary_spend_list_list, method[2], current_balance)

        current_balance = calculation_results[1]

        table.print_table(headers)

        day += 1
