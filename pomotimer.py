from win10toast import ToastNotifier

def main():
    # in minutes
    time_work = 0 
    time_rest = 0
    
    print(f"Pomodoro timer started with {time_work} minutes of work time and {time_rest} minutes of rest time.")
    print("Good work and remember to concentrate!")
    
    toaster = ToastNotifier()
    toaster.show_toast("Title", "Hello, World!", duration=5)
    
if __name__ == "__main__":
    main()