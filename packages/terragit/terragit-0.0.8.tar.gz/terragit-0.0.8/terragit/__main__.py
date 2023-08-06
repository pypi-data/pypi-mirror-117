import sys
from terragit.changes import *
def main():
    if sys.argv[1] =="changes":
        print(sys.argv[1])
        mr_changes()

if __name__ == '__main__':
    main()
