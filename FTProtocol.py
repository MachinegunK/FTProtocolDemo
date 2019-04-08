import ftplib

ftp_address=input('Please enter your FTP Address: ')

ftplib.FTP(ftp_address)
user_name=input('Enter your username: ')
user_passwrd=input('Enter your password: ')


ftp.login(user= user_name,passwd= user_passwrd)

desiredDirectory= input('Type in desired directory: ')

ftp.cwd(desiredDirectory)

Print('Contents of the directory:',ftp.pwd())
ftp.dir()

downloader()

uploader()

deleter()


#downloading function
def downloaderr():

       filer=input('Name of file to download:')
       ftp.retrbinary('RETR'+ filer,open(filer,'wb').write)
            
       ftp.quit()
       return;

            
#uploading function
def uploader():

       uploadfile=input('Name of file to upload: ')
       ftp.storbinary('STOR'+uploadfile,open(uploadfile,'rb'))
       
       ftp.quit()
       return;

#deleting function
def deleter():

    waster=input('Name of file to delete(include its extension): ')
    ftp.delete(waster)

    ftp.quit()                  
    return;








