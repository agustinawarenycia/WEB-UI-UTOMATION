import argparse
import subprocess

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    # --testdir command line argument added
    p.add_argument('--testdir', required=False, help="File path")
    a = p.parse_args()
    testdir = a.testdir
    # complete command
    c = f'behave -f html -o report/report.html  {testdir}'
    s = subprocess.run(c, shell=True, check=True)
