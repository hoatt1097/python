from time import sleep
hello = 'Hello everybody! '
name = 'My name is Hoa'
for i in hello + name:
	print(i, end='', flush=True)
	sleep(0.1)
print()