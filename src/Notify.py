from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/thelv/Documents/Redes 3/Practica3/PythonProject/rrd/'
imgpath = '/home/thelv/Documents/Redes 3/Practica3/PythonProject/img/'
fname = 'trend.rrd'

#mailsender = "dummycuenta3@gmail.com"
mailsender = "gustavo19ofi32@gmail.com"
mailreceip = "dummycuenta3@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'irqzantpaxcycxmk'

def send_alert_attached(subject,device,sw,time,date,comm):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(imgpath+'deteccionCPU.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msgHeadTxt = MIMEText("Información de inventario\n")
    msgDevTxt = MIMEText("Nombre del dispositivo: "+device+"\n")
    msgSwTxt = MIMEText("Sistema operativo: "+sw+"\n")
    msgTimTxt = MIMEText("Tiempo de operacion: "+time+"\n")
    msgDatTxt = MIMEText("Tiempo del sistema: "+date+"\n")
    msgComTxt = MIMEText("Comunidad del dispositivo: "+comm+"\n")
    nameTxt = MIMEText("López González Gustavo\tGrupo 4CM13")
    msg.attach(img)
    msg.attach(msgHeadTxt)
    msg.attach(msgDevTxt)
    msg.attach(msgSwTxt)
    msg.attach(msgTimTxt)
    msg.attach(msgDatTxt)
    msg.attach(msgComTxt)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()
    print("Mensaje enviado")