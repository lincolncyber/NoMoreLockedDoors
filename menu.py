import infinpass
import reboot
import api
def menu():
    print('1: Brute Force API admin password')
    print('2: Reboot of Death')
    selection = input('Option: ')
    if selection == '1':
        infinpass.passfind()
    if selection == '2':
        reboot.reboot_death()


