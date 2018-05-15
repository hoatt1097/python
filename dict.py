dict = {'thienhoa':'Tran Thien Hoa', 12:'muoi hai'}
print(dict)
get = dict.get('abc',('Key khong co %d trong Dict','abc'))
print(get)

getValue = dict.update(abc='meo co gi')
print(dict)