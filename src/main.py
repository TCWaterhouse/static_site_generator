import shutil
import os

def copy_dir(source, target):
    # Clear target directory
    shutil.rmtree(target)

def main():
    copy_dir("static/", "public/")
    
if __name__ == "__main__":
    main()