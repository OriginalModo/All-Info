# Современный питонист должен знать и использовать только f-strings,
# они модные, молодежные, удобные. Все старые форматы должны умереть,
# но к сожалению, выживают за счет старых туториалов и слепого копипаста новичков.
# Постоянно вижу код тех же телеграм ботов где для строк используют старый format
# ибо все копируют с какого то древнего или не очень умного видео.

a = 'Hello'
b = 'World'
import datetime

# pi = 3.141592
# result = 121
# print(f'{pi:.2f}')  # f'{pi:.2f <- сколько будет после запятой}'
# print(f'{result:06}') # запосление нулями
# print(f'{result:^12}') # заполение пробелы по центру
# print(f'{result:0^12}') # заполение нулями по центру
# print(f'{result:>12}') # заполение пробелами слева
# print(f'{result:<12}') # заполение пробелами справа

# result = 12112312
# print(f'{result:,}') # разделитель

#     today = datetime.datetime.now()
#     print(f'{today:%d-%m-%Y %H:%M}')

# # Считаем % от числа
#     real = 86 # %
#     full = 100 # от какого числа
#     print(f'{real/full:.2%}')

if __name__ == '__main__':
    result = 12112312
    real = 97.6
    full = 99
    print(f'{real/full:.2%}')