'''
	a = 'Name:{a},Address:{b},Phone:{c}'.format(a='thienhoa',b='quan 9',c='0165422')
	print(a)

	a='Name{:*<30}'.format('thienhoa')
	print(a)
'''
# chuỗi trong python

row_1 = '+ {:-<6} + {:-<15} + {:-<10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va Ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('15520', 'Tran Thien Hoa', 'Binh Dinh')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('1542', 'Obama', 'American')
row_5 = '+ {:-<6} + {:-<15} + {:-<10} +'.format('', '', '')
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)

# srt in python

a = 'thienhoa-Hello Everyone thiện'
b = a.encode()
print(a)
print(b)
print(type(a))

list = [i for i in range(30)]
print(list)