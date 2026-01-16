class Note:
    def __init__(self,title,id,content):
        self.title = title
        self.id = id
        self.content = content

    def set_json(self):
        return  {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }