##  Filename:  PythonNSLOOKUP.py
##  Date Updated:  Oct. 12, 2019
##  Author:  Jonas McClure (jonmcclu@iu.edu)

##  Purpose:  Allow input of web addresses and output the IP addresses associated with their domain names.

## Import Directives
import socket
import tkinter


def getAddress(name, listPlace):
    ip_list = []
    address = socket.getaddrinfo(name,0,0,0,0)
    for result in address:
        ip_list.append(result[-1][0])
#    ip_list = list(set(ip_list))

    return ip_list[listPlace]


def mainWindow():
    # The primary window
    window = tkinter.Tk()
    window.title("Python NSLOOKUP")
    window.geometry('500x500')

    # The text input
    label = tkinter.Label(window, text = "Enter the URL:")
    label.pack()
    entry = tkinter.Entry(window,bd=5)
    entry.pack()

    def textInput():
        #TODO:  Change (4) to the size of ip_list
        text.delete('1.0', 'end')
        for i in range(4):
            text.insert('1.0', getAddress(entry.get(), i) + '\n')

    # Button to grab the text
    button = tkinter.Button(window, text = "Search", command =  textInput)
    button.pack()

    text = tkinter.Text(window)
    text.pack()

    window.mainloop()
    return


def main():
    mainWindow()
    return

main()
