import subprocess

# diccionario de las ips
process = {}

for i in range(1, 255):
    # ip general
    ip = "192.168.0."+str(i)
    process[ip] = subprocess.Popen(['ping', '-c1', ip], stdout=subprocess.DEVNULL)
    
while process:
    for ip, proc in process.items():
        # si encuentra un proceso NONE, la ip la eliminamos
        if proc.poll() is not None:
            del process[ip]
            # print(proc.returncode)
            if proc.returncode == 0:
                print(ip)
            break 
    
