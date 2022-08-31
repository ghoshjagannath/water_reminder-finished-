from plyer import notification
import time
import tqdm


#in this project you are asked how many time you need to remind and for houw much hour . 
#that is very simple project and complete it as fast as possible . 

def reminder():
    count=0
    while True:
        notification.notify(title = 'Health',message = 'Drink water',app_icon = None,timeout = 10)
        count+=1
        for i in tqdm.tqdm(range(int(60))):
            time.sleep(1)
        if count>4:
            break
        else:
            pass


if __name__=="__main__":
    reminder()