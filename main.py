#OTP GENERATOR
import random #RANDOM MODULE USED TO GENERATE RANDOM NUMBERS USED IN OTP
import smtplib #SMTP SIMPLE MAIL TRANSFER PROTOCOL USED TO E MAIL TH OTP IN THIS CASE
#HERE I HAVE USED FOR LOOP AND RANDOM MODULE TO GENERATE A OTP
int1 = int(input("enter the length of otp:"))
mylist1 = []
for i in range(int1):
    n1 = random.randint(1,9)
    mylist1.append(n1)
otp = ''.join(map(str,mylist1))
print(otp)
#HERE REST OF THE CODE WILL BE USED TO SEND THE EMAIL OTP USING SIMPLE MAIL TRANSFER PROTOCOL SMTP
#PS CUZ I AM A NOOB I USED CHATGPT TO GENERATE THE CODE WHICH WILL SEND EMAIL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(otp, recipient_email):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "HI YOUR OTP CODE IS:"
    body = f"your otp code is:{otp}"
    msg.attach(MIMEText(body,'plain'))

    #now  to send email
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.starttls() #this is used to upgrade the connection to secure
        server.login(sender_email, sender_password)
        server.send_message(msg)
print(otp)
send_email(otp,"hansrajmeenaji198@gmail.com")
try:
    send_email(otp, "hansrajmeenaji198@gmail.com")
except Exception as e:
    print(f"An error occurred: {e}")



