#!/usr/bin/env python
# Date 27/04/2019
# Created by r2dr0dn

# Modules
import sys,os,re,socket
from time import sleep
try:
	import requests
except ImportError:
	print("\n[!] Error: requests module is missed Please install it use command: pip install requests")
	exit(1)
try:
	import json
except ImportError:
	print("\n[!] Error: JSON module is missed Please install it use command: pip install simplejson")
	exit(1)
os.system("clear")
####=COLORS=########
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
yellow="\033[1;36m"
Red="\033[1;31m"
purple="\033[35m"
Light="\033[95m"
cyan="\033[96m"
stong="\033[39m"
unknown="\033[38;5;82m"
unknown2="\033[38;5;198m"
unknown3="\033[38;5;208m"
unknown4="\033[38;5;167m"
unknown5="\033[38;5;91m"
unknown6="\033[38;5;210m"
unknown7="\033[38;5;165m"
unknown8="\033[38;5;49m"
unknown9="\033[38;5;160m"
unknown10="\033[38;5;51m"
unknown11="\033[38;5;13m"
unknown12="\033[38;5;162m"
unknown13="\033[38;5;203m"
unknown14="\033[38;5;113m"
unknown15="\033[38;5;14m"
####################
def cnet():
	try:
		ip =  socket.gethostbyname("www.google.com")
		con = socket.create_connection((ip,80), 2)
		return True
	except socket.error:
		pass
	return False

def getINFO(IP):
	try:
                response = requests.get("http://ip-api.com/json/"+IP).text
		labs = json.loads(response.decode("utf-8"))
		info = [
		labs['query'].encode('ascii','replace'),
		labs['status'].encode('ascii','replace'),
		labs['regionName'].encode('ascii','replace'),
		labs['country'].encode('ascii','replace'),
		labs['city'].encode('ascii','replace'),
		labs['isp'].encode('ascii','replace'),
		str(labs['lat']).encode('ascii','replace') + "," + str(labs['lon']).encode('ascii','replace'),
		labs['zip'].encode('ascii','replace'),
		labs['timezone'].encode('ascii','replace'),
		labs['as'].encode('ascii','replace')]
                sleep(0.10)
                print(Green + "\t\t IP: " +unknown+info[0])
                sleep(0.10)
                print(Green+ "\t\t Status: " +unknown+info[1])
                sleep(0.10)
                print(Green+ "\t\t Region: " +unknown+ info[2])
                sleep(0.10)
                print(Green + "\t\t Country: " +unknown+ info[3])
                sleep(0.10)
                print(Green + "\t\t City: " +unknown+ info[4])
                sleep(0.10)
                print(Green + "\t\t ISP: "+unknown + info[5])
                sleep(0.10)
                print(Green + "\t\t Lat,Lon: "+unknown+ info[6])
                sleep(0.10)
                print(Green + "\t\t ZIPCODE: "+unknown + info[7])
                sleep(0.10)
                print(Green + "\t\t TimeZone: " +unknown+ info[8])
                sleep(0.10)
                print(Green + "\t\t AS: " +unknown+ info[9])
                sleep(0.10)
	except(KeyboardInterrupt,EOFError):
                print(Red + "\n[!] Aborting ...")
                sleep(1.5)
                exit(1)
        except Exception:
                print(unknown2 + "\n[!] Something Went Wrong")
                print(unknown3+"\n["+yellow+"!"+cyan+"]"+yellow+" You Can Show The GeoIP OF Target In [ "+Green+"https://whatismyipaddress.com/ip/"+str(ip)+yellow+" ]"+cyan)
                exit(1)
