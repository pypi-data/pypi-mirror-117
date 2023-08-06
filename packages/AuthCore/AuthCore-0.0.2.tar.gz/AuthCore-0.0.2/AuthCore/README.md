# AuthCore

The simple membership system for cross-platform application.


#### SERVER: setup a member system
```
# 啟動系統
itf = ac.SimpleMemberSystem(db_file_path="./")
```

#### APP: sign up for third-part application
```
# 註冊平台
decode_key, label = itf.signup_platform()

```


#### SERVER: signup a user
```
# 註冊會員
account = "root"
pws = "root"
itf.signup_user(account, pws)
```

#### SERVER: update info of the user
```
# update or increase info of user
data = {
            "var1": idx,
            "var2": idx,
            "var3": idx,
        }
itf.update_user(account, pws, **data)
```

#### APP: login as user
```
# the label from the step 1 (setup a member system)
# decode_key from the step 1 (setup a member system)

# user login
encode_text = itf.login_user(label, "root", "root")  

# decode the secret user info
decode_text = DecryptITF.decrypt(decode_key, encode_text) 
print(f"解析會員資料： decode_text:{decode_text}")
```

#### SERVER: Delete a user
```
# Delete a user
itf.delete_user(account, pws)
```