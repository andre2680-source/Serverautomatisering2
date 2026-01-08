import socket # Import the socket module for network operations

while True:
    AskForUrl = input ("please enter a website URL (e.g., google.com): ") # Prompt user for a website URL
    try:
        ip_address = socket.gethostbyname(AskForUrl) # Attempt to get the IP address for the URL
        print(f"The IP address of {AskForUrl} is {ip_address}.") # Print the resolved IP address
        break # Exit the loop if successful
    except socket.gaierror as e:
        print(f"DNS lookup failed for {AskForUrl}. Error: {e}") # Print an error message if the lookup fails