import os, struct, time
from typing import List


class Data:
    """
    File data to render in output
    """

    def __init__(self, file):
        self.name = file
        self.size = str(os.path.getsize(file))
        self.date = str(
            time.strftime("%Y %b %d %H:%M", time.localtime(os.path.getmtime(file)))
        )

        def permission_output(it):
            if it[1]:
                return it[0]
            return "-"

        self.permission = [
            ("r", os.access(file, os.R_OK)),
            ("w", os.access(file, os.W_OK)),
            ("e", os.access(file, os.X_OK)),
        ]
        self.permission = "".join(
            map(lambda it: permission_output(it), self.permission)
        )

        # Link Location
        if self.name[-4:] == ".lnk":
            self.name += " -> " + self.link_location(file)

    def link_location(self, path):
        """
        Determines the target of a Windows shortcut file
        :param path: the location of the shortcut
        :returns: shortcut location
        """
        result = ""
        with open(path, "rb") as stream:
            content = stream.read()
            lflags = struct.unpack("I", content[0x14:0x18])[0]
            position = 0x18
            if (lflags & 0x01) == 1:
                position = struct.unpack("H", content[0x4C:0x4E])[0] + 0x4E
            last_pos = position
            position += 0x04
            length = struct.unpack("I", content[last_pos:position])[0]
            position += 0x0C
            position = (
                last_pos + struct.unpack("I", content[position : position + 0x04])[0]
            )
            size = (length + last_pos) - position - 0x02
            temp = struct.unpack("c" * size, content[position : position + size])
            result = "".join([chr(ord(a)) for a in temp])
        return result

    def to_string(self, size_width):
        """
        Renders file data as a string
        :param size_width: width of size column
        :returns: string to print
        """
        return " ".join(
            [self.permission, self.size.rjust(size_width), self.date, self.name]
        )


# Iterate Files
output: List[Data] = []
size_width: int = 0
for file in os.listdir(os.getcwd()):
    data = Data(file)
    output.append(data)

    # Data Width
    if len(data.size) > size_width:
        size_width = len(data.size)

# Render Output
for file in output:  # type: ignore
    print(file.to_string(size_width))  # type: ignore
