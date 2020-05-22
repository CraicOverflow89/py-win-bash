import os, time

# Data Class
class Data:

	def __init__(self, file):
		self.name = file
		self.size = str(os.path.getsize(file))
		self.date = str(time.strftime('%Y %b %d %H:%M', time.localtime(os.path.getmtime(file))))
		def permission_output(it):
			if it["v"]:
				return it["k"]
			return "-"
		self.permission = [
			{"k": "r", "v": os.access(file, os.R_OK)},
			{"k": "w", "v": os.access(file, os.W_OK)},
			{"k": "e", "v": os.access(file, os.X_OK)}
		]
		self.permission = "".join(map(lambda it: permission_output(it), self.permission))

	def to_string(self, size_width):
		return " ".join([self.permission, self.size.rjust(size_width), self.date, self.name])

# Iterate Files
output = []
size_width = 0
for file in os.listdir(os.getcwd()):
	data = Data(file)
	output.append(data)

	# Date Width
	if len(data.size) > size_width:
		size_width = len(data.size)

# Render Output
for file in output:
	print(file.to_string(size_width))