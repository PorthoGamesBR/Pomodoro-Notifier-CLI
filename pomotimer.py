from win10toast import ToastNotifier

def main():
    toaster = ToastNotifier()
    toaster.show_toast("Title", "Hello, World!", duration=5)
    
if __name__ == "__main__":
    main()