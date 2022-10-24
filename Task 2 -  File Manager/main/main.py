import sys

import commands as cmd

while True:
    command = input().split(' ')

    match command[0]:
        case "pwd":
            cmd.pwd()
        case "cd":
            cmd.cd(command[1])
        case "touch":
            cmd.touch(command[1])
        case "cat":
            cmd.cat(command[1])
        case "ls":
            cmd.ls()
        case "rm":
            cmd.rm(command[1])
        case "exit":
            sys.exit(0)
