import hashlib
import sqlite3
from connection import con, cur


def encrypt_data(data, key):
    encrypted = ''
    for char in data:
        encrypted += chr(ord(char) ^ key)
    return encrypted

def process_data(name, email, phone, username, password):
    username_hash = hashlib.sha256(username.encode()).hexdigest()
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    encryption_key = 123
    encrypted_name = encrypt_data(name, encryption_key)
    encrypted_email = encrypt_data(email, encryption_key)
    encrypted_phone = encrypt_data(phone, encryption_key)
    return (encrypted_name, encrypted_email, encrypted_phone, username_hash, password_hash)

if __name__ == "__main__":
    member_name = "Greg Paul"
    member_email = "greg.paul@example.com"
    member_phone = "123-456-7890"
    member_username = "greg"
    member_password = "paul"

    encrypted_data = process_data(member_name, member_email, member_phone, member_username, member_password)
    
    print("Encrypted Name: " + encrypted_data[0])
    print("Encrypted Email: " + encrypted_data[1])
    print("Encrypted Phone: " + encrypted_data[2])
    print("Hashed Username: " + encrypted_data[3])
    print("Hashed Password: " + encrypted_data[4])

    try:
        con = sqlite3.connect('Libarary.db')
        cur = con.cursor()
        query = "INSERT INTO 'members' (memberName, memberEmail, memberPhone, employee, password, username) VALUES(?,?,?,?,?,?)"
         # Assuming 'employee' is set to 0 for a regular member
        cur.execute(query, (encrypted_data[0], encrypted_data[1], encrypted_data[2], 0, encrypted_data[4], encrypted_data[3]))
        con.commit()
        con.close()
        print("data in database")
    except:
        print("error")