import hashlib
from data.todo_data import TodoData


class Todo(TodoData):
    def __init__(self, user_id):
        self.user_id = user_id
        
    def create_todo(self):
        todo_data = None

        while True:
            title = input("Silahkan masukkan judul todo: ").strip()
            description = input("Silahkan masukkan deskripsi todo: ").strip()

            self.payload = {
                "title": title,
                "description": description,
                "user_id": self.user_id,
                "finished_at": None
            }

            todo_data = self.insert()
            print("Berhasil mendaftarkan akun!")
            break

        return todo_data
    
    def update_todo(self):
        todo_data = None

        while True:
            todo_id = int(input("Silahkan masukkan id todo: "))
            
            data = self.get(todo_id)
            
            if not data:
                print("Todo tidak ditemukan!")
                return None
            
            print(f"{data['title']} - {data['description']}")
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
            break

        return todo_data
    
    def finish_todo(self):
        todo_data = None

        while True:
            todo_id = int(input("Silahkan masukkan id todo: "))
            
            data = self.get(todo_id)
            
            if not data:
                print("Todo tidak ditemukan!")
                return None

            todo_data = self.finish(todo_id)
            print("Berhasil menyelesaikan todo!")
            break

        return todo_data
    
    def delete_todo(self):
        todo_data = None

        while True:
            todo_id = int(input("Silahkan masukkan id todo: "))
            
            data = self.get(todo_id)
            
            if not data:
                print("Todo tidak ditemukan!")
                return None

            todo_data = self.delete(todo_id)
            print("Berhasil menyelesaikan todo!")
            break

        return todo_data
