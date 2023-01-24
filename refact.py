import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailWorks():
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    def send_message(self, subject, recipients, message):
        
        GMAIL_SMTP = "smtp.gmail.com"
        
        #Отправить сообщение
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        # идентифицируем себя в клиенте smtp gmail
        ms.ehlo()
        # защитить нашу электронную почту с помощью шифрования tls
        ms.starttls()
        # повторно идентифицировать себя как зашифрованное соединение
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login)
        ms, msg.as_string()

        ms.quit()
        # ---------------


    def receive_message(self, header):
        
        GMAIL_IMAP = "imap.gmail.com"
        
        # Получить 
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        
        assert data[0], 'Нет писем с текущим заголовком'
        
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        
        mail.logout()
        
        return email_message





if __name__ == '__main__':
    
    login = 'av.nezdanov@gmail.com'
    password = 'uvgb1985'
    subject = 'Subject'
    recipients = ['nezdan@inbox.ru', 'beskonpanda@gmalil.com']
    message = 'Message'
    header = None
    
    
    mail = MailWorks(login, password)
    
    # Отправить письмо
    mail.send_message(subject, recipients, message)
    
    # Получить писма
    mail.receive_message(header)

    