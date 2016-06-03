MapMob Python Client
====================

Requirements
------------
The library has been tested with Python 2.7 and 3.4

Geting started
-----------
First create a client instance:

    from MapMobClient import MapMobClient

    client = MapMobClient("http://mapmob.com/api");

Registration:

	if client.register(test_email, test_login, test_pass):
	    print("User registered")
	else:
	    print("Unable to register user")
	    print(client.get_latest_error())

In the error case client.get_latest_error() will contain:
	
	{"code":400,"message":"Validation error","errors":{"username":["This username is already used."],"email":["This email is already used."]}}

Authorization:

	if client.authorize(test_login, test_pass):
	    print("Logged in")
	else:
	    print("Unable to log in")
	    print(client.get_latest_error())

In the error case client.get_latest_error() will contain:

	{"code":401,"message":"Invalid credentials for username: test12"}
