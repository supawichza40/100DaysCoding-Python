import json

password_storage = {
    "Facebook":{
        "email":"supa@gmail.com",
        "password":"dfaslkdfsa"
    },
    "Google":{
        "email":"supa@gmail.com",
        "password":"dfasdkfjas"
    }
}

password_storage["Twitter"] = {
    "email":"King@gmail.com",
    "password":"sdafsadf"
}
with open("password.json",mode="w") as password_writer:
    json.dump(password_storage,password_writer,indent=4)