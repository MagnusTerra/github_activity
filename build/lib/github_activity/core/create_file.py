class CreateFile:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def create(self):
        try:
            with open(self.filename, "w") as f:
                f.write(self.content)
            print(f"File {self.filename} created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")
    