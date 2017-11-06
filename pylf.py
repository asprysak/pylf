"""
A simple script wrapper which augments the original script's logging.
Originally prepared for logging out some verbose and useless TensorFlow logs.

I should probably add some configuration options and create a project out of this...
... and maybe add some nice progress bar.
"""

import colorful
import subprocess
import os


def main():
    os.environ['PYTHONUNBUFFERED'] = '1'
    process = subprocess.Popen(['python3', 'infiloop.py'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True,
                               bufsize=1)
    while process.poll() is None:
        line = process.stdout.readline()
        if line:
            if '-=>' in line:  # Assume sophisticated pattern
                print(colorful.bold_green(line.strip()))
            else:
                print(line.strip())
        line = process.stderr.readline()
        if line:
            print(colorful.red(line.strip()))


if __name__ == '__main__':
    main()
