## Lesson 11 Homework
# 1.Create your own virtual environment and install some python packages.


PS C:\Users\User\Desktop\PythonHomeworks\Lesson_11> cd path/to/your/project
>> python -m venv venv
>> python3 -m venv venv
>>
cd : Cannot find path 'C:\Users\User\Desktop\PythonHomeworks\Lesson_11\path\to\your\project' because it does not exist.
At line:1 char:1
+ ~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\User\D...to\your\project:String) [Set-Location], ItemNotFoundException   
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand
 
PS C:\Users\User\Desktop\PythonHomeworks\Lesson_11> venv\Scripts\activate
>> pip install flask requests
>>
venv\Scripts\activate : File C:\Users\User\Desktop\PythonHomeworks\Lesson_11\venv\Scripts\Activate.ps1 cannot be loaded because 
running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink 
/?LinkID=135170.
At line:1 char:1
+ venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
Collecting flask
  Downloading flask-3.1.1-py3-none-any.whl.metadata (3.0 kB)
Collecting requests
  Downloading requests-2.32.4-py3-none-any.whl.metadata (4.9 kB)
Collecting blinker>=1.9.0 (from flask)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask)
  Downloading click-8.2.1-py3-none-any.whl.metadata (2.5 kB)
Collecting itsdangerous>=2.2.0 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask)
  Downloading MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl.metadata (4.1 kB)
Collecting werkzeug>=3.1.0 (from flask)
  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.4.2-cp312-cp312-win_amd64.whl.metadata (36 kB)
Collecting idna<4,>=2.5 (from requests)
  Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Downloading urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests)
  Downloading certifi-2025.7.14-py3-none-any.whl.metadata (2.4 kB)
Requirement already satisfied: colorama in c:\users\user\appdata\roaming\python\python312\site-packages (from click>=8.1.3->flask) (0.4.6)
Downloading flask-3.1.1-py3-none-any.whl (103 kB)
Downloading requests-2.32.4-py3-none-any.whl (64 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading certifi-2025.7.14-py3-none-any.whl (162 kB)
Downloading charset_normalizer-3.4.2-cp312-cp312-win_amd64.whl (105 kB)
Downloading click-8.2.1-py3-none-any.whl (102 kB)
Downloading idna-3.10-py3-none-any.whl (70 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl (15 kB)
Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
Installing collected packages: urllib3, markupsafe, itsdangerous, idna, click, charset_normalizer, certifi, blinker, werkzeug, reSuccessfully installed blinker-1.9.0 certifi-2025.7.14 charset_normalizer-3.4.2 click-8.2.1 flask-3.1.1 idna-3.10 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.2 requests-2.32.4 urllib3-2.5.0 werkzeug-3.1.3

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip
PS C:\Users\User\Desktop\PythonHomeworks\Lesson_11> pip list
>>
Package                 Version
----------------------- -----------
asttokens               3.0.0
blinker                 1.9.0
certifi                 2025.7.14
charset-normalizer      3.4.2
click                   8.2.1
colorama                0.4.6
comm                    0.2.2
debugpy                 1.8.14
decorator               5.2.1
executing               2.2.0
Flask                   3.1.1
idna                    3.10
ipykernel               6.29.5
ipython                 9.3.0
ipython_pygments_lexers 1.1.1
itsdangerous            2.2.0
jedi                    0.19.2
Jinja2                  3.1.6
jupyter_client          8.6.3
jupyter_core            5.8.1
MarkupSafe              3.0.2
matplotlib-inline       0.1.7
nest-asyncio            1.6.0
packaging               25.0
parso                   0.8.4
pip                     25.0.1
platformdirs            4.3.8
prompt_toolkit          3.0.51
psutil                  7.0.0
pure_eval               0.2.3
Pygments                2.19.1
python-dateutil         2.9.0.post0
pywin32                 310
pyzmq                   26.4.0
requests                2.32.4
six                     1.17.0
tornado                 6.5.1
traitlets               5.14.3
urllib3                 2.5.0
wcwidth                 0.2.13
Werkzeug                3.1.3
PS C:\Users\User\Desktop\PythonHomeworks\Lesson_11> deactivate
>> 
deactivate : The term 'deactivate' is not recognized as the name of a cmdlet, function, script file, or operable program. Check 
the spelling of the name, or if a path was included, verify that the path is correct and try again.
+ deactivate
+ ~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (deactivate:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\User\Desktop\PythonHomeworks\Lesson_11> project_folder/venv/bin/python
>> 
project_folder/venv/bin/python : The term 'project_folder/venv/bin/python' is not recognized as the name of a cmdlet, function, 
script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and 
At line:1 char:1
+ project_folder/venv/bin/python
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (project_folder/venv/bin/python:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\User\Desktop\PythonHomeworks\Lesson_11>
# 2.Create custom modules.
# Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
# Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)




import math_operations
import string_utils

# Using math_operations
print("Add:", math_operations.add(10, 5))
print("Subtract:", math_operations.subtract(10, 5))
print("Multiply:", math_operations.multiply(10, 5))
print("Divide:", math_operations.divide(10, 0))

# Using string_utils
text = "Hello World"
print("Reversed:", string_utils.reverse_string(text))
print("Vowel Count:", string_utils.count_vowels(text))


# 3. Create custom packages.
# Create geometry package.
#  geometry\
#      __init__.py
#      circle.py
#  
# Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
# Create file_operations package.
#  file_operations\
#      __init__.py
#      file_reader.py
#      file_writer.py
#  
# Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).


import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            return "Content written successfully."
    except Exception as e:
        return f"Error: {str(e)}"


from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file


radius = 5
print("Area:", calculate_area(radius))
print("Circumference:", calculate_circumference(radius))

file_path = "sample.txt"
content = "Hello from custom packages!"

print(write_file(file_path, content))
print("File content:", read_file(file_path))
