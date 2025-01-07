import subprocess, os
from pathlib import Path


def main():
    path = os.getcwd() + "/data/DataCleaning.R"
    print(path)
    try:

        subprocess.call(['Rscript',path], shell=False)
        print("cash money")
    except subprocess.CalledProcessError as e:
        print("bruh")

if __name__ == "__main__":
    main()

