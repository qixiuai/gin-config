
import pdb

from collections import namedtuple

from absl import app


def main(argv):
    del argv
    t = namedtuple("A", ['a', 'b'])
    
    s = "test"
    print(s[-2:])
    

if __name__ == '__main__':
    app.run(main)
    
