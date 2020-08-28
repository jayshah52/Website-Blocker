import time
from datetime import datetime as dt
host_temp = r"C:\Users\Jay Shah\Desktop\python\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,6) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Office Hours!")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " + website+ "\n")

    else:
        print("Office Closed! ")
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)  #place the pointer to the first character so it starts appending from there.
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
                file.truncate()  # Delete everything after this.


    time.sleep(5)
