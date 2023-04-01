# Revershell
Python Client-Server script to establish a reverse connection between both machines (victim machine, attacker machine).

We will need to run the attacker.py script from the attacking machine, where the user will be asked to insert a command to be sent to the victim machine and be able to execute it thanks to the subprocess library. Then, at the same time, we will receive that output from the victim machine back to our attacking machine with the execution of the corresponding command.

The operation will be as follows, where we will first execute the code from the victim machine so that it remains in listening mode waiting for the command sent by the attacking machine:
