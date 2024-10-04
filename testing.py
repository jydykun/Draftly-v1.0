import os
import shutil



print(os.getcwd())

os.chdir(os.pardir)

print(os.getcwd())

os.mkdir("testing")
