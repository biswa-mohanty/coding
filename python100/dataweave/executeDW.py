import os
import subprocess


def jsonParsing():
    os.system("dw")
    print("abc")


# print(dw "output application/xml --- users: {( 1 to 100 map (item) -> {user: 'User' ++ item} )}")
if __name__ == '__main__':
    fileName = input("What is the file name: \n")
    # subprocess.run(['dw', "output application/xml --- users: {( 1 to 100 map (item) -> {user: 'User' ++ item} )}"])
    os.system('dw -i payload ' + fileName + ' "output application/json --- payload filter (item) -> item.age > 17" > usersoutput.json')
    #os.system('dw -i payload I:\\OneDrive\\learning\\coding\\python100\\dataweave\\users.json "output application/json --- payload filter (item) -> item.age > 17"')
    #ubprocess.run(['dw -i payload I:\\OneDrive\\learning\\coding\\python100\\dataweave\\users.json',
    #                '"output application/json --- payload filter (item) -> item.age > 17"'])
    # subprocess.run(['dw -i payload I:\\OneDrive\\learning\\coding\\python100\\dataweave\\users.json "output application/json --- payload filter (item) -> item.age > 17"'])
