import sys
import json
import datetime

# URL lib parts
from urllib.request import Request, urlopen
from urllib.parse   import urlencode
def main():
    # Check the CLI arguments
    if len(sys.argv)<5 :
        print("Usage: python3 %s <url> <username> <password> <role>"%sys.argv[0])
        return
    
    # Prep the arguments blob
    args = dict()
    args['username']  = sys.argv[2]
    args['password']  = sys.argv[3]
    if sys.argv[4] == 'facofc':
        args['role'] = 'Facilities Officer'
    elif sys.argv[4] == 'logofc':
        args['role'] = 'Logistics Officer'
     # Print a message to let the user know what is being tried
    print("Activating user: %s"%args['username'])

    # Setup the data to send
    data = urlencode(args)
    
    # Make the resquest
    location = sys.argv[1] + 'activate_user'
    req = Request(location, data.encode('ascii'), method='POST')
    
    res = urlopen(req)
    
    # Parse the response
    resp = json.loads(res.read().decode('ascii'))
    
    # Print the result code
    print("Call to LOST returned: %s"%resp['result'])

if __name__=='__main__':
    main()
