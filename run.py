import argparse
import wpy
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print args.accumulate(args.integers)


#, helpers=helpers, partials=partials

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
		    'faultSequence' : "pru_error",
		    'endpointName' : "DSC_USBCE_DAM_CALLBACK_DEV_IN_ENDPOINT",
		    'inSequenceKey': "pru_in"
		}
artifact = generator.generateProxy(data)
artifact.setName(data["name"])
artifact.setType("PROXY")
generator.hold(artifact)


# print(artifact)

data = {
	'parentGroupId' : "com.pru.esb",
	'parentArtifactId' : "ewsg",
	'parentVersion' : "1.0.0",
	'groupId' : "com.pru.esb",
	'artifactId' : "ewsg-car",
	'version' : "1.0.0",
	'name' : "ewsg-car",
	'description' : "ewsg-car"
}
directory = "/Users/chan/Development/WSO2/wso2-scratch/prudential-dev-service/pru-work/generated"

artifactTu = generator.generateCarPom(data, directory)
artifact = artifactTu[0]
artifact.setName("pom")
artifact.setType("POM")
generator.hold(artifact)

artifact = artifactTu[1]
artifact.setName("artifact")
artifact.setType("POM")
generator.hold(artifact)


generator.saveList("configs")

