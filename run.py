import argparse
import wpy

generator = wpy.ArtifactGenerator()
data = {
		    'name' : "id",
		    'type' : "http",
		    'http' : True,
		    'http_props': {
		        'uri': "/.id",
		        'method': "HEAD GET"
		    }
		}
artifact = generator.generateEndpoint(data)
artifact.setName(data["name"])
artifact.setType("ENDPOINT")
generator.hold(artifact)

data = {
		    'name' : "appcheck",
		    'type' : "address",
		    'address' : True,
		    'address_props': {
		        'uri': "/.id",
		        'method': "HEAD GET",
		        'format': "soap11",
		        'traceFlag': "true"
		    }
		}

artifact = generator.generateEndpoint(data)
artifact.setName(data["name"])
artifact.setType("ENDPOINT")
generator.hold(artifact)

data = {
		    'name' : "appcheck",
		    'startOnLoad' : "address",
		    'traceFlag' : "false",
		    'transports' : "http https",
		    'faultSequence' : "dev_error",
		    'endpointName' : "DSCIN_ENDPOINT",
		    'inSequenceKey': "dev_in"
		}
artifact = generator.generateProxy(data)
artifact.setName(data["name"])
artifact.setType("PROXY")
generator.hold(artifact)

data = {
	'parentGroupId' : "com.example.esb",
	'parentArtifactId' : "gateway",
	'parentVersion' : "1.0.0",
	'groupId' : "com.example.esb",
	'artifactId' : "gateway-car",
	'version' : "1.0.0",
	'name' : "gateway-car",
	'description' : "gateway-car",
	'serverRole' : "EnterpriseServiceBus",
	'resourceVersion' : "1.0.0",
	'resourceFileType' : "xml"
}
directory = "configs"

artifactTu = generator.generateArtifact(data, directory)

artifact = artifactTu
artifact.setName("artifact")
artifact.setType("POM")
generator.hold(artifact)

artifactTu = generator.generateCarPom(data, directory)
artifact = artifactTu
artifact.setName("pom")
artifact.setType("POM")
generator.hold(artifact)


generator.saveList("configs")

