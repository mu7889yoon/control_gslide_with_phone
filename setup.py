import os

def register_ip():
    print('Registering ip')
    print('input phone_ip >> ',end='')
    phone_ip = input()
    print('input computer_ip >> ',end='')
    computer_ip = input()
    text = 'phone_ip=\'' + str(phone_ip) +'\'\ncomputer_ip=\'' + str(computer_ip)+'\''
    with open('conf.py','a') as f:
        f.write(text)
    import conf
    print('New settings:')
    print('phone_ip    = ',conf.phone_ip)
    print('computer_ip = ',conf.computer_ip)
    print('Registering ip done. Starting server.')


def main():
    if not os.path.exists('conf.py'):
        register_ip()
    else:
        import conf
        # 現在の設定を表示
        print('Now settings:')
        print(' - phone_ip    = '+conf.phone_ip)
        print(' - computer_ip = '+conf.computer_ip)
        print('If you want to change settings, Press [Y]. Otherwise Press anykey. >> ',end='')
        flg = input()
        if flg == 'Y' or flg == 'y':
            os.remove('conf.py')
            register_ip()
        else:
            print('No change. Starting server.')
