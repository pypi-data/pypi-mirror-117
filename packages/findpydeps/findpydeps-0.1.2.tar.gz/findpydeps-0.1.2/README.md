# findpydeps
Find the python dependencies used by your python files and projects.

## Installation
Simply install it via pip:
```
pip install findpydeps
```

## Usage
For the usage, please refer to the `findpydeps -h` output (or `python3 -m findpydeps -h`)

Example usage:
```
findpydeps -i "/home/$USER/python/example-project/" test.py ../test2.py
```

The output can be redirected to a requirements.txt file, like this:
```
findpydeps -i . > requirements.txt
# or maybe a better alternative :
# findpydeps -i main.py -l
# or (the same) :
# findpydeps --input main.py --follow-local-imports
```
and then use the generated file:
```
python3 -m pip install -r requirements.txt
```
