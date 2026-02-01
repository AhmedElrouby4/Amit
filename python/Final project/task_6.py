def read_txt_file(file_path):
    """Reads the contents of a text file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except IOError:
        return "Error: An error occurred while reading the file."


class UserExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.usernames = {}

    def extract_usernames(self):
        content = read_txt_file(self.file_path)

        # Check if an error message was returned
        if content.startswith("Error"):
            return content

        lines = content.splitlines()

        for line in lines:
            if ":" in line:
                username, _ = line.split(":", 1)
                self.usernames[username] = True

        return self.usernames


# Usage example
if __name__ == "__main__":
    extractor = UserExtractor("test.txt")
    result = extractor.extract_usernames()

    print(result)
