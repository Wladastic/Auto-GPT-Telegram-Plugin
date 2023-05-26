class LocalCommands:

    def create_file(self, file_name: str, content: str = "") -> None:
        with open(file_name, "w") as file:
            file.write(content)

    def edit_code(self, file_name: str, new_content: str) -> None:
        with open(file_name, "w") as file:
            file.write(new_content)

    def edit_specific_line(self, file_name: str, line_number: int, new_content: str) -> None:
        with open(file_name, "r") as file:
            lines = file.readlines()

        lines[line_number - 1] = new_content + "\n"

        with open(file_name, "w") as file:
            file.writelines(lines)