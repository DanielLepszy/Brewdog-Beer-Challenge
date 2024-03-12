# Brewdog-Beer-Challenge
Test Automation coding challenge :muscle:
## Pre-requirements 
- Docker
- Python 3.9
- Pip

> :warning: **No proxies configuration required**

## Dependencies 
All project dependencies are store in <b>requirement.txt</b> file  

## Installation
### On Docker :
#### Build docker image from project root path:
```bash
docker build --no-cache --progress=plain -t <image_name:tag> .
```
During image build, all packages and dependencies are installed as well.  

#### Run docker container from the image:
```bash
docker run -it <image_name:tag>
```
### Locally (Optional) :
In case any dependencies issue, please reinstall packages again:
```bash
pip install --no-cache-dir -r requirements.txt
```

## Run automation tests using pytest from /app path
#### Using markers :
```bash  
python3 -m pytest --cache-clear -s  -m <marker_name> 
```
Where marker_name is : 'api' or 'smoke' or 'additional' 

#### Using expression :
```bash
python3 -m pytest --cache-clear -s  -k "<marker_name> and <test_method_name>"
```
## Test Report

#### Genrate test reports
In pytest.ini you can find simple configuration for pytest report. To long story short, you do not need to attach any additional flags to generate test report. Run tests suite using previous commands and the test report will be generated automatically in pytest-report.txt file.

To preview report, please use 'cat' method :
```bash
cat pytest-report.txt 
```

To output test report in console:
- disallow 'md_report_output' flag in pytest.ini  
- keep 'md-report' and 'md-report-verbose=1' flags attached in pytest.ini 

> Alternatively, I provided another report in .html. Please attach ' --html=report.html ' flag to your pytest commads.