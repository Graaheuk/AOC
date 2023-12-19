import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.read().rstrip().split('\n\n')
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

def isAccepted(part, workflow):
    step = 'in'
    while step != 'A' or step != 'R':
        for i in range(len(workflow[step])):
            if not ':' in workflow[step][i]:
                step = workflow[step][i]
                break
            else:
                splited = workflow[step][i].split(':')
                if '<' in workflow[step][i]:
                    if workflow[step][i][0] == 'x' and part[0] < int(splited[0][2:]):
                        step = splited[1]
                        break
                    if workflow[step][i][0]=='m' and part[1] < int(splited[0][2:]):
                        step = splited[1]
                        break
                    if workflow[step][i][0]=='a' and part[2] < int(splited[0][2:]):
                        step = splited[1]
                        break
                    if workflow[step][i][0]=='s' and part[3] < int(splited[0][2:]):
                        step = splited[1]
                        break
                elif '>' in workflow[step][i]:
                    if workflow[step][i][0]=='x' and part[0] > int(splited[0][2:]):
                        step = splited[1]
                        break
                    if workflow[step][i][0]=='m' and part[1] > int(splited[0][2:]):
                        step = splited[1]
                        break
                    if workflow[step][i][0]=='a' and part[2] > int(splited[0][2:]):
                        step = splited[1]
                        break
                    if workflow[step][i][0]=='s' and part[3] > int(splited[0][2:]):
                        step = splited[1]
                        break
    return step == 'A'

workflows = lines[0].split('\n')
workflow = dict()
for i in workflows:
    splited = i.split('{')
    name = splited[0]
    rest = splited[1][:len(splited[1])-1].split(',')
    workflow[name] = rest

print(workflow)

parts = lines[1].split('\n')
part = []
for i in parts:
    splited = i[1:len(i)-1].split(',')
    x = int(splited[0].split('=')[1])
    m = int(splited[1].split('=')[1])
    a = int(splited[2].split('=')[1])
    s = int(splited[3].split('=')[1])
    part += [[x,m,a,s]]

res = 0
for p in part:
    if isAccepted(p, workflow):
        res += sum(p)

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2


print("Part 2 : ", )
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))