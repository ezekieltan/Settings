import json
import os
class Settings:
	def __init__(self, name):
		self.name = name
		self.__readAll__()
		pass
	def write(self,key, value):
		self.contents[key] = value
		self.__flush__()
	def read(self,key):
		if(key in self.contents.keys()):
			return self.contents[key]
		else:
			return None
	def __readAll__(self):
		if(os.path.isfile(self.name)):
			f=open(self.name, "r")
			self.contents = json.loads(f.read())
			f.close()
		else:
			f=open(self.name, "w+")
			f.write('{}')
			f.close()
			self.__readAll__()
	def __flush__(self):
		f=open(self.name, "w")
		f.write(json.dumps(self.contents))
		f.close()