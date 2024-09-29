import os
from zipfile import ZipFile
import sys

def uniq(lines):
  UniqLines = set()
  for line in lines:
    UniqLines.add(line)
  for ans in UniqLines:
    print(ans)

username = "Root"
dirname = ""
FileText = ""
with ZipFile('files.zip', 'a') as myzip:

  while True:
    command = input('~' + dirname + '# ')
    if command == 'ls':
      if dirname == "":
        for name in myzip.namelist():
          print(name)
      else:
          for name in myzip.namelist():
            if name.startswith(dirname):
                print(name.split("/")[-1])



    elif command == "exit":
      exit(0)
    elif command.startswith('cd'):
      if len(command) == 2:
        dirname = ""
      else:
        ndir = command.split(" ")[1]
        if ndir in myzip.namelist():
          dirname = ndir
        else:
          print("sh: cd: can't cd to " + ndir + ": No such file or directory")

    elif command == "clear":
      print(100 * '\n')

    elif command == "whoami":
      print(username)

    elif command.startswith('uniq'):
      if len(command) == 4:
        FileText = ""
      else:
        FText = command.split(" ")[1]
        if (dirname + FText) in myzip.namelist():
          FileText = (dirname + FText)
          try:
            if FileText[-4:] == ".txt":
              with myzip.open(FileText) as file_obj:
                lines = file_obj.read().decode('utf-8').splitlines()
                uniq(lines)
            else:
              print(f"Файл {FText} не найден в архиве files.zip")
          except KeyError:
            print(f"Файл {FText} не найден в архиве files.zip")
        else:
          print(f"Файл {FText} не найден в архиве files.zip")
    else:
      print("Command not found.")


