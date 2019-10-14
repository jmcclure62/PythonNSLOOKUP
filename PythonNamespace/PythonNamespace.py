##  Filename:  PythonNSLOOKUP.py
##  Date Updated:  Oct. 14, 2019
##  Author:  Jonas McClure (jonmcclu@iu.edu)

##  Purpose:  Allow input of web addresses and output the IP addresses associated with their domain names.

## Import Directives
import socket
import tkinter


def getAddress(name):
    ip_list = []
    address = socket.getaddrinfo(name,0,0,0,0)
    for result in address:
        ip_list.append(result[-1][0])
#    ip_list = list(set(ip_list))

    return ip_list


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
        ## TODO:  create input validation for entry.get() -- remove initial and trailing spaces
        userInput = entry.get().strip()
        try:
            listLen = len(getAddress(userInput))
            text.delete('1.0', 'end')
            for i in range(listLen):
                text.insert('1.0', getAddress(userInput)[i] + '\n')
        except:
            text.delete('1.0','end')
            text.insert('1.0', "Unable to obtain information about that address.")

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

#Followup Links

# https://www.datacamp.com/community/tutorials/gui-tkinter-python#GM

## TODO List
# Enable pressing 'return' to hit the button