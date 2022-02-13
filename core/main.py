from os import system
from core.todo import Todo
from core.user import User

class Main:
    def __init__(self):
        self.user = User()

    def run(self):
        user_data = None
        
        while True:
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            print("----------------\n")
            pilihan = int(input("Masukkan pilihan anda: "))
            if pilihan == 1:
                data = self.user.login()
                if not data:
                    system.exit(1)
                user_data = data
                
                break
            elif pilihan == 2:
                self.user.register()
                continue
            elif pilihan == 3:
                print("Keluar dari sistem")
                system.exit(1)
            else:
                print("Pilihan tidak tersedia")
                
        print("----------------\n")
        print(f"Hello, {user_data['name']}. Selamat datang di aplikasi todo!")
        print("----------------\n")
        
        todo = Todo()
        
        while True:
            print("1. Lihat Todo")
            print("2. Tambah Todo")
            print("3. Ubah Todo")
            print("4. Hapus Todo")
            print("5. Logout")
            print("----------------\n")
            pilihan = int(input("Masukkan pilihan anda: "))
            if pilihan == 1:
                data = self.user.login()
                if not data:
                    system.exit(1)
                user_data = data
                
                break
            elif pilihan == 2:
                self.user.register()
                continue
            elif pilihan == 5:
                print("Keluar dari sistem")
                system.exit(1)
            else:
                print("Pilihan tidak tersedia")