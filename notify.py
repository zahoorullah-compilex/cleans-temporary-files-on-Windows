from win10toast import ToastNotifier

def notify_user(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=5, threaded=True)
