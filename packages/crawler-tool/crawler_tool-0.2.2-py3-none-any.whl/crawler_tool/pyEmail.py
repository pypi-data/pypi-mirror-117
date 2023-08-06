# -*- coding: utf-8 -*-

# author: 'ileona'
# date: 2021/8/26 10:33


from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


class Email(SMTP_SSL):
    def __init__(self, smtp_server, port, from_mail, password):
        super(Email, self).__init__(smtp_server, port)
        self.from_mail = from_mail
        self.password = password

    def send_text(self, from_name, title, text, to_emails):
        msg = MIMEText(text, 'plain', 'utf-8')
        # 邮件头信息
        msg['From'] = Header(from_name)
        msg['To'] = Header(",".join(to_emails))
        msg['Subject'] = Header(title)

        self.login(user=self.from_mail, password=self.password)
        self.sendmail(from_addr=self.from_mail, to_addrs=to_emails, msg=msg.as_string())
        self.quit()
