import socket # Network connections (TCP/UDP)
import time # Time-related functions

host = [
    "google.com",
    "facebook.com",
    "youtube.com",
    "1.1.1.1",
    "8.8.8.8",
    "8.8.4.4"
] # List of hosts to check reachability

Port = 80 # HTTP port (can be changed to 443 for HTTPS)

timeout_in_seconds = 4.0 # Timeout for each connection attempt

def check_host_reachability(host, port, timeout): # Function to check if a host is reachable on a specific port
    start_time = time.time() # Record the start time

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
    
    sock.settimeout(timeout) # Set the timeout for the socket

    try:
        sock.connect((host, port)) # Attempt to connect to the host and port
        end_time = time.time() # Record the end time
        elapsed_time = end_time - start_time # Calculate elapsed time
        sock.close() # Close the socket
        return "OK", elapsed_time # Return success status and elapsed time
    
    except socket.timeout:
        end_time = time.time() # Record the end time
        elapsed_time = end_time - start_time # Calculate elapsed time
        sock.close() # Close the socket
        return "TIMED OUT", elapsed_time # Return timeout status and elapsed time
    
    except socket.gaierror as e:
        end_time = time.time() # Record the end time
        elapsed_time = end_time - start_time # Calculate elapsed time
        sock.close() # Close the socket
        return f"ERROR: {e}", elapsed_time # Return error status and elapsed time
    
    except OSError as e:
        end_time = time.time() # Record the end time
        elapsed_time = end_time - start_time # Calculate elapsed time
        sock.close() # Close the socket
        return f"ERROR: {e}", elapsed_time # Return error status and elapsed time
    
for h in host: # Iterate through each host in the list
    status, elapsed = check_host_reachability(h, Port, timeout_in_seconds) # Check reachability
    elapsed_str = f"{elapsed:.3f} seconds" # Format elapsed time to 3 decimal places

    print(f"{h:<25} | port {Port:<5} | {status:<20} | time: {elapsed_str}") # Print the results