import time
import os
import sys
from collections import deque

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
    while step != 'A' and step != 'R':
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

state = ['in', (1,4000), (1,4000), (1,4000), (1,4000)]
res = 0
queue = deque([state])
while queue:
    name, x, m, a, s = queue.popleft()
    if name == 'A':
        res += (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
        continue
    elif name == 'R':
        continue
    for i in range(len(workflow[name])):
        instru = workflow[name][i]
        if not ':' in instru:
            queue.append([instru, x, m, a, s])
            break
        else:
            
            splited = instru.split(':')
            value = int(splited[0][2:])
            if '<' in instru:
                if instru[0] == 'x':
                    if x[0] < value < x[1]:
                        queue.append([splited[1], (x[0], value - 1), m, a, s])
                        queue.append([name, (value, x[1]), m, a, s])
                        break
                    elif x[0] > value: 
                        continue
                    elif x[1] < value:
                        queue.append([splited[1], x, m, a, s])
                        break
                if instru[0] =='m':
                    if m[0] < value < m[1]:
                        queue.append([splited[1], x, (m[0], value - 1), a, s])
                        queue.append([name, x, (value, m[1]), a, s])
                        break
                    elif m[0] > value: 
                        continue
                    elif m[1] < value:
                        queue.append([splited[1], x, m, a, s])
                        break
                if instru[0] =='a':
                    if a[0] < value < a[1]:
                        queue.append([splited[1], x, m, (a[0], value - 1), s])
                        queue.append([name, x, m, (value, a[1]), s])
                        break
                    elif a[0] > value: 
                        continue
                    elif a[1] < value:
                        queue.append([splited[1], x, m, a, s])
                        break
                if instru[0] =='s':
                    if s[0] < value < s[1]:
                        queue.append([splited[1], x, m, a, (s[0], value - 1)])
                        queue.append([name, x, m, a, (value, s[1])])
                        break
                    elif s[0] > value: 
                        continue
                    elif s[1] < value:
                        queue.append([splited[1], x, m, a, s])
                        break

            if '>' in instru:
                if instru[0] == 'x':
                    if x[0] < value < x[1]:
                        queue.append([name, (x[0], value), m, a, s])
                        queue.append([splited[1], (value + 1, x[1]), m, a, s])
                        break
                    elif x[1] < value: 
                        continue
                    elif x[0] > value:
                        queue.append([splited[1], x, m, a, s])
                        break
                if instru[0] =='m':
                    if m[0] < value < m[1]:
                        queue.append([name, x, (m[0], value), a, s])
                        queue.append([splited[1], x, (value + 1, m[1]), a, s])
                        break
                    elif m[1] < value: 
                        continue
                    elif m[0] > value:
                        queue.append([splited[1], x, m, a, s])
                        break
                if instru[0] =='a':
                    if a[0] < value < a[1]:
                        queue.append([name, x, m, (a[0], value), s])
                        queue.append([splited[1], x, m, (value + 1, a[1]), s])
                        break
                    elif a[1] < value: 
                        continue
                    elif a[0] > value:
                        queue.append([splited[1], x, m, a, s])
                        break
                if instru[0] =='s':
                    if s[0] < value < s[1]:
                        queue.append([name, x, m, a, (s[0], value)])
                        queue.append([splited[1], x, m, a, (value + 1, s[1])])
                        break
                    elif s[1] < value: 
                        continue
                    elif s[0] > value:
                        queue.append([splited[1], x, m, a, s])
                        break

print("Part 2 : ", res)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))