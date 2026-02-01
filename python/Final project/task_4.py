class TextFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"Error: {e}")

    def count_lines(self):
        return len(self.content.splitlines())

    def count_words(self):
        return len(self.content.split())

    def count_characters(self):
        return len(self.content)

    def display_content(self):
        print("File Content:")
        print(self.content)


if __name__ == "__main__":
    reader = TextFileReader("sample.txt")
    reader.read_file()

    print("Number of lines:", reader.count_lines())
    print("Number of words:", reader.count_words())
    print("Number of characters:", reader.count_characters())

    reader.display_content()
