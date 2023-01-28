from win10toast import ToastNotifier
import argparse
import time
import datetime

default_times = {'w':30,'r':15}
pomo_running = False

parser = argparse.ArgumentParser(description='This is a pomodoro timer')
parser.add_argument('-w', '--work', help='Work time', type=int, required=False)
parser.add_argument('-r', '--rest', help='Rest time', type=int, required=False)

args = parser.parse_args()

toaster = ToastNotifier()
def end_phase_notify(phase, time):
    toaster.show_toast("Pomotimer", f"{phase} time has ended. Take {time} minutes of rest!", duration=10)
    
def start_pomo(time_work, time_rest):
    print(f"Pomodoro timer started with {time_work} minutes of work time and {time_rest} minutes of rest time.")
    print("Good work and remember to concentrate!")
    print()
    
    tw = datetime.timedelta(minutes=time_work)
    tr = datetime.timedelta(minutes=time_rest)
    
    pomo_running = True
    pomo_ammount = 3
    
    while pomo_running:
        pomo_ammount-=1
        time.sleep(tw.total_seconds())
        end_phase_notify("Work",time_rest)
        time.sleep(tr.total_seconds())
        end_phase_notify("Rest",time_work)
        if pomo_ammount == 0:
            pomo_running = False
            
    print("Pomotimer ended. Thanks for your time and hope to see you soon!")
    
def main():
    # in minutes
    time_work = default_times['w'] if not args.work else args.work
    time_rest = default_times['r'] if not args.rest else args.rest
    
    start_pomo(time_work, time_rest)
    
    
if __name__ == "__main__":
    main()