def queueRequests(target, wordlists):
    # Initialize the RequestEngine with the target endpoint and connection settings
    # concurrentConnections: Number of simultaneous connections to the target server.
    # requestsPerConnection: Number of requests to send per connection before closing it.
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=40,
                           requestsPerConnection=1,
                           pipeline=False
                           )

    # Specify the range of numbers for fuzzing
    start_range = 0
    end_range = 9999

    # Iterate over the specified range of numbers
    for number in range(start_range, end_range + 1):
        # Format the number as a string (with leading zeros if necessary)
        formatted_number = str(number).zfill(4)  # Ensures numbers are 4 digits (e.g., 0001, 0010)

        # Queue the request with the number      
        engine.queue(target.req, formatted_number)


def handleResponse(req, interesting):
    # Check the response status
    if req.status != 404:
        # If the status is not 404, add the request to the table
        table.add(req)
