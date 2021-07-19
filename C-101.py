import dropbox

class DropboxTransfer:
    def __init__(self, access_token):
        self.access_token = access_token


    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)



        d = open(file_from, 'rb')
        dbx.files_upload(d.read(), file_to)



def main():
    access_token = 'NfwQ_Itd6uUAAAAAAAAAAU3pyTDeZ1uA6AHAHH2GbMoF6jAQXjhxJ2cmi_-sxpHV'
    dropboxTransfer = DropboxTransfer(access_token)

    file_from = input('Enter the file path to transfer : ')
    file_to = input('Enter the full path of file to upload to Dropbox : ')

    dropboxTransfer.upload_file(file_from, file_to)
    print("File has been uploaded successfully")


main()
