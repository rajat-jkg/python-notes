import smtplib
#smtplib is the module used for email automation

try:
    ser = smtplib.SMTP("smtp.gmail.com",587)
    # implement the email automation we first need to create a server which is done by the above statement
    # syntax(" smtp server name", port)
    # smtp server and port depends upon the mail we are using

    ser.starttls()
    # the above statement strts the server
    ser.login('project.autoemailer@gmail.com','simplepassword')
    # the above staement is for login
    sender = 'project.autoemailer@gmail.com'
    toMail = 'ypk0513@gmail.com'
    mes = 'Subject: Greetings \nHi Abhishek'
    ser.sendmail(sender,toMail,mes)
    #syntax for sending email: server.sendmail("sender email", "reciever email", "message")

except:
    print("Failed")

