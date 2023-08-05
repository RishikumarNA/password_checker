import requests
import hashlib
import sys

def request_to_api(query_code):
    url= "https://api.pwnedpasswords.com/range/"+query_code
    res=requests.get(url)
    if res.status_code != 200:
        raise RuntimeError("Error in the code. Check the response from api"+res.status_code)
    return res

def get_password_leak_count(hashes,hash_to_check):
    hashes=(line.split(":") for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_to_check:
            return count
    return 0


def pwned_password_check(password):
    sha1password= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5, remain=sha1password[:5],sha1password[5:]
    response= request_to_api(first_5)
    return get_password_leak_count(response,remain)

#def main(args):
 #   for password in args:
  #      count = pwned_password_check(password)
   #     if count:
    #        print("your password is already been hacked for " + count+ " many times.please don't use this ")
     #      print("your password is secured. you can use this")

    #return "done!!!"

if __name__ == '__main__':
    #sys.exit(main(sys.argv[1:]))
    
    password = input("Please Enter your password to check : ")
    count = pwned_password_check(password)
    if count:
        print("your password is already been hacked  " + count+ " times.please don't use this. Try with another password ")
    else:
        print("your password is secured. you can use this")
    
    print("done!!!")

  