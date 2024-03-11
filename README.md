# Brewdog-Beer-Challenge
Test Automation coding challenge :muscle:
## Pre-requirements 
- Docker
- Python 3.9
- Pip

> :warning **No proxies configuration required**

## Dependencies 
All project dependencies are store in <b>requirement.txt</b> file  

## Installation
### On Docker :
#### Build docker image from project root path:
```bash
docker build --no-cache --progress=plain -t <image_name:tag> <path_to_dockerfile_directory>
```

#### Run docker container from the image:
```bash
docker run -it <image_name:tag>
```
### Locally :
```bash
pip install --no-cache-dir -r requirements.txt
```

## Run automation tests using pytest
#### Using markers :
```bash  
python3 -m pytest --cache-clear --capture=tee-sys -m <marker_name> 
```
Where marker_name has two value: 'api' or 'smoke'. 

#### Using expression :
```bash
python3 -m pytest --cache-clear --capture=tee-sys -k "<marker_name> and <test_method_name>"
```
## Test Report

#### Genrate test report in .html
Run test with --html flag:
```bash
python3 -m pytest --cache-clear --capture=tee-sys --html=<folder_name>/<report_name>.html -m <marker_name> 
```