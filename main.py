import os
import requests
import chardet

# 参数设定
username = os.environ['USERNAME']    # 获取用户名
password = os.environ['PASSWORD']    # 获取密码
web_url = os.environ['WEB_URL']      # 获取目标网站地址

login_url = web_url + '/php_mysql/login.php'   # 登录页面链接
test_url = web_url + '/php-editor/test_load_ojtimu1.php'  # 测试页面链接
chat_url = web_url + '/php_hudong/chat/index.php'         # 聊天室页面链接
explorer_url = web_url + '/explorer.php'                 # 资源管理器页面链接
logout_url = web_url + '/php_mysql/loginOut.php'         # 登出页面链接

# 登录数据
data = {
    'name': username,
    'passwd': password,
    'type': '1',
    'sub': '登陆'
}

# 发送登录请求
session = requests.Session()                                 # 创建会话对象
session.headers = {'User-Agent': 'Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0'}     # 设置会话 User-Agent
response = session.post(login_url, data=data)                # 发送 POST 请求并保持会话状态

# 获取响应内容并进行编码自动检测
content = response.content                                   # 获取响应内容
encoding = chardet.detect(content)['encoding']               # 自动检测响应内容编码方式
text = content.decode(encoding)                              # 解码响应内容

# 检查登录是否成功并获取 cookie
cookies = None                                                # 初始化 cookie
if '_登录成功！' in text:                                    # 判断是否登录成功
    print('登录成功')
    cookies = response.cookies                               # 获取 cookie
else:
    print('登录失败')
    # 结束进程或执行其他操作
    os._exit(0)

# 访问其他页面
response1 = session.get(test_url, cookies=cookies)            # 发送 GET 请求并设置 cookie
if 'action="login.php"' in response1.text:                    # 判断页面是否访问成功
    print('访问 test_url 失败，登录状态丢失')
else:
    print('访问 test_url 成功')

response2 = session.get(chat_url, cookies=cookies)            # 发送 GET 请求并设置 cookie
if 'action="login.php"' in response2.text:                    # 判断页面是否访问成功
    print('访问 chat_url 失败，登录状态丢失')
else:
    print('访问 chat_url 成功')

response3 = session.get(explorer_url, cookies=cookies)        # 发送 GET 请求并设置 cookie
if 'action="login.php"' in response3.text:                    # 判断页面是否访问成功
    print('访问 explorer_url 失败，登录状态丢失')
else:
    print('访问 explorer_url 成功')

# 发送登出请求并清除 cookie
response4 = session.get(logout_url, cookies=cookies)           # 发送 GET 请求并设置 cookie
content4 = response4.content                                  # 获取响应内容
encoding4 = chardet.detect(content4)['encoding']              # 自动检测响应内容编码方式
text4 = content4.decode(encoding4)                             # 解码响应内容

if '你已经退出系统！' in text4:                               # 判断是否登出成功
    print('登出成功')
    session.cookies.clear()                                   # 清除 cookie
else:
    print('登出失败')
    session.cookies.clear()                                   # 清除 cookie
