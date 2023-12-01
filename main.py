per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую планируете положить под проценты:"))
per_cent_values = per_cent.values()
deposit = round(max(list(map(lambda x: x * money * 0.01, per_cent_values))))
deposit_print = "Максимальная сумма, которую вы можете заработать — " + str(deposit)
print(deposit_print)