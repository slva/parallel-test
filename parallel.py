
from multiprocessing import Pool
import os


def do_it(p):
	print(str(p))
	print(os.getppid())
	print(os.getpid())


if __name__ == '__main__':

	l = [1,2,3,4,5]

	pool = Pool()
	pool.map(do_it, l)
	pool.close()
	pool.join()