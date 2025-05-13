import ftplib  # Import the ftplib module for FTP operations
import socket # Import the socket module for network operations

def check_anonymous_ftp(ip_list, timeout=10):
    """
    Checks for anonymous FTP login on a list of IP addresses.

    Args:
        ip_list (list): A list of IP addresses to check.
        timeout (int, optional): The timeout for socket connections in seconds. Defaults to 10.
    """
    results = []  # Initialize an empty list to store the results for each IP
    for ip in ip_list:
        print(f"[+] Checking FTP anonymous login on {ip}")
        result = {'ip': ip, 'anonymous_login': False, 'read_access': False, 'write_access': False, 'error': None}  # Initialize a dictionary to store the results for the current IP
        try:
            # Establish a connection with a timeout
            ftp = ftplib.FTP(ip, timeout=timeout)
            # Attempt anonymous login
            ftp.login('anonymous', 'anonymous@example.com')  # Use 'anonymous' as the username and a dummy email address
            print(f"[+] Anonymous login successful on {ip}")
            result['anonymous_login'] = True  # Set the anonymous_login flag to True if successful

            # Check for read/write permissions (a basic check)
            try:
                # Attempt to list files.  If this succeeds, we can read.
                ftp.retrlines('LIST', lambda x: None) # No need to print the listing.  Use a lambda to avoid printing to console
                print(f"[+] Read access allowed on {ip}")
                result['read_access'] = True  # Set the read_access flag to True if successful

                # Attempt to create a directory. If this succeeds, we can write.
                try:
                    ftp.mkd('test_dir')
                    print(f"[+] Write access allowed on {ip}")
                    result['write_access'] = True  # Set the write_access flag to True if successful
                    ftp.rmd('test_dir')  # Clean up the directory we created.  Remove the test directory.
                except ftplib.all_errors as e:
                    if "550" in str(e):  # Check for "550 Permission denied" error specifically
                         print(f"[-] Write access denied on {ip}")
                    else:
                        print(f"[!] Error checking write access on {ip}: {e}")  # Print other write-related errors
                        result['error'] = f"Error checking write access: {e}"  # Store the error message
            except ftplib.all_errors as e:
                if "550" not in str(e):
                    print(f"[-] Read access denied on {ip}")
                else:
                    print(f"[!] Error checking read access on {ip}: {e}")
                    result['error'] = f"Error checking read access: {e}"
            ftp.quit()  # Close the FTP connection
        except ftplib.all_errors as e: # Catch FTP errors
            if "timed out" in str(e):
                print(f"[-] Connection timed out on {ip}")
                result['error'] = "Connection timed out"  # Store the error message
            elif "refused" in str(e):
                print(f"[-] Connection refused on {ip}")
                result['error'] = "Connection refused"  # Store the error message
            elif "530 Login incorrect" in str(e):
                print(f"[-] Anonymous login failed on {ip}")
                result['error'] = "Anonymous login failed"  # Store the error message
            else:
                print(f"[!] Error connecting to {ip}: {e}")
                result['error'] = f"Error connecting: {e}"  # Store the error message
        except socket.gaierror: # Catch socket errors
            print(f"[-] Could not resolve hostname {ip}")
            result['error'] = "Could not resolve hostname"  # Store the error message
        except Exception as e: # Catch any other errors
            print(f"[!] An unexpected error occurred while checking {ip}: {e}")
            result['error'] = f"Unexpected error: {e}"  # Store the error message
        finally:
            results.append(result)  # Append the result dictionary to the list
    return results  # Return the list of results

if __name__ == "__main__":
    # List of IP addresses to check
    ip_addresses = ['127.0.0.1', '192.0.2.0']

    # You can replace this list with IPs from a file
    # with open('ip_list.txt', 'r') as f:
    #     ip_addresses = [line.strip() for line in f]

    results = check_anonymous_ftp(ip_addresses)  # Call the function to check the IPs

    # Print the results
    print("\n+-----------------------------------------------------------------------------+")
    print("|                               FTP Check Results                               |")
    print("+-----------------------------------------------------------------------------+")
    for result in results:
        print(f"| IP Address: {result['ip']:47} |")
        print(f"| Anonymous Login: {str(result['anonymous_login']):43} |")
        print(f"| Read Access: {str(result['read_access']):46} |")
        print(f"| Write Access: {str(result['write_access']):45} |")
        if result['error']:
            print(f"| Error: {result['error']:49} |")
        print("+-----------------------------------------------------------------------------+")

