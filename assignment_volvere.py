import platform
import subprocess 
import speedtest
import pyautogui
import psutil
import socket


print(" All Installed software list")
try:
    data = subprocess.check_output(['wmic', 'product', 'get', 'name'], universal_newlines=True)
    product_names = data.split('\n')[1:]  # Assuming the first line is a header and skipping it

    for product_name in product_names:
        print(product_name.strip())

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
    
   
print(" Internet Speed ")  
# internet speed
speed = speedtest.Speedtest();
print("Download Speed = ",speed.download())
print("Upload Speed = ",speed.upload())

print(" Screen resolvution")
# screen resolution
print(pyautogui.size()) 

print(" No of core and threads of CPU , Windows version,  CPU Model And RAM Size")
my_system = platform.uname()
print(f"OS Name: {my_system.system}")
print(f"OS Version: {my_system.version}")
print(f"CPU Model: {my_system.processor}") #CPU Model
print("Core Count= ",psutil.cpu_count())
print("Thread count= ",psutil.cpu_count()/psutil.cpu_count(logical=False))
print("RAM = ",int(psutil.virtual_memory().total/1000000000 ))

print("  Wifi/Ethernet mac address")
for interface in psutil.net_if_addrs():
    	# Check if the interface has a valid MAC address
	if psutil.net_if_addrs()[interface][0].address:
		# Print the MAC address for the interface
		print(psutil.net_if_addrs()[interface][0].address)
		break

print(" Public IP address")
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
print(get_ip_address())


