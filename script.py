#!/usr/bin/python3
#!/bin/bash
import os
import requests
import json
import subprocess




file_path2 = os.path.abspath('i2b.c.')
file_path2 = os.path.abspath('12h.c')

with open('0_autograde.txt', 'r') as file:
 autoGrade = file.read()
 
x =list(map(lambda a: a.split(" ")[1:] , (autoGrade.split("\n"))))

#line by line string
y = '\n'.join(' '.join(sublist) for sublist in x)
print("____________________________________________________LLAMA-AUTOGRADER____________________________________________________________")
#print(y)
print("____________________________________________________LLAMA-AUTOGRADER____________________________________________________________")

y =[line for line in y.split("\n") if line]



       
    
# for line in y:
#     print(line[0]) 

# for line in y:
#     print(line) 

# parameters =[]
# for line in y:
#     if line[0] == '📝':
#      while line != '::***:' or line[0]!='📝':
#       parameters.append(line)
    

teachercompare1 = "/test/negative_bin.sh"
teachercompare2 = "/test/negative_hex.sh"
teachercompare3 = "/test/positive_bin.sh" 
teachercompare4 = "/test/positive_hex.sh"
studentcode1 = os.path.abspath('i2b.c.')
studentcode2 = os.path.abspath('i2h.c.')
autograder = y
request = f""" student code " "{studentcode1}" & {studentcode2} " github autograder output " "{autograder} " " test comparing results  " "{teachercompare1}" &  "{teachercompare2}"& "{teachercompare3}"& "{teachercompare4}" "  """


url = "http://localhost:11434/api/generate"
data = {
    "model": "llama3.1",
    "prompt": request,
    "stream": False
}

# Send a POST request
response = requests.post(url, json=data)

# print(response.text)

print(response.json().get("response", ""))

if os.path.exists("feedback.md"):
 with open("feedback.md", "a") as file:
  file.write("\n__________LLAMA AUTOGRADER START__________\n")
  file.write(response.json().get("response", "")) 
  file.write("\n__________LLAMA AUTOGRADER END__________\n")
else:
 with open("feedback.md", "w") as file:
  file.write("\n__________LLAMA AUTOGRADER START__________")
  file.write(response.json().get("response", "")) 
  file.write("\n__________LLAMA AUTOGRADER END__________\n")


file_path1 = os.path.abspath('0_autograde.txt')

subprocess.run('git add .', shell=True)
subprocess.run('git commit -m "0"', shell=True)
subprocess.run('git push origin main', shell=True)






#print(y)
#print(y.split("\n"))
