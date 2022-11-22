money = int(input('Введите сумму вклада'))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = int(money * per_cent.get('ТКБ') / 100)
SKB = int(money * per_cent.get('СКБ') / 100)
VTB = int(money * per_cent.get('ВТБ') / 100)
SBER = int(money * per_cent.get('СБЕР') / 100)
print ('Депозит ТКБ =',TKB, 'руб.' '\nДепозит СКБ =', SKB, 'руб.' '\nДепозит ВТБ =', VTB, 'руб.' '\nДепозит СБЕР =', SBER, 'руб.')

deposit = [TKB, SKB, VTB, SBER]
deposit_max = max(deposit)
print ('Максимальная сумма, которую вы можете заработать =', deposit_max, "руб.")