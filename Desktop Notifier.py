from plyer import notification
import time 

if __name__ == '__main__':
    while 1:
        notification.notify(
            title = "*****  Take Rest  *****",
            message = "Rest is Vital for mental as well as physical health",
            app_icon = "E:/CODING/MyPythonProjects/rest.ico",
            timeout = 5
        )
        time.sleep(10)
