# Data preparation:
import csv
import sys
from sets import Set


# Define a connection graph:
def updateGraph(usr1, usr2):
    if usr1 not in graph:
        graph[usr1] = Set([usr2])
    else:
        graph[usr1].add(usr2)
    if usr2 not in graph:
        graph[usr2] = Set([usr1])
    else:
        graph[usr2].add(usr1)


def constructLargerGraph():
    for usr in graph:
        largerGraph[usr] = Set([])
        friends = graph[usr]
        largerGraph[usr] = largerGraph[usr].union(friends)
        for friend in friends:
            largerGraph[usr] = largerGraph[usr].union(graph[friend])


# Feature 1: only need to check if id1 and id2 had connection before:
def isConnectOnF1(usr1, usr2):
    return (usr1 in graph and usr2 in graph[usr1]) or (usr2 in graph and usr1 in graph[usr2])


def isConnectOnF2(usr1, usr2):
    if usr1 not in graph or usr2 not in graph:
        return False
    else:
        if usr1 in graph[usr2]:
            return True
        elif len(graph[usr1].intersection(graph[usr2])) > 0:
            return True
        return False


def isConnectOnF3(usr1, usr2):
    if usr1 not in largerGraph or usr2 not in largerGraph:
        return False
    else:
        if usr1 in largerGraph[usr2] or usr2 in largerGraph[usr1]:
            return True
        elif len(largerGraph[usr1].intersection(largerGraph[usr2])) > 0:
            return True
        return False

train_path = sys.argv[1]
test_path = sys.argv[2]
output1_path = sys.argv[3]
output2_path = sys.argv[4]
output3_path = sys.argv[5]
f_train = open(train_path, 'rU')
f_test = open(test_path, 'rU')
f_output1 = open(output1_path, 'w')
f_output2 = open(output2_path, 'w')
f_output3 = open(output3_path, 'w')

# Construct graph
reader = csv.reader(f_train)
reader.next()
graph = {}
largerGraph = {}
for row in reader:
    if len(row) < 4:
        continue
    id1 = row[1]
    id2 = row[2]
    updateGraph(id1, id2)

# Construct larger graph for fast detection
constructLargerGraph()
print "Finish training"

# Read stream data
reader = csv.reader(f_test)
reader.next()
for row in reader:
    if len(row) < 4:
        continue
    id1 = row[1]
    id2 = row[2]
    # Feature 1
    if not isConnectOnF1(id1, id2):
        f_output1.write("unverified\n")
    else:
        f_output1.write("trusted\n")
    # Feature 2
    if not isConnectOnF2(id1, id2):
        f_output2.write("unverified\n")
    else:
        f_output2.write("trusted\n")
    # Feature 3
    if not isConnectOnF3(id1, id2):
        f_output3.write("unverified\n")
    else:
        f_output3.write("trusted\n")
    updateGraph(id1, id2)

f_output1.close()
f_output2.close()
f_output3.close()

