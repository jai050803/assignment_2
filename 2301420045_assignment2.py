import  logging
import multiprocessing
import time

#subtask 1: Initialize the logging 
logging.basicConfig(
	filename = 'process_log.txt',
	level = logging.INFO,
	format = '%(asctime)s - %(processName)s - %(message)s'
)


#Subtask 2: Define the Dummy task

def system_process(task_name):
	logging.info(f"{task_name} started")
	time.sleep(2)
	logging.info(f"{task_name} ended")


#Subtask 3: Create two process and run them concurrently

if __name__ == '__main__':
	print("system starting")
	logging.info("System startup initiated")

	#create the processes
	p1 = multiprocessing.Process(target = system_process, args=('process-1',))
	p2 = multiprocessing.Process(target = system_process, args=('process-2',))
	
	p1.start()
	p2.start()

#subtask 4: Ensure proper termination and verify logs
	p1.join()
	p2.join()
	
	logging.info("System shutdown complete")
	print("system shutdown")



