class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

if __name__ == "__main__":
    with FileManager("example.txt", 'w') as file:
        file.write("Hello, this is a test.")



    with open("example.txt", 'r') as file:
        content = file.read()
        print("File content:", content)

