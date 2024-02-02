# Python Website blocker and unblocker
# Python application that blocks the access of websites, redirecting the user back to localhost


import platform


def block_website(hosts_path, blocked_websites):
    try:
        with open(hosts_path, 'r+') as f:
            # Reads file content
            content = f.read()

            # Writes a redirect command for the specified website back to localhost, blocking the website access
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    f.write(f"{localhost} {website}\n")

    # Handles possible errors
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(e)


def unblock_website(hosts_path, blocked_websites):
    try:
        with open(hosts_path, 'r+') as f:
            # Reads file content
            content = f.readlines()

            # Sets the file position indicator to the beginning of the file
            f.seek(0)

            # Checks if the blocked website inside the file is still a blocked website
            # If not, doesn't write the website into the file
            for line in content:
                if any(website in line for website in blocked_websites):
                    f.write(line)

            # Removes any content after the last line that was written
            f.truncate()

    # Handling possible errors
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(e)


# Retrieves 'hosts' file path based on operating system
# We will use the 'hosts' file to redirect certain websites back to localhost 127.0.0.1
if platform.system() == "Windows":
    path_to_hosts = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux":
    path_to_hosts = r"/etc/hosts"
else:
    path_to_hosts = r"undefined"

localhost = "127.0.0.1"
websites_to_be_blocked = [r"https://www.facebook.com/", r"https://www.instagram.com/", r"https://www.tiktok.com"]

block_website(path_to_hosts, websites_to_be_blocked)
