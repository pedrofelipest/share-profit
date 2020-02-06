#!/usr/bin/python
# -*- coding: utf-8 -*-

data = [7, 1, 5, 3, 6, 4, 8]
# data = [7, 6, 4, 3, 1]

lucros = [[dia2 - dia1 for dia2 in data[key:]] for key, dia1 in enumerate(data)]
dia_1 = lucros.index(max(lucros))
dia_2 = lucros[dia_1].index(max(lucros[dia_1])) + dia_1
lucro = lucros[dia_1][dia_2-dia_1]

if lucro > 0:
    print(f'Dia de compra: {dia_1 + 1}')
    print(f'Dia de venda: {dia_2 + 1}')
    print(f'Lucro: {lucro}')
else:
    print(f'Não há nenhuma operação que possa ser feita que dê lucro.')
