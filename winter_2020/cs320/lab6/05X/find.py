#!/usr/bin/env python3
#

import sys
import os
import shutil


def find(root, filename):
    found = []
    for root, dirs, files in os.walk(root):
        # to test os.walk()
        ''' 
        print("Root: ", root)
        print(" dir: ", dirs)
        print(" file: ", files)
        '''
        for each_file in files:
            if each_file == filename:
                found.append(os.path.join(root,each_file))
    return found


def copy(found, new_dir):
    path = os.getcwd()
    path = path + "/" + new_dir
    access_rights = 0o755
    os.mkdir(path , access_rights)
    for each_file in found:
        file_name = each_file.replace('/', '', 1)
        file_name = file_name.replace('/', '_')
        shutil.copyfile(each_file, path + '/' + file_name)




def root_error():
    print ("root_error: input root does not exist")
    exit(0)


def usage():
  print ('usage: ./find.py [--copy dirname] root file')
  exit(0)

def main():
  if len(sys.argv) < 2: usage()
  if sys.argv[1] == '--copy':
     if len(sys.argv) < 5: usage()
     new_dir = sys.argv[2]
     root = sys.argv[3]
     filename = sys.argv[4]
     if not os.path.isdir(root): root_error()
     found = find(root,filename)
     for f in found:
       print(f)
     copy(found,new_dir)
  else:
     if len(sys.argv) < 3: usage()
     root = sys.argv[1]     
     filename = sys.argv[2]
     found = find(root,filename)
     for f in found:
       print(f)

if __name__ == '__main__':
  main()
