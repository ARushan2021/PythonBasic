import threading
from time import sleep

reversed_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''
for i in  reversed_numbers:
    print(i, 'поток 1')
    sleep(1)
'''
def potok1(interval):
    while True:
        for i in reversed_numbers:
            print(i, 'поток 1')
            sleep(interval)

t = threading.Thread(target=potok1, args=(1,))
t.daemon = True
t.start()
t.join()