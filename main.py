import subprocess
import os
sys = 'System: '

def talkMe():
    inp = subprocess.getoutput("termux-speech-to-text")
    output = str(inp)
    if(output):
    	print("You said: "+str(inp))
    else:
    	print("Your last command couldn\'t be heard")
    return output

def utkvs(output):
    if 'hi' in output:
    	print(sys + 'Hello!')
    	os.system('termux-tts-speak Hello!')
    elif 'hello' in output:
    	os.system('termux-tts-speak Hello!')
    	print(sys + 'Hello!') 
    elif 'hai' in output:
    	os.system('termux-tts-speak Hello!')
    	print(sys + 'Hello!') 
    elif 'exit' in output:
        print('Exited') 
        os.system('termux-tts-speak Exited') 
        os._exit(os.EX_OK)
    elif 'discord' in output:
        os.system('am start --user 0 -n com.discord/com.discord.app.AppActivity$AppAction')
        os.system('termux-tts-speak Opened discord') 
        print('Opened discord') 
    elif 'favorite' in output:
        os.system('am start com.discord/com.discord.app.AppActivity$Main')
        print('Opened discord') 
    elif 'Chrome' in output:
        os.system('am start --user 0 -n com.android.chrome/com.google.android.apps.chrome.Main')
        os.system('termux-tts-speak Opened chrome') 
        print('Opened chrome')
    elif 'vps' in output:
        os.system('ssh root@144.172.83.230')
        os.system('daxlydarkvps101')
        os.system('termux-tts-speak Connected to vps') 
        print('Connected to vps')
    elif 'BPS' in output:
        os.system('ssh root@144.172.83.230')
        os.system('termux-tts-speak Connected to vps') 
        print('Connected to vps')
    elif 'call' in output:
        number = output.replace('call ','')
        final = number.replace(' ', '') 
        print('Calling ' +final) 
        os.system(f'termux-tts-speak Calling {final}') 
        os.system(f'termux-telephony-call {final}') 
    else:
        print('Invalid command') 
        os.system('termux-tts-speak Invalid command') 
        pass
       
while True:
    utkvs(talkMe())
   

"""
am start --user 0 -n package.name/com.package.name.ActivityName
"""