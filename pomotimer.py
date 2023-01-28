from win10toast import ToastNotifier
import argparse

default_times = {'w':30,'r':15}

parser = argparse.ArgumentParser(description='This is a pomodoro timer')
parser.add_argument('-w', '--work', help='Work time', type=int, required=False)
parser.add_argument('-r', '--rest', help='Rest time', type=int, required=False)

args = parser.parse_args()

def main():
    # in minutes
    time_work = default_times['w'] if not args.work else args.work
    time_rest = default_times['r'] if not args.rest else args.rest
    
    print(f"Pomodoro timer started with {time_work} minutes of work time and {time_rest} minutes of rest time.")
    print("Good work and remember to concentrate!")
    print()
    
    toaster = ToastNotifier()
    toaster.show_toast("Title", "Hello, World!", duration=2)
    
if __name__ == "__main__":
    main()