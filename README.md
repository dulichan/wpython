# W-python

WSO2 Python generation utilties

## Installation

Clone the github project and symlink the run.sh

## Features

1. Generate ESB endpoint artifacts
2. Generate ESB proxy artifacts
3. Generate CAR pom for ESB project
4. Generate the artifact.xml for synapse-project

## Usage

Use `ArtifactGenerator` to generate the artifacts needed.

```python
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
```
Use Generator to save the artifacts. The artifacts will be stored in configs folder. 

```python
artifact.setName(data["name"])
artifact.setType("ENDPOINT")
generator.hold(artifact)
generator.saveList("configs")

```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D



## License

WTFPL
