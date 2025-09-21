import time, requests, pyfiglet, threading
print(pyfiglet.figlet_format("qwe"))

msg = input("ne spamliyim: ")
webhook = input("webhook urlsi gir: ")
th = int(input('kac thread? (200 yap gec)): '))
sleep = int(input("bekleme suresi? (hizli olsun dersen 0): "))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"gonderdim: {msg}")
        except:
            print("gecersiz webhook:" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()
