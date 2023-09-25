
import subprocess
a="eth0"
c = "180"
d = 1
for i in range(0,255,1):
	d = d+1
	str(d)
	for j in range(0,255,1):
		subprocess.call("ifconfig " + a + " inet " + "192.168." + c+"."+ str(d), shell= True)
