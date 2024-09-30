import argparse
import fileinput

parser = argparse.ArgumentParser("Subset to paths with at least one node "
                                 "within provided range")
parser.add_argument('-p', help='node interval as provided to tabix, i.e. '
                    'in the form {n}:node-NODE')
args = parser.parse_args()

argsp = args.p.split(':')[1].split('-')
min_node = int(argsp[0])
max_node = int(argsp[1])

for line in fileinput.input(files='-'):
    line = line.rstrip()
    path = line.split('\t')[5]
    path = path.replace('>', '<').split('<')[1:]
    for node in path:
        if int(node) <= max_node and int(node) >= min_node:
            print(line)
            break
