
##登陆注册验证api
+ ### 普通用户
  + #### 登陆api
     + #####  http://www.druglover.cn/userapi/user/?action=login
         ###### *post方法 携带字段g_name或者g_email或者都写，后端提供检测账号功能;g_password* 
                 |  字段   | 含义  |
                 |  ----  | ----  |
                 | g_name  | 用户名字 |
                 | g_email  | 用户email |
                 | g_password  | 用户密码 |
  + #### 注册api
     + #####  http://www.druglover.cn/userapi/user/?action=register
          ###### *post方法 携带字段g_name;g_email;g_password;g_code;后端提供各种报错路径信息* 
                 |  字段   | 含义  |
                 |  ----  | ----  |
                 | g_name  | 用户名字 |
                 | g_email  | 用户email |
                 | g_password  | 用户密码 |
                 | g_code  | 邮箱验证码 |
  + #### 发送邮箱验证码api
     + #####  http://www.druglover.cn/userapi/code/
               ###### *post方法 携带字段g_email 
                 |  字段   | 含义  |
                 |  ----  | ----  |
                 | g_email  | 用户email |
+ ### 管理员后台用户
  + #### 登陆api
     + #####  http://www.druglover.cn/userapi/admin/?action=login
         ###### *post方法 携带字段g_name或者g_email或者都写，后端提供检测账号功能;g_password* 
                 |  字段   | 含义  |
                 |  ----  | ----  |
                 | g_name  | 用户名字 |
                 | g_email  | 用户email |
                 | g_password  | 用户密码 |
  + #### 注册api
     + #####  http://www.druglover.cn/userapi/admin/?action=21a2c3e2-a709-34b2-8ca6-a62f3b58912f
          ###### *post方法 携带字段g_name;g_email;g_password;g_code;后端提供各种报错路径信息* 
                 |  字段   | 含义  |
                 |  ----  | ----  |
                 | g_name  | 用户名字 |
                 | g_email  | 用户email |
                 | g_password  | 用户密码 |
                 | g_code  | 邮箱验证码 |
          ###### ***管理后台提供接口但是不提供页面，可以在postman中实现注册或者在登录后的管理后台注册*** 
  + #### 发送邮箱api
     + #####  http://www.druglover.cn/userapi/admincode
               ###### *post方法 携带字段g_email 
                 |  字段   | 含义  |
                 |  ----  | ----  |
                 | g_email  | 用户email |
