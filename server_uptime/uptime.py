import logging
import argparse, sys
import urllib3

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", action="store", type=str)
    parser.add_argument("-u", "--url", action="store", type=str)
    parser.add_argument("-fe", "--fromEmail", action="store", type=str)
    parser.add_argument("-fep", "--fromEmailPassword", action="store", type=str)
    parser.add_argument("-te", "--toEmail", action="store", type=str)
    
    return parser.parse_args(sys.argv[1:])

def send_email(args):
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    try:
        server= smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(args.fromEmail, args.fromEmailPassword)
        msg=MIMEMultipart()
        msg['From']=args.fromEmail
        msg['To']=args.toEmail
        msg['Subject']="Error - Server Down"
        body= "Server %s is not working" % args.url
        msg.attach(MIMEText(body, 'plain'))
        server.sendmail(args.fromEmail,args.toEmail,msg.as_string())
        logging.debug("Email Notification is sent to " + args.toEmail)
    except Exception:
        logging.exception("couldn't send email to " + args.toEmail)
        
if __name__ == "__main__":
    args= get_arguments()

    #configuring logging files
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=args.file,
                    filemode='a')
    http = urllib3.PoolManager()
    
    response = http.request('GET',args.url )
    print (response)
    if response.status == 200:
        logging.debug(args.url + " is operational")
    else:
        logging.error(args.url + " IS NOT WORKING \n" + response.read())
        send_email(args)

