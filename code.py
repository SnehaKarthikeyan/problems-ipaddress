Coding:
  
import re
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def check(Ip): 
    if(re.search(regex, Ip)): 
        print("VALID IP ADDRESS") 
    else: 
        print("INVALID IP ADDRESS") 
Ip = input()
check(Ip)
