# Strace is your friend

This project aims to help you find out why Apache is returning a 500 error using strace. Once the issue is found, it should be fixed and automated using Puppet instead of Bash.


## Instructions

1. Use strace to attach to a current running process.
2. Use tmux to run strace in one window and curl in another one.
3. Find the issue causing Apache to return a 500 error.
4. Fix the issue.
5. Automate the fix using Puppet.

## Hint

