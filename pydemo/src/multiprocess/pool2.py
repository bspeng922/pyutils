import multiprocessing

def func(x):
    return x*x

class someClass(object):
    def __init__(self,func):
        self.f = func

    def go(self):
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        print pool.map(self.f, range(10))

if __name__ == '__main__':
    print multiprocessing.cpu_count()
    a=someClass(func)
    a.go()