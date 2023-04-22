import requests,time,argparse,sys

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

from apscheduler.schedulers.blocking import BlockingScheduler

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",

    "Referer": "http://113.106.4.60:8901/course_web/",

    "Origin": "http://113.106.4.60:8901",

}

phpsession = "0ebpsshjbrsd75glgpt6eognf2"

url = "http://113.106.4.60:8901/php_mysql/login.php"

xin_url = "http://113.106.4.60:8901/php_hudong/chat/index.php"

oj_url = "http://113.106.4.60:8901/php_run/index.php"

jifen_url = "http://113.106.4.60:8901/php_mysql/jf_show1.php?xh="

# par = argparse.ArgumentParser()

# par.add_argument('-u',type=str,default=None)

# par.add_argument('-p',type=str,default=None)

# par.add_argument('-jf',type=int,default=None)

# args = par.parse_args()

# if args.u == None:

#     print("请输入账号")

#     sys.exit(0)

# if args.p == None:

#     print("请输入密码")

#     sys.exit(0)

# if args.jf == None:

#     print("请输入学号")

#     sys.exit(0)

username = "吴开淦"

password = "1433223"

student_num = "1433223"

def read_ji():

    ji_response = requests.get(jifen_url + student_num,headers=headers)

    with open("inte.html",mode="wb") as f:

        jf_lxml = BeautifulSoup(ji_response.content,"lxml")

        rem = jf_lxml.find_all("h2",class_="text-danger")[0].contents[0].strip() #string text

        print("当前积分共"+rem+"分")

def sign():

    # path = Service('chromedriver.exe')

    op = Options()

    op.headless = False

    # 创建浏览器

    browser = webdriver.Chrome(options=op)

    browser.get(url)

    browser.maximize_window()

    # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    print("当前操作网页\t"+browser.title)

    # time.sleep(1)

    name = browser.find_element(By.ID,"name")

    name.send_keys(username)

    paw = browser.find_element(By.ID,"passwd")

    paw.send_keys(password)

    sub = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/form/input[1]")

    sub.click()

    browser.execute_script("window.open('http://113.106.4.60:8901/php_hudong/chat/index.php','_blank')")

    print("当前操作网页\t"+"讨论交流签到成功")

    browser.execute_script("window.open('http://113.106.4.60:8901/php-editor/test_index.php','_blank')")

    print("当前操作网页\t"+"oj练习签到成功",end='\n')

    time.sleep(2)

    read_ji()

    browser.close()

    browser.quit()

def func():

    # 创建调度器BlockingScheduler()

    scheduler = BlockingScheduler()

    scheduler.add_job(sign, 'interval', minutes=15, id='test_job1')

    scheduler.add_job(read_ji, 'interval', minutes=15, id='test_job2')

    scheduler.start()

if __name__ == "__main__":

    sign()

    func()
