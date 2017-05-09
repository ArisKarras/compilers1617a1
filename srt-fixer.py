import sys
import re
import argparse

rexp = re.compile(r'(\d\d):([0-5]\d):([0-5]\d,\d\d\d)\s-->\s(\d\d):([0-5]\d):([0-5]\d,\d\d\d)')

parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()
str1 = str(args.offset)
sec, milisec = str1.split('.')
if len(milisec) == 1:
	milisec = milisec + "0"
if len(milisec) == 2:
	milisec = milisec + "0"
sec = int(sec)
milisec = int(milisec)
if args.offset < 0:
	milisec = milisec * -1

with open(args.fname,newline='') as ifp:	
	for line in ifp:
	
		# -- αντικαταστήστε με τον δικό σας κώδικα (αρχή) --
		m = rexp.search(line)
		if m:
			a_hour = int(m.group(1))
			t_hour = int(m.group(4))
			a_min = int(m.group(2)) 
			t_min = int(m.group(5)) 
			a_sec, a_milisec = m.group(3).split(',')
			t_sec, t_milisec = m.group(6).split(',')
			a_sec = int(a_sec)
			t_sec = int(t_sec)
			a_milisec = int(a_milisec)
			t_milisec = int(t_milisec)
			a_sec = a_sec + sec
			t_sec = t_sec + sec
			a_milisec = a_milisec + milisec
			t_milisec = t_milisec + milisec			
			
			if a_milisec >= 1000:
				num1 = a_milisec // 1000
				a_milisec = a_milisec - (num1 * 1000)
				a_sec = a_sec + num1
				
			if t_milisec >= 1000:
				num4 = t_milisec // 1000
				t_milisec = t_milisec - (num4 * 1000)
				t_sec = t_sec + num4
			
			if a_sec >= 60:
				num2 = a_sec // 60
				a_sec = a_sec - (num2 * 60)
				a_min = a_min + num2
				
			if t_sec >= 60:
				num5 = t_sec // 60
				t_sec = t_sec - (num5 * 60)
				t_min = t_min + num5
			
			if a_min >= 60:
				num3 = a_min // 60
				a_min = a_min - (num3 * 60)
				a_hour = a_hour + num3
				
			if t_min >= 60:
				num6 = t_min // 60
				t_min = t_min - (num6 * 60)
				t_hour = t_hour + num6
						
			while a_milisec < 0:
				a_milisec = a_milisec + 1000
				a_min = a_min - 1

			while t_milisec < 0:
				t_milisec = t_milisec + 1000
				t_sec = t_sec - 1

			while a_sec < 0:
				a_sec = a_sec + 60
				a_min = a_min - 1
			
			while t_sec < 0:
				t_sec = t_sec + 60
				t_min = t_min - 1
				
			while a_min < 0:
				a_min = a_min + 60
				a_hour = a_hour - 1
					
			while t_min < 0:
				t_min = t_min + 60
				t_hour = t_hour - 1
		
			a_hour = str(a_hour)		
			if len(a_hour) == 1:
				a_hour = "0" + a_hour
			t_hour = str(t_hour)
			if len(t_hour) == 1:
				t_hour = "0" + t_hour
			a_min = str(a_min)
			if len(a_min) == 1:
				a_min = "0" + a_min
			t_min = str(t_min)
			if len(t_min) == 1:
				t_min = "0" + t_min
			a_sec = str(a_sec)
			if len(a_sec) == 1:
				a_sec = "0" + a_sec
			t_sec = str(t_sec)
			if len(t_sec) == 1:
				t_sec = "0" + t_sec
			a_milisec = str(a_milisec)
			if len(a_milisec) == 1:
				a_milisec = "0" + a_milisec
			if len(a_milisec) == 2:
				a_milisec = "0" + a_milisec
			t_milisec = str(t_milisec)
			if len(t_milisec) == 1:
				t_milisec = "0" + t_milisec
			if len(t_milisec) == 2:
				t_milisec = "0" + t_milisec
			
			sys.stdout.write(a_hour)
			sys.stdout.write(":")
			sys.stdout.write(a_min)
			sys.stdout.write(":")
			sys.stdout.write(a_sec)
			sys.stdout.write(",")
			sys.stdout.write(a_milisec)
			sys.stdout.write(" --> ")
			sys.stdout.write(t_hour)
			sys.stdout.write(":")
			sys.stdout.write(t_min)
			sys.stdout.write(":")
			sys.stdout.write(t_sec)
			sys.stdout.write(",")
			sys.stdout.write(t_milisec)
			sys.stdout.write("\n")
		else:
			sys.stdout.write(line)
			
# Aristeidis Karras
# P2013020
		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --

