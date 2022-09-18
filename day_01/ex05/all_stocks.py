# import sys

# def clean_data(args):
#     list_of_args = args.replace(' ', '').split(',')
#     return list_of_args

# def get_key(d, value):
#     for key, val in d.items():
#         if val == value:
#             return key

# def check_list_validity(list_of_args):
#     if ' '.join(list_of_args).isspace():
#         return False
#     for arg in list_of_args:
#         if len(arg) == 0:
#             return False
#     return True

# def find_and_display_data(args):

#     COMPANIES = {
#     'Apple': 'AAPL',
#     'Microsoft': 'MSFT',
#     'Netflix': 'NFLX',
#     'Tesla': 'TSLA',
#     'Nokia': 'NOK'
#     }
#     STOCKS = {
#         'AAPL': 287.73,
#         'MSFT': 173.79,
#         'NFLX': 416.90,
#         'TSLA': 724.88,
#         'NOK': 3.37
#     }

#     list_of_args = clean_data(args)
    
#     if check_list_validity(list_of_args) == False:
#         print('\n')
#         return

#     for arg in list_of_args:
#         if arg.upper() in STOCKS:
#             print(arg.upper() + ' is a ticker symbol for ' + get_key(COMPANIES, arg.upper()))
#         elif arg.capitalize() in COMPANIES:
#             print(arg.capitalize() + ' stock price is ' + str(STOCKS[COMPANIES[arg.capitalize()]]))
#         else:
#             print(arg + ' is an unknown company or an unknown ticker symbol')


# if __name__ == '__main__':
#     if len(sys.argv) == 2:
#         find_and_display_data(sys.argv[1])

import sys

def find_element(elem):
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }
    
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }

    inv_dict = {value: key for key, value in companies.items()} # создаем инвертированый словарь
    list_of_args = sys.argv[1].replace(' ', '').split(',') # удаляем пробелы и разделяем стоку по запятой
    for arg in list_of_args:
        if not arg:
            print('')
            return # если нет слов, перевод на новую строку
    for arg in list_of_args:
        if arg.upper() in stocks:
            print("%s is a ticker symbol for %s"
                % (arg.upper(), inv_dict[arg.upper()]))
        elif arg.capitalize() in companies:
            print("%s stock price is %s"
                % (arg.capitalize(), stocks[companies[arg.capitalize()]]))
        else:
            print("%s is an unknown company or an unknown ticker symbol"
                % (arg))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_element(sys.argv[1])