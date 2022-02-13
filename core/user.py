import hashlib
from data.user_data import UserData

class User(UserData):
  def login(self):
    user_data = None
    flag = 0
    
    while True:
      email = input("Silahkan masukkan email anda: ").strip().lower()
      password = input("Silahkan masukkan password anda: ").strip()

      data = self.get_by_email(email)
      
      if not data and flag < 3:
        print("Email atau password salah!\n")
        flag += 1
        continue
      
      if flag >= 3:
        print("Anda telah mencoba login 3 kali. Silahkan coba lagi!\n")
        break
      
      password_hash = str(hashlib.md5(bytes(str(password).encode('utf-8'))).hexdigest())
      
      if data['password'] == password_hash:
        user_data = data
        print("Login berhasil!")
        break
      
      print("Email atau password salah!")
      
    return user_data
  
  def register(self):
    user_data = None
    
    while True:
      name = input("Silahkan masukkan nama anda: ").strip()
      email = input("Silahkan masukkan email anda: ").strip().lower()
      password = input("Silahkan masukkan password anda: ").strip()

      name.replace(" ", "")
      email.replace(" ", "")
      password.replace(" ", "")

      data = self.get_by_email(email)
      
      if data:
        print("Email sudah didaftarkan!")
        continue
      
      password_hash = str(hashlib.md5(bytes(str(password).encode('utf-8'))).hexdigest())
      
      self.payload = {
        "name": name,
        "email": email,
        "password": password_hash
      }
      
      user_data = self.insert()
      print("Berhasil mendaftarkan akun!")
      break
    
    return user_data
