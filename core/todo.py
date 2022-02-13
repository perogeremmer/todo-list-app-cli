from time import sleep
from data.todo_data import TodoData


class Todo(TodoData):
    def __init__(self, user_id):
        super(Todo, self).__init__()
        self.user_id = user_id
        
    def get_todo(self):
        data = self.get(self.user_id)
        
        if len(data) < 1:
            print("\nKamu belum memiliki todo!\n")
            sleep(2)
            return False
        
        print("Daftar todo: ")
        print("-------------------------------")
        for item in data:
            status = "Belum selesai" if not item['finished_at'] else "Sudah selesai"
            
            print(f"ID: {item['id']}")
            print(f"Title: {item['title']}")
            print(f"Description: {item['description']}")
            print(f"Status: {status}")
            print(f"---------------------------")
        
        sleep(5)
        input("Tekan enter untuk kembali ke menu utama")
        return True
        
    def create_todo(self):
        todo_data = None
        add_todo = True
        
        while add_todo:
            title = input("Silahkan masukkan judul todo: ").strip()
            description = input("Silahkan masukkan deskripsi todo: ").strip()

            self.payload = {
                "title": title,
                "description": description,
                "user_id": self.user_id,
                "finished_at": None
            }

            todo_data = self.insert()
            print("Berhasil menambahkan todo!")
            sleep(1)
            
            while True:
                option = input("Ingin menambahkan todo lagi? (y/n): ").strip()
                option.replace(" ", "")
                
                if option not in ["y", "n"]:
                    print("Masukkan pilihan yang benar! (y/n)")
                    continue
                
                if option == "n":
                    add_todo = False
                    
                break

        return todo_data
    
    def update_todo(self):
        todo_data = None

        while True:
            todo_id = int(input("Silahkan masukkan id todo: "))
            
            data = self.get(user_id=self.user_id, id=todo_id)
            
            if not data:
                print("Todo tidak ditemukan!")
                return
            
            if self.user_id != data['user_id']:
                print("Todo tidak ditemukan!")
                return
            
            print(f"{data['title']} - {data['description']}\n")
            title = input("Silahkan masukkan judul todo (Kosongkan jika tidak ingin melakukan perubahan): ").strip()
            description = input("Silahkan masukkan deskripsi todo (Kosongkan jika tidak ingin melakukan perubahan): ").strip()
            
            if not title:
                title = data['title']
                
            if not description:
                description = data['description']

            self.payload = {
                "title": title,
                "description": description
            }

            todo_data = self.update(todo_id)
            print("Berhasil mengubah todo!")
            sleep(4)
            break

        return todo_data
    
    def finish_todo(self):
        todo_data = None

        while True:
            todo_id = int(input("Silahkan masukkan id todo: "))
            
            data = self.get(user_id=self.user_id, id=todo_id)
            
            if not data:
                print("Todo tidak ditemukan!")
                sleep(4)
                return None

            todo_data = self.finish(todo_id)
            print("Berhasil menyelesaikan todo!")
            sleep(4)
            break

        return todo_data
    
    def delete_todo(self):
        todo_data = None

        while True:
            todo_id = int(input("Silahkan masukkan id todo: "))
            
            data = self.get(user_id=self.user_id, id=todo_id)
            
            if not data:
                print("Todo tidak ditemukan!")
                sleep(4)
                return

            self.delete(todo_id)
            
            todo_data = True
            print("Berhasil menghapus todo!")
            sleep(4)
            break

        return todo_data
