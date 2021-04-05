import os
# print("Process (%s) start..." %os.getppid())
# pid=os.F_OK
# print(pid)
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


from multiprocessing import Process
def run_proc(name):
    print('Run child Process %s (%s)' %(name,os.getpid()))

if __name__ == '__main__':
    print('parent process %s.'%os.getppid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('child process end!')
