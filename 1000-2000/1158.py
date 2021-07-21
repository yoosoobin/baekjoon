import sys

n,k = map(int,sys.stdin.readline().split())
num_list = [i for i in range(1,n+1)]
pop_list = []
pos = k-1
for i in range(n):
    if len(num_list)>pos:
        pop_list.append(num_list.pop(pos))
        pos += k-1
    elif len(num_list)<= pos:
        pos %= len(num_list)
        pop_list.append(num_list.pop(pos))
        pos += k-1

print("<"+', '.join(str(i) for i in pop_list)+">")