#  Filename:  PythonNamespace.pyw
#  Date Updated:  Oct. 15, 2019
#  Author:  Jonas McClure (jonmcclu@iu.edu)

#  Purpose:  Allow input of web addresses and output the IP addresses associated with their domain names.

# Import Directives
import socket
import tkinter
import fnmatch


def get_address(name):
    # Function Input:  web address from tkinter form input
    # Function Output:  list/array of IP addresses returned for the input address
    ip_list = []
    address = socket.getaddrinfo(name, 0, 0, 0, 0)
    for result in address:
        ip_list.append(result[-1][0])
    return ip_list


def find_iu_address(address):
    # Function Input:  first IP address found associated with the input web address
    # Function Output:  string indicating the addresses relation to central hosting services at IU.
    func_out = ""
    if (address == "2001:18e8:2:e::104") or (address == "2001:18e8:2:e::103") or (address == "129.79.123.148") or \
            (address == "129.79.123.149"):
        func_out = "This address points to the IU Sitehosting production servers. \n\n"
    elif (address == "2001:18e8:2:e::102") or (address == "2001:18e8:2:e::101") or (address == "129.79.123.146") or \
            (address == "129.79.123.147"):
        func_out = "This address points to the IU Sitehosting test servers. \n\n"
    elif fnmatch.fnmatch(address, '129.79.78.*'):
        # Matches any IP addresses that start with 129.79.78 -- indicating their existence on Webserve
        func_out = "This address point to the IU Webserve servers. \n\n"
    else:
        func_out = "This address is not pointing to IU Sitehosting or Webserve. \n\n"
    return func_out


def main_window():
    # Create the primary tkinter window with dimensions of 500x500.
    window = tkinter.Tk()
    window.title("Python Namespace")
    window.geometry('500x500')

    # Create a tkinter entry section to allow input for the web address
    label = tkinter.Label(window, text="Enter the URL:")
    label.pack()
    entry = tkinter.Entry(window, bd=5, width="75")
    entry.pack()

    def text_input():
        # Function:  grabs entry input and placed 'getAddress()' output into a textbox
        user_input = entry.get().strip()  # Removes the leading and trailing spaces from the input address
        try:
            list_len = len(get_address(user_input))
            text.delete('1.0', 'end')
            text.insert('1.0', find_iu_address(get_address(user_input)[0]))
            text.insert('end', "The IP Addresses for [" + user_input + "] are:  \n")
            for i in range(list_len):
                rel_address = get_address(user_input)[i]
                text.insert('end', rel_address + '\n')
        except:  # Outputs if an associated web address is not found
            text.delete('1.0', 'end')
            text.insert('1.0', "Unable to obtain information about that address.")

    def onclick(event=None):
        text_input()
        return

    window.bind('<Return>', onclick)

    # Button to grab the text
    button = tkinter.Button(window, text="Search", command=onclick)
    button.pack()

    text = tkinter.Text(window)
    text.pack()

    window.mainloop()
    return


def main():
    main_window()
    return


main()
