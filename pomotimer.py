from win10toast import ToastNotifier
import argparse
import time
import datetime
import threading
import sys

default_times = {'w':30,'r':15}
pomo_running = False
pomo_ammount = 0

parser = argparse.ArgumentParser(description='This is a pomodoro timer')
parser.add_argument('-w', '--work', help='Work time', type=int, required=False)
parser.add_argument('-r', '--rest', help='Rest time', type=int, required=False)

args = parser.parse_args()
    
toaster = ToastNotifier()
def end_phase_notify(phase, time):
    toaster.show_toast("Pomotimer", f"{phase} time has ended. Take {time} minutes of rest!", duration=1)
    
def start_pomo(time_work, time_rest):
    print(f"Pomodoro timer started with {time_work} minutes of work time and {time_rest} minutes of rest time.")
    print("Good work and remember to concentrate!")
    print()
    
    tw = datetime.timedelta(minutes=time_work)
    tr = datetime.timedelta(minutes=time_rest)
    
    # This supresses the error messages from windows
    sys.stderr = open("error.log", "w")
    while True:   
        time.sleep(tw.total_seconds()) 
        end_phase_notify("Work",time_rest)        
        time.sleep(tr.total_seconds())       
        end_phase_notify("Rest",time_work)        
        pomo_ammount += 1
            

def input_thread():
    while True:
        user_input = input("WRITE QUIT AND PRESS ENTER TO EXIT: ")
        if(user_input and user_input[0].lower() == 'q'):
            pomo_running = False
            print(f"Pomotimer ended. Ammount of complete pomos: {pomo_ammount} Thanks for your time and hope to see you soon!")
            break
    quit()
    
def main():
    # in minutes
    time_work = default_times['w'] if not args.work else args.work
    time_rest = default_times['r'] if not args.rest else args.rest
    
    pomo_thr = threading.Thread(target=start_pomo, args=(time_work, time_rest))
    pomo_thr.daemon = True
    pomo_thr.start()
    
    input_thr = threading.Thread(target=input_thread)
    input_thr.daemon = False
    input_thr.start()
    

    
if __name__ == "__main__":
    main()