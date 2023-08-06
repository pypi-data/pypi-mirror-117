import argparse
class addone(object):

    number = 0
    def __init__(self, **kw):
        self.number = kw['number']

    def addtest(self):
        print(self.number + 1)

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-number', type=int, help='input number', default=0)
    args = parser.parse_args()
    
    obj = addone(number=args.number)
    obj.addtest()
