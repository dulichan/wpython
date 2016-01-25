from pybars import Compiler
import lxml.etree as etree
import collections
from . import Artifact
import os
class ArtifactGenerator(object):
	"""Class used to generate artifacts for WSO2"""
	def __init__(self):
		self.artifactList = []
		pass
	"""Generate the artifact based on the passed template location and data"""
	def generate(self, data, templateLocation):
		compiler = Compiler()
		
		source = open(templateLocation).read().decode('utf-8')
		template = compiler.compile(source)

		output = template(data)
		parser = etree.XMLParser(remove_blank_text=True)
		root = etree.XML(output, parser)
		xml_output = etree.tostring(root, pretty_print = True, xml_declaration = True, encoding='UTF-8')
		artifactObj = Artifact(xml_output)
		return artifactObj

	def merge(self, a, b, path=None):
	    "deep merge dictionary"
	    if path is None: path = []
	    for key in b:
	        if key in a:
	            if isinstance(a[key], dict) and isinstance(b[key], dict):
	                self.merge(a[key], b[key], path + [str(key)])
	            elif a[key] == b[key]:
	                pass # same leaf value
	            else:
	                #raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
	                pass
	        else:
	            a[key] = b[key]
	    return a

	def generateEndpoint(self, data):
		if data["type"]=="address":
			defaultData = {
			    'address_props': {
			        'statistics': "false",
			        'traceFlag': "false"
			    }
			}
			data = self.merge(data, defaultData)
		artifactObj = self.generate(data, "templates/endpoint.hbs")
		return artifactObj

	def generateProxy(self, data):
		artifactObj = self.generate(data, "templates/proxy.hbs")
		return artifactObj

	def get_filepaths(self, directory, function):
	    """
	    This function will generate the file names in a directory 
	    tree by walking the tree either top-down or bottom-up. For each 
	    directory in the tree rooted at directory top (including top itself), 
	    it yields a 3-tuple (dirpath, dirnames, filenames).
	    """
	    file_paths = []  # List which will store all of the full filepaths.

	    # Walk the tree.
	    for root, directories, files in os.walk(directory):
	        for filename in files:
	            # Join the two strings in order to form the full filepath.
	            filepath = os.path.join(root, filename)
	            file_paths = function(filepath, filename, file_paths)
	             # Add it to the list.

	    return file_paths  # Self-explanatory.

	def generateArtifact(self, data, directory):
		def generateCarPom(self, data, directory):
		""" Pass in the generic parameters for the pom file. The method will read the synapse
		directory and create the resources dictionary """
		
		synapse_directory = directory
		
		def synapse_config(filepath, filename, file_paths):
			typeName = filepath.split("/")
			# print typeName
			#if typeName[13]=="synapse-config":
			#	if len(typeName) == 16:
			#		typeName = typeName[14]
			#		typeName = typeName[:-1]
			#		file_paths.append({'filePath': filepath, 'fileName': filename, 'type': typeName}) 
			if typeName[8]=="generated":
				if len(typeName) == 11:
					typeName = typeName[9]
					typeName = typeName[:-1]
					file_paths.append({'filePath': filepath, 'fileName': filename, 'type': typeName}) 
			return file_paths
		fileList = self.get_filepaths(synapse_directory, synapse_config)
		# print fileList
		resources = []
		for fileObj in fileList:
			resources.append({'type': fileObj['type'], 'resourceName': fileObj['fileName'].split(".")[0], 'serverRole': "EnterpriseServiceBus", 'resourceVersion': "1.0.0", 'resourceFileType': "xml"})
		#print resources
		data['resources'] = resources
		print data
		artifactCarObj = self.generate(data, "templates/car_pom.hbs")
		artifactArtiObj = self.generate(data, "templates/artifact.hbs")
		return [artifactCarObj, artifactArtiObj]
		#registry_directory = directory + "/ewsg-registry/"
		#def registry_config(filepath, filename, file_paths):
			#typeName = filepath.split("/")
			#print typeName
			# if typeName[13]=="synapse-config":
			# 	if len(typeName) == 16:
			# 		typeName = typeName[14]
			# 		file_paths.append({'filePath': filepath, 'fileName': filename, 'type': typeName}) 
		
			#return file_paths
		#fileList = self.get_filepaths(registry_directory, registry_config)

	def generateCarPom(self, data, directory):
		""" Pass in the generic parameters for the pom file. The method will read the synapse
		directory and create the resources dictionary """
		
		synapse_directory = directory
		
		def synapse_config(filepath, filename, file_paths):
			typeName = filepath.split("/")
			# print typeName
			#if typeName[13]=="synapse-config":
			#	if len(typeName) == 16:
			#		typeName = typeName[14]
			#		typeName = typeName[:-1]
			#		file_paths.append({'filePath': filepath, 'fileName': filename, 'type': typeName}) 
			return file_paths
		fileList = self.get_filepaths(synapse_directory, synapse_config)
		# print fileList
		resources = []
		for fileObj in fileList:
			resources.append({'type': fileObj['type'], 'resourceName': fileObj['fileName'].split(".")[0], 'serverRole': "EnterpriseServiceBus", 'resourceVersion': "1.0.0", 'resourceFileType': "xml"})
		#print resources
		data['resources'] = resources
		print data
		artifactCarObj = self.generate(data, "templates/car_pom.hbs")
		artifactArtiObj = self.generate(data, "templates/artifact.hbs")
		return [artifactCarObj, artifactArtiObj]
		#registry_directory = directory + "/ewsg-registry/"
		#def registry_config(filepath, filename, file_paths):
			#typeName = filepath.split("/")
			#print typeName
			# if typeName[13]=="synapse-config":
			# 	if len(typeName) == 16:
			# 		typeName = typeName[14]
			# 		file_paths.append({'filePath': filepath, 'fileName': filename, 'type': typeName}) 
		
			#return file_paths
		#fileList = self.get_filepaths(registry_directory, registry_config)

	def hold(self, artifact):
		self.artifactList.append(artifact)

	def saveList(self, location):
		for (artifact) in self.artifactList:
			artifact.save(location)