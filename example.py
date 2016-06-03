from MapMobClient import MapMobClient

client = MapMobClient("http://mapmob.com/api");
test_email = "test12@gmail.com"
test_login = "test12"
test_pass = "123456"

if client.register(test_email, test_login, test_pass):
    print("User registered")
else:
    print("Unable to register user")
    print(client.get_latest_error())

if client.authorize(test_login, test_pass):
    print("Logged in")
else:
    print("Unable to log in")
    print(client.get_latest_error())


