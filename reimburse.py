#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Reimburse(object):
    def __init__(self):
        self.bills_path = sys.argv[1]
        # pleasure money
        self.pleasure = int(sys.argv[2])
        self.bill_list = []
        self.path = []
        self.cheese = dict()
        with open(self.bills_path) as file:
            for line in file:
                line = line.rstrip()
                try:
                    bill = float(line)
                    self.bill_list.append(bill)
                    self.path.append(0)
                except:
                    print "input bill may be error"
                    sys.exit()
        self.bill_len = len(self.bill_list)
    
    def recursive(self, idx, tot):
        if idx == 0:
            tot = tot + self.bill_list[idx]
            if tot >= self.pleasure:
                self.path[idx] = 1
                self.cheese[tot] = self.path[:]
                return
        else:
            self.path[idx] = 1
            self.recursive(idx - 1, tot + self.bill_list[idx])
            self.path[idx] = 0
            self.recursive(idx - 1, tot)
    
    def output_cheese(self):
        sort = sorted(self.cheese.items(), key=lambda d:d[0])
        f = open('coconut.txt', 'w')
        for k, v in sort:
            out_line = str(k) + " : "
            for i in range(0, self.bill_len):
                if v[i] == 1:
                    out_line = out_line + '\t' + str(self.bill_list[i])
            out_line = out_line + '\n'
            f.write(out_line)
        f.close()

    def find_awesome_path(self):
        self.recursive(self.bill_len - 1, 0)
        self.output_cheese()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: <bills.txt>, <reimburse money>'
        sys.exit()
    reimburse = Reimburse()
    reimburse.find_awesome_path()
