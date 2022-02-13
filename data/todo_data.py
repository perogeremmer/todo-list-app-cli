import datetime


todo_data = []


class TodoData:
    def __init__(self):
        self.todo_data = todo_data
        self.payload = {}

    def validate(self, payload):
        if 'title' not in payload or not payload['title']:
            raise Exception("You should fill title")

        if 'description' not in payload or not payload['description']:
            raise Exception("You should fill description")

    def clear(self):
        self.payload = {}

    def get(self, id=None):
        if not id:
            return self.user_data

        value = []
        for item in self.user_data:
            if item['id'] == id:
                value = item
                break

        return value

    def insert(self):
        self.validate(self.payload)

        length = len(self.payload)
        self.payload['id'] = (length + 1)

        self.user_data.append(self.payload)
        data = self.payload.copy()

        self.clear()
        return data

    def update(self, id):
        self.validate(self.payload)

        for item in self.user_data:
            if item['id'] == id:
                item.update(self.payload)
                break

        self.clear()
        
    def finish(self, id):
        for item in self.user_data:
            if item['id'] == id:
                item['finished_at'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                break

        return True

    def delete(self, id):
        index = 0

        for idx, item in self.user_data:
            if item['id'] == id:
                index = idx
                break

        self.todo_data.pop(index)
        self.clear()
