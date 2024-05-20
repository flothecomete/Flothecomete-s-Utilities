import extract_msg
import os
from sys import argv

man = """
msg_to_txt(1)                  User Commands                  msg_to_txt(1)

NAME
       msg_to_txt - Convert Outlook msg file to txt

SYNOPSIS
       msg_to_txt [OPTIONS] ARGUMENTS

DESCRIPTION
       examplecmd est une commande fictive utilisée à des fins de démonstration
       dans cet exemple de page de manuel.

OPTIONS
       -h
           Show this manual

       -f
           File mode. To convert one file.

       -d
           Directory mode. All the files of the specified directory will be convert. 

ARGUMENTS
       PATH
           Path of the file/directory.

EXAMPLES
       msg_to_txt -f mail.msg
           Convert the file mail.msg.

       msg_to_txt -d path/to/folder
           Convert all the files in path/to/folder.

AUTHOR
       Writed by Flothecomete.

REPORTING BUGS
       Report bugs on <https://github.com/flothecomete/Flothecomete-s-Utilities>.

COPYRIGHT
       Copyright © 2024 Flothecomete.
       Licence GPLv3+: GNU GPL version 3 ou ultérieure
       <https://gnu.org/licenses/gpl.html>.
       Ceci est un logiciel libre : vous êtes libre de le modifier et de le redistribuer.
       Il n'y a AUCUNE GARANTIE, dans la mesure permise par la loi.

                                                           msg_to_txt(1)

"""

def directory_msg_to_txt(directory):
    for file in os.listdir(directory):
        msg_to_txt(path=directory+"/"+file)
    

def msg_to_txt(path):
    message = extract_msg.Message(path)
    headers = message.header.__str__()
    sender = message.sender
    sent = message.date.strftime("%a, %d %b %X %z")
    to = message.to
    subject = message.subject
    body = message.body

    with open(path[:-4]+".txt", 'w', encoding="utf-8") as output:
        output.write(headers + "\n")
        output.write("From: " + sender + "\n")
        output.write("Sent: " + sent + "\n")
        output.write("To: " + to + "\n")
        output.write("Subject: " + subject + "\n")
        output.write("-----------------\n\n")
        output.write(body)

    message.close()

if __name__ == "__main__":
    options = ["-f", "-d", "-h"]
    argc = len(argv)
    scriptname = argv[0]
    if argc != 2 and argc != 3:
        print(f"usage: {scriptname} [option] path")
    else:
        option = argv[1]
        if option not in options:
            print(f"options are {options}\n\t{scriptname} -h \tfor help")
        elif option == "-h":
            print(man)
        elif argc == 3:
            path = argv[2]
            if option == "-f":
                msg_to_txt(path=path)
            elif option == "-d":
                directory_msg_to_txt(directory=path)
            else:
                print(f"usage: {scriptname} [option] path")
        else:
            print(f"usage: {scriptname} [option] path")
