from employee_management import EmployeeManagementSystem

if __name__ == "__main__":
    system = EmployeeManagementSystem()

    system.load_csv("data.csv")

    system.connect_employees("EMP001", "EMP002", 4)
    system.connect_employees("EMP001", "EMP003", 2)
    system.connect_employees("EMP002", "EMP004", 5)
    system.connect_employees("EMP003", "EMP004", 1)
    system.connect_employees("EMP004", "EMP005", 3)

    print("Total Employees:", system.total_employees())

    print("\nBFS Traversal:")
    print(system.bfs_traversal("EMP001"))

    print("\nDFS Traversal:")
    print(system.dfs_traversal("EMP001"))

    print("\nShortest Distance EMP001 -> EMP005:")
    print(system.shortest_path("EMP001", "EMP005"))

    print("\nMinimum Spanning Tree:")
    for edge in system.minimum_spanning_tree():
        print(edge)
