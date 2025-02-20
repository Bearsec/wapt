def queueRequests(target, wordlists):
    # Initialize the RequestEngine with the target endpoint and connection settings
    # concurrentConnections: Number of simultaneous connections to the target server.
    # requestsPerConnection: Number of requests to send per connection before closing it.
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    # Iterate over words in the dictionary
    for word in open('/home/kali/directory-list-2.3-medium.txt'):
        word = word.rstrip()  # Remove whitespace and newline characters
        # Add extensions to each word
        for ext in ['.txt', '.php', '.zip']:
            # Form the full word with the extension
            full_word = "{}{}".format(word, ext)
            # Queue the request with the full word
            engine.queue(target.req, full_word)


def handleResponse(req, interesting):
    # Check the response status
    if req.status != 404:
        # If the status is not 404, add the request to the table
        table.add(req)
