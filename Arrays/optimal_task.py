def optimal_task(tasks):
    tasks = sorted(tasks)
    for i in range(len(tasks)//2):
        print(tasks[i], tasks[~i])


A = [6, 3, 2, 7, 5, 5, 9]
optimal_task(A)
