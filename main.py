import encryption
e_key = input("Key: ").upper()
e_msg = input("Messege: ").upper()

print("\nPress 1 for Encryption.")
print("Press 2 for Decryption.")
e_d = input("\nSelect: ")

if e_d == "1":
    print("\nEncrypted Message: ", encryption.encrypt(e_key,e_msg))
elif e_d == "2":
    print("\nDecrypted Message: ", encryption.decrypt(e_key,e_msg))
else:
    print("\nInvalid Key: 1 or 2 only.")


#Sample
#Key:                   space               | Key:                  red
#Message:               tommorow are quiz   | Message:              kill the bug
#Encrypted Message:     MWU MAI ORZ OOQ TRE | Encrypted Message:    LHU  ITB  KLEG

