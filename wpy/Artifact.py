import os
class Artifact(object):
	
	def __init__(self, content):
		self.content = content

	def __str__(self):
		return self.content

	def save(self, directory):
		fileLocation = directory
		if not os.path.isdir(fileLocation):
			 os.makedirs(fileLocation)
		if self.type == "ENDPOINT":
			fileLocation = fileLocation + "/endpoints/"
			if not os.path.isdir(fileLocation):
				os.makedirs(fileLocation)
		if self.type == "PROXY":
			fileLocation = fileLocation + "/proxy-services/"
			if not os.path.isdir(fileLocation):
				os.makedirs(fileLocation)	
		fileLocation = fileLocation + self.name + ".xml"
		fobj = open(fileLocation, 'w')
		fobj.write(self.content)
		fobj.close()

	def setName(self, name):
		self.name = name
	def setType(self, type):
		self.type = type