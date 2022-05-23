if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        try:
            students[score] += [name]
        except:
            students[score] = [name]
    for i in sorted(students[sorted(students.keys())[1]]):
        print(i)
