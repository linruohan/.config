import threading
def process_thread(name):

    def process_teacher():

    #std=local_school.teacher
        print('HELLO,%s(in %s)' % (name,threading.current_thread().name))
#local_school.teacher=name
    process_teacher()

t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
