main.py

1

Not sure what to do? Run some examples (start typing to dismiss)

Line 1 : Col 1

History
Console



Enable "Accessible Terminal" in Workspace Settings to use a screen reader with the console.
Booting ReplReady
Shell
Git
Packager
Secrets
Database
Unit Tests
Settings
main.py
Console
New Tab



Tab Actions

Close Tab
main.py - Python - Replit

Code examples
Get started with some program examples.
Server (Flask)
from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)
Factorial
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))
Hello World
print('Hello World!')
Input
name = input('What is your name?\n')
print('Hi, %s.' % name)
Loop
for i in range(5):
  print('A number:', i)