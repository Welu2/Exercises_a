# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command, *other = input().split()
        for i in range(len(other)):
            other[i] = int(other[i])
        if command == "insert":
            list.insert(other[0], other[1])
        elif command == "print":
            print(list)
        elif command == "remove":
            list.remove(other[0])
        elif command == "append":
            list.append(other[0])
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
