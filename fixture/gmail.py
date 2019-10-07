import pprint
import time


from imbox import Imbox





class Letter:
    def __init__(self, ident, subject, date, content):
        self.id = ident
        self.subject = subject
        self.date = date
        self.content = content

    def __repr__(self):
        return str(self.__dict__)

class Inbox:

    def __init__(self):
        self.mail = Imbox('imap.gmail.com', username='igory@smashedmedia.com',password= 'Admin@1!', ssl=True)


    def all_inbox_messages(self):
        all = self.mail.messages()

    def get_last_message(self):
        inbox_messages_from = self.mail.messages(sent_from='infotest@smashedmedia.guru')
        for uid, message in inbox_messages_from:  # Every message is an object with the following
            subject = message.subject
            content = message.body.plain
            print ({'subject':subject,'content':content})


    def clear_inbox(self):
        all = self.mail.messages()
        for uid, message in all:
            self.mail.delete(uid)
