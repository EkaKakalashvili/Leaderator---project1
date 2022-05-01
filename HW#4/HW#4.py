"""
Eka Kakalashvili
823419435
Homework – 4. Complete the code.
You must:
    (1) complete implementations of the existed methods.
    (2) write a method that uploads files and directories to the FTP server
        with an existing structure on the local computer.
    (3) test you FTP_Client class
"""
from ftplib import FTP, error_perm
import os


class FTP_Client(FTP):  # localhost --> 127.0.0.1

    def __init__(self, host='127.0.0.1', user='user1', passw='test123'):
        super().__init__(host, user, passw)

    def __str__(self):
        return self.getwelcome()

    def ftp_UploadFile(self, file1, file2, size=4096):
        """ this function uploads file file1 to FTP server with name file2. """
        if len(file1) > 4 and '.' in file1 and file1[-3:].lower() == 'txt':
            with open(file1) as file:
                self.storlines('STOR ' + file2, file)
        else:
            with open(file1, 'rb') as file:  # Open file as binary file
                self.storbinary('STOR ' + file2, file, size)

    def ftp_DownloadFile(self, file1, file2):
        """ this function downloads file file1 from FTP server with name file2. """
        with open(file2, 'wb') as file:
            self.retrbinary('RETR ' + file1, file.write)

    def ftp_RenameFile(self, fromName, toName):
        """Rename file fromName on the server to toName"""
        try:
            self.rename(fromName, toName)
        except error_perm:
            print("File cannot be renamed!")

    def ftp_DeleteFile(self, FileName):
        """ Remove the file named filename from the server."""
        try:
            self.delete(FileName)
        except error_perm:
            print("Such file does not exist!!!")

    def ftp_CreateDirectory(self, DName):
        """ Create a new directory on the server. """
        try:
            self.mkd(DName)
        except error_perm:
            print("Directory not created!")

    def ftp_DeleteFolder(self, DName):
        """ Remove the directory named DName on the server. """
        try:
            self.rmd(DName)
        except error_perm:
            print("File not found.")

    def ftp_ChangeDirectory(self, DName):
        """ Change directory on the server. """
        try:
            self.cwd(DName)
        except error_perm:
            print("Directory wasn't entered.")

def main():
    """
                your code
    """
    client = FTP_Client()

    client.ftp_CreateDirectory('HW#4')

    for (directory, folders, files) in os.walk('.'):
        print(directory, folders, files)
        directory = directory.replace('.', 'HW#4')
        client.ftp_ChangeDirectory(".\\" + directory)

        for folder in folders:
            client.ftp_CreateDirectory(folder)
        for file in files:
            pathToFile = directory + "\\" + file
            client.ftp_UploadFile(pathToFile, file)

if __name__ == '__main__':
    main()
