# Configurable-Shell
Build a remote shell with configuration of yours (It doesnt give you actual shell but makes you feel like you have one)

## Working
* Shell is built by stdin and stdout. Take stdin and give stdout. This module is useful during RCE.
```python
from configurable-shell import LinuxShell
```
* To develop a shell define `stdout` yourself. The `stdin` is predefined as keyboard input (you can override that too)
```python
def sample_stdout(self, cmd):
	""" Write RCE Code to send command and return cmd output """
	return output
def sample_stdin(self):
	""" Must return user_input """
	user_input = input("$> ")
	return user_input 

LinuxShell.stdin = sample_stdin #must return user input
LinuxShell.stdout = sample_stdout #pwd should return /home/username
```
* Boom, You got a shell  
```python
rootshell = LinuxShell('root')
rootshell.interact()
root@machine:/root#
```
