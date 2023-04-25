import json
import re
import smtplib
import ssl
import subprocess
import datetime

import certifi
import requests
import telebot
from decouple import config
from imap_tools import MailBox, AND
from googletrans import Translator

API_KEY = config("API_KEY")
bot = telebot.TeleBot(API_KEY)
translator = Translator()

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

LANGCODES = dict(map(reversed, LANGUAGES.items()))

print("Starting")

@bot.message_handler()
def hello(message):
    # print(message)
    js = json.dumps({"_id":"6311f2815ff7c71aa1f78429","deleted":False,"ticketNumber":"225","subject":"lite tankar","description":"Hej.\nHar lite tankar och ideer som jag har samt frått från andra som använder plattformarna. \nNär det gäller dNFT plattformen hade det varit bra om man kunde klicka sig direkt från låten till handelsplattformen. Alltså om man ser på de avslutatde kampanjerna så skulle det finnas en direktlänk dit där man kan köpa dessa tokens.\n\nSen var det en som önskade en dela knapp på NFT sidan, så man direkt kan dela till olika medier.\n\nlite input bara :)\n\nha en go helg!","createdBy":"603e777bd354dd0b214689fd","creatorEmail":"daniel.berglov@gmail.com","status":"NOT_RESOLVED","ticketType":"USER","createdFor":{"type":"ADMIN"},"created_at":"2022-09-02T12:09:37.642Z","updated_at":"2022-09-02T12:09:37.642Z","__v":0})
    js = json.loads(js)
    print(js)
    ticketNumber = js["ticketNumber"]
    subject = js["subject"]
    date = datetime.datetime.strptime(js["created_at"],"%Y-%m-%dT%H:%M:%S.%fZ").date()
    description = js["description"]
    transDesc = trans(description,"en")
    transSubject = trans(subject,"en")

    bot.send_message(message.chat.id, f"ticketNumber: {ticketNumber}\ndate: {date}\n\nsubject: {transSubject.text}\n\n{transDesc.text}")

def trans(text,dest='en'):
    ''' Translator Function
    it Translate the text to the destionation language'''
    return  translator.translate(text,dest=dest)

# @bot.message_handler(commands=['anyreply'])
# def checkReply(message):
#     username = "rahulprojecthotel@gmail.com"
#     password = config("APP_KEY")
#     request = message.json.get("reply_to_message").get("entities")[0].get("type") == "email"
#     if request:
#         email = message.reply_to_message.text.split()[1]
#         mb = MailBox("imap.gmail.com").login(username, password)
#         bot.send_message(message.chat.id, "Checking your mail...")
#         mail_messages = mb.fetch(criteria=AND(seen=False, from_=email), mark_seen=False, bulk=True)
# #       since mail_message is class generator so we have to convert it to list get the len
#         if len(list(mail_messages)):
#             for msg in mail_messages:
#                 bot.send_message(message.chat.id, "You have some reply to that message")
#                 bot.send_message(message.chat.id, msg.text)
#         else:
#             bot.send_message(message.chat.id, "Sorry No reply to this message")
#     else: bot.send_message(message.chat.id, "Sorry wrong message")


# def handel_request(message):
#     request = message.text.split()
#     print(message.text)
#     if request[0] == "mail":
#         # print(request)
#         try:

#             # print(message.json.get("entities")[0].get("type"))
#             if message.json.get("entities")[0].get("type") == "email":
#                 # get the subject and message
#                 mess = re.findall('"([^"]*)"', message.text)
#                 if len(mess) > 1:
#                     bot.send_message(message.chat.id,
#                                      "your are trying to send two messages 🤨")
#                     return False
#                 elif len(mess[0]) == 0:
#                     bot.send_message(message.chat.id,
#                                      "There is nothing to send!")
#                     return False
#                 else:
#                     return True
#             else:
#                 bot.send_message(message.chat.id,
#                                  'Message should look like\nmail mailId_receiver "message"\n\nNOTE: message should '
#                                  'enclosed with double quote')
#                 return False

#         except Exception as e:
#             print(e)
#             bot.send_message(message.chat.id, "Something went wrong")
#             return False

#     else:
#         bot.send_message(message.chat.id,
#                          'Message should look like\nmail mailId_receiver "message"\n\nNOTE: message should '
#                          'enclosed with double quote')
#         return False


# def send_mail(mailTo, mess):
#     port = 465  # For SSL
#     password = config("APP_KEY")

#     # Create a secure SSL context
#     context = ssl.create_default_context(cafile=certifi.where())
#     mailFrom = "rahulprojecthotel@gmail.com"
#     # mailTo = "rahulnixonbit@gmail.com"
#     # mess = "hello!! how are you?"
#     receiver_name = mailFrom.split("@")[0]
#     message = "From: From {} <{}>\nTo: To {} <{}>\nMIME-Version: 1.0\nContent-type: text/html\nSubject: SMTP HTML " \
#               "e-mail test\n\n<pre>{}<pre>".format(
#         mailFrom.split("@")[0], mailFrom, receiver_name, mailTo, mess)
#     print(message)
#     try:
#         with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#             server.login(mailFrom, password)
#             server.sendmail(mailFrom, mailTo, message)
#             server.quit()
#             return True
#     except Exception as e:
#         print(e)
#         return False


# @bot.message_handler(func=handel_request)
# def reply_message(message):
#     request = message.text.split()
#     receivers_mail = request[1]
#     mess = re.findall('"([^"]*)"', message.text)
#     bot.send_message(message.chat.id, f"got The request\nmail = {receivers_mail}\nmessage = {mess[0]}")
#     bot.send_message(message.chat.id, "Sending mail.....")
#     status = send_mail(receivers_mail, mess[0])
#     if status:
#         bot.send_message(message.chat.id, "<strong>Mail Send successfully!!🤘</strong>")
#     else:
#         bot.send_message(message.chat.id, "failed to send mail!🫣")


# @bot.message_handler(func=lambda message: message.document.mime_type == 'application/pdf', content_types=['document'])
# def compressPdf(message):
#     reply = bot.send_message(message.chat.id, "Downloading File")
#     file_id = message.document.file_id
#     file_info = bot.get_file(file_id)
#     print(file_info)
#     if file_info:
#         fileReps = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_KEY, file_info.file_path))
#         print(fileReps.status_code)
#         if fileReps.status_code == 200:
#             reply = bot.edit_message_text("Got the file", message.chat.id, reply.message_id)
#             with open(message.document.file_name, "wb") as file:
#                 file.write(fileReps.content)
#                 file.close()
#             reply = bot.edit_message_text("Compressing...", message.chat.id, reply.message_id)
#             subprocess.call(["gs", '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
#                              '-dPDFSETTINGS=/ebook',
#                              '-dNOPAUSE', '-dQUIET', '-dBATCH',
#                              '-sOutputFile={}_compressed'.format(message.document.file_name),
#                              message.document.file_name])
#             try:
#                 file = open(message.document.file_name + "_compressed", "rb")
#                 bot.edit_message_text("sending...", message.chat.id, reply.message_id)
#                 bot.delete_message(message.chat.id, reply.message_id)
#                 bot.send_document(message.chat.id, file)
#                 print("file send")
#                 file.flush()
#             except Exception as e:
#                 print(e)
#         else:
#             bot.edit_message_text("Unable to download file!", message.chat.id, reply.message_id)

#     else:
#         bot.edit_message_text("Unable to download file!", message.chat.id, reply.message_id)


bot.polling()
