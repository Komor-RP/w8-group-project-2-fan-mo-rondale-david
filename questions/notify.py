import yagmail


class Notify(object):
    def sendemail(self, recipient, subject, body):
        yag = yagmail.SMTP('questionbox18@gmail.com', 'fanmorondave')
        yag.send(recipient, subject, body)
