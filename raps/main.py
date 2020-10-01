import time

PHONE_EMPTY = 0
PHONE_FULL  = 1

SERVER_CONNECTED    = 0
SERVER_UNCONNECTED  = 1

ERROR_NOTHING       = 0
ERROR_INITIALIZE    = 1
ERROR_SERVER        = 2
ERROR_UNKNOWN       = 3

# Initialize
phone = PHONE_EMPTY
server = SERVER_UNCONNECTED
error = ERROR_NOTHING

slot_num = 14

# Server Connection
url = '127.0.0.1'
port = 8080

def server_connect(url, port):
    result = False

    return result

server_try = 1
server_maxtry = 3
print('Connecting Server...')
while True:
    if server_connect(url, port):
        print('Server Connected!')
        server = SERVER_CONNECTED
        break
    else:
        print('Server Connection Failed. (',server_try,'/',server_maxtry,')')
        server_try += 1
        time.sleep(5)
    
    if server_try > server_maxtry:
        print('Cannot Connect to Server. Call Admin.')
        error = ERROR_SERVER
        break

# Check Server Data


# Wait
phone_owner = ''

while True:
    if error == ERROR_INITIALIZE:
        print('ERROR: Initialize Error.')
        time.sleep(60)
    elif error == ERROR_SERVER:
        print('ERROR: Server Connection Failed.')
        time.sleep(60)
    elif error == ERROR_UNKNOWN:
        print('ERROR: Unknown Error. Call Admin.')
        time.sleep(60)
    elif phone == PHONE_FULL:
        print('Now Containing Phone of ', phone_owner, '.')
        time.sleep(60)
    elif phone == PHONE_EMPTY:
        print('Now Empty.')
        time.sleep(60)
    
    # Listen to Server
    server_msg = ''

    if server_msg == 'start phone return' and phone == PHONE_EMPTY:
        # Listen Again
        server_msg = ''
        qr_string = ''
        if server_msg == 'start qr detection':
            #QR Detection
            pass
        
        # Send qr_string
        return_success = True
        if return_success:
            # Lock Door
            pass
        else:
            # Do Nothing
            pass
    if server_msg == 'start phone return' and phone == PHONE_FULL:
        # Tell Server Error Message
        pass