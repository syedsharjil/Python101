import time
from datetime import datetime as dt
host_temp="host"
# host_path= r"C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]
while True:
    if int(dt(dt.now().year,dt.now().month,dt.now().date,8)) < dt.now() < int(dt(dt.now().year,dt.now().month,dt.now().date,16)):
       with open(host_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if (website in website_list):
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Happy Hours")
        time.sleep(5)

    