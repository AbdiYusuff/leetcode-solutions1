# The Leetcode file system keeps a log each time some user performs a change folder operation.
# The operations are described below:
# "../" : Move to the parent folder of the current folder. 
#(If you are already in the main folder, remain in the same folder).
# "./" : Remain in the same folder.
# "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

def minOperations(log):
    n = len(log)
    for i in range(n):
        if log[i] == "./":
            continue
        elif log[i] == "../":
            