def flarekiller(URL,noinfo=None):
	if cnet() !=True:
		print(unknown5 + "\n[!] No Connection Access "+unknown6+"\n Please Check your Connection!")
		exit(1)
	domain = re.sub(r'(.*://)?([^/?]+).*', '\g<2>', URL)
	try:
		fakeIP = socket.gethostbyname(domain)
	except socket.error:
		print(unknown7 + "\n[!] Error [404] Server Not Found!")
		exit(1)
	try:
		print("        "+unknown9+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
		print("        "+unknown9+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
		print("        "+unknown9+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
		print("        "+unknown9+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
		print("        "+unknown14+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
		print("        "+unknown14+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
		print("        "+unknown14+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
		print("        "+unknown14+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
		print("        "+unknown14+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
		print("        "+unknown14+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
		print("        "+unknown12+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
		print("        "+unknown12+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
		print("        "+unknown12+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
		print("        "+unknown12+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
		print("        "+unknown12+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
		print("        "+unknown12+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
		print("        "+unknown8+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
		print("        "+unknown8+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
		print("        "+unknown8+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
		print("        "+unknown8+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
		print("        "+unknown8+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
		print("        "+unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
		print("        "+unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
		print("        "+unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
		print("        "+unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
		print(unknown8+"\n["+unknown9+"~"+unknown10+"]"+unknown8+" Analysis "+unknown9+"Website[ "+unknown10+URL+unknown8+" ]"+unknown9+"..."+unknown10)
		DATA = {"cfS":domain}
		headers = {"User-agent":"FireFox"}
		data = requests.post("http://www.crimeflare.org:82/cgi-bin/cfsearch.cgi",headers=headers,data=DATA).text
		print(cyan+"======================"+"="*len(URL)+"=====")
                if "No working nameservers are registered." in data:
                        print(unknown10+"  ["+unknown11+"!"+unknown12+"]"+unknown10+" ERRORCode["+unknown11+"404"+unknown12+"]: Server Not Found!"+unknown10)
                        print(unknown13+"  ["+unknown14+"!"+unknown15+"]"+unknown+" Please Check Your URL !")
                if "these are not CloudFlare-user nameservers" in data and "No working nameservers are registered." not in data:
                        print(unknown2+"  ["+unknown3+"!"+unknown4+"]"+unknown5+" CloudFlare "+unknown6+"STATUS: "+unknown7+" Disabled"+unknown7+"!"+unknown8)
                        print(unknown8+"  ["+unknown9+"!"+unknown10+"]"+unknown11+" This Website Not Using "+unknown12+"CloudFlare"+unknown13+" Security"+unknown14+" !!!"+unknown15)
                        print(cyan+"====================================================")
                        print(Green+"["+Blue+"+"+Grey+"]"+yellow+" IP: "+Red+fakeIP+purple)
                        if noinfo==None:
                                print(Light+"["+cyan+"+"+Light+"]"+cyan+" [ GEOIP INFO ]:"+Light+"======"+cyan)
                                getINFO(fakeIP)
                if "Sorry, but the domain name must contain one or two dots." in data:
                        print(unknown+"  ["+unknown2+"!"+unknown3+"] "+unknown4+"Sorry,"+unknown5+" but the domain name must contain one or two dots."+unknown6+" !!!"+unknown7)
                if "A direct-connect IP address was found:" in data:
                        ips =  re.findall( r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",data)
                        print(unknown8+"  ["+unknown9+">"+unknown10+"]"+unknown11+" CloudFlare "+unknown12+" STATUS:"+unknown13+" Enabled"+unknown14)
                        print(cyan+"  ["+Green+">"+cyan+"]"+Green+" CloudFlare IP Is: "+cyan+fakeIP)
                        print(yellow+"  ======================"+"="*len(fakeIP))
                        print(Blue+"  ["+cyan+"+"+Blue+"]"+cyan+" Real IP Is: "+Blue+ips[0])
                        print(yellow+"  ================"+"="*len(ips[0])+cyan)
                        if noinfo==None:
                                print(Red+"  ["+cyan+"+"+Red+"]"+cyan+" [ GEOIP INFO ]:"+Red+"======"+cyan)
                                getINFO(ips[0])
                if "No direct-connect IP address was found for this domain." in data:
                        print(Grey+"  ["+yellow+"!"+Grey+"] "+yellow+"Sorry,"+cyan+" I Can't Find The Real IP Address Of This Website"+yellow+"!"+Light+" :("+cyan)
	except(KeyboardInterrupt,EOFError):
                print(unknown3+"\n["+yellow+"!"+unknown2+"]"+yellow+" Aborting"+unknown12+"..."+cyan)
                sleep(1.5)
                exit(1)
        except Exception as e:
                print(unknown15+"\n["+yellow+"!"+unknown2+"]"+yellow+" Error: "+unknown5+str(e)+cyan)
                exit(1)
def usage():
    print("        "+unknown9+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown9+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown9+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown9+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
    print("        "+unknown14+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
    print("        "+unknown14+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
    print("        "+unknown14+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
    print("        "+unknown14+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
    print("        "+unknown14+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
    print("        "+unknown14+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
    print("        "+unknown12+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
    print("        "+unknown12+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
    print("        "+unknown12+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
    print("        "+unknown12+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
    print("        "+unknown12+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
    print("        "+unknown12+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
    print("        "+unknown8+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
    print("        "+unknown8+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
    print("        "+unknown8+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
    print("        "+unknown8+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
    print("        "+unknown8+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+Blue+"                   "+unknown+"["+unknown15+"FlareKiller"+unknown+"]"+unknown+"         ")
    print("     "+purple+"             "+unknown+"["+unknown9+"  Created By r2dr0dn"+unknown+"]"+unknown+"    "+Reset+"\n")
    print(unknown2 + "Usage : \n "+unknown9+"python2 flarekiller.py <Website Url> \n "+unknown5+"Examples\n "+unknown7+"python2 flarekiller.py https://google.com \n "+cyan+"python2 flarekiller.py https://google.com noinfo")
    exit(1)
if len(sys.argv) <2:
    print(usage())

if len(sys.argv) ==2:
        URL = sys.argv[1]
        if URL in ("-h","-H","-hh","-HH","--help","--HELP","/?"):
                print(usage())
        flarekiller(URL)

if len(sys.argv) ==3:
        URL = sys.argv[1]
        if URL in ("-h","-H","-hh","-HH","--help","--HELP","/?"):
                print(usage())
        if sys.argv[2] in ("no","NO","nofo","NOINFO","noinfo","n","N"):
                flarekiller(URL,noinfo=True)
        else:
                print(Red+"\n["+yellow+"!"+Red+"]"+yellow+" Unknown Option : "+Red+sys.argv[2]+cyan)
                flarekiller(URL)
# Done
