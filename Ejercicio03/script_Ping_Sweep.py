import subprocess
import sys 

p = {}
for i in range(1, 255):
    ip = "{}.{}".format(sys.argv[1], i)
    p[ip] = subprocess.Popen(['ping', '-c1', ip], stdout=subprocess.DEVNULL)
    
while p:
    for ip, proc in p.items():
        if proc.poll() is not None:
            del p[ip]
            if proc.returncode == 0:
                print(ip)
            elif proc.returncode == 1:
                pass
            else:
                print('%s error' % ip)
            break 
    
