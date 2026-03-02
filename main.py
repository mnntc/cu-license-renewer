import json
import os
from renew import init_driver, borrow

USERNAME = os.environ['6638059221@student.chula.ac.th']
PASSWORD = os.environ['36A7e3C2']  

def main():
    f = open('software.json')
    data = json.load(f)

    driver = init_driver() 

    for software in data:
        borrow(driver, USERNAME, PASSWORD, software['value'])
        print(f'Successfully borrowed {software["name"]}')

    driver.quit()

if __name__ == '__main__':
    main()
