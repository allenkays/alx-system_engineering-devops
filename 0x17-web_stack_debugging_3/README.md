# 0x17. Web stack debugging #3
Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

Hint:

    - strace can attach to a current running process
    - use tmux to run strace in one window and curl in another one

Requirements:

    - 0-strace_is_your_friend.pp file contains Puppet code
