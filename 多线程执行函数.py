import threading

"""
    //多线程执行函数
"""

#创建子线程
"""
    //args参数后面加元组（args，），单个参数必须要有逗号代表元组，target代表需要线程执行的目标函数
"""
thread_1 = threading.Thread(target=,args=)    

#子线程启动  
thread_1.start() 

#子线程等待主线程完成
thread_1.join()    