from imap_tools import MailBox, AND

# use your email id here
username = "rahulprojecthotel@gmail.com"

# use your App Password you
# generated above here.
password = "ixvujnbhrfrzuhhr"
mb = MailBox("imap.gmail.com").login(username, password)
messages = mb.fetch(criteria=AND(seen=False, from_="rahulnixonbit@gmail.com"), mark_seen=False, bulk=True)
for msg in messages:
    print(msg.from_, msg.text, msg.subject, msg.html)
