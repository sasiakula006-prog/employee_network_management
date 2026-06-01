from collections import deque
from queue import Queue


class EmployeeManagementSystem:
    MAX_EMPLOYEES = 100

    def __init__(self):
        self.employees = [None] * self.MAX_EMPLOYEES
        self.adjacency_matrix = [
            [0] * self.MAX_EMPLOYEES
            for _ in range(self.MAX_EMPLOYEES)
        ]
        self.num_employees = 0

    def add_employee(self, employee):
        if self.num_employees < self.MAX_EMPLOYEES:
            self.employees[self.num_employees] = employee
            self.num_employees += 1

    def remove_employee(self, registration_number):
        index = self.find_employee_index(registration_number)

        if index != -1:
            self.employees[index] = None

            for i in range(self.MAX_EMPLOYEES):
                self.adjacency_matrix[index][i] = 0
                self.adjacency_matrix[i][index] = 0

    def connect_employees(self, reg1, reg2, weight):
        index1 = self.find_employee_index(reg1)
        index2 = self.find_employee_index(reg2)

        if index1 != -1 and index2 != -1:
            self.adjacency_matrix[index1][index2] = weight
            self.adjacency_matrix[index2][index1] = weight

    def disconnect_employees(self, reg1, reg2):
        index1 = self.find_employee_index(reg1)
        index2 = self.find_employee_index(reg2)

        if index1 != -1 and index2 != -1:
            self.adjacency_matrix[index1][index2] = 0
            self.adjacency_matrix[index2][index1] = 0

    def find_employee_index(self, registration_number):
        for i in range(self.num_employees):
            if (
                self.employees[i] is not None
                and self.employees[i].registration_number == registration_number
            ):
                return i

        return -1

    def get_number_of_employees(self):
        count = 0

        for employee in self.employees:
            if employee is not None:
                count += 1

        return count

    def find_employee(self, registration_number):
        index = self.find_employee_index(registration_number)

        if index != -1:
            return self.employees[index]

        return None

    def print_employees(self):
        for employee in self.employees:
            if employee is not None:
                print(f"Employee: {employee.registration_number}")
                print(f"Age: {employee.age}")
                print(f"Gender: {employee.gender}")
                print(f"Education Level: {employee.education_level}")
                print(f"Job Title: {employee.job_title}")
                print(f"Years of Experience: {employee.years_of_experience}")
                print(f"Salary: {employee.salary}")
                print()

    # Dijkstra's Algorithm
    def shortest_distance_between_employees(self, reg1, reg2):
        index1 = self.find_employee_index(reg1)
        index2 = self.find_employee_index(reg2)

        if index1 == -1 or index2 == -1:
            return -1

        distance = [9999] * self.MAX_EMPLOYEES
        visited = [False] * self.MAX_EMPLOYEES

        distance[index1] = 0

        for _ in range(self.MAX_EMPLOYEES - 1):

            min_distance = 9999
            min_index = -1

            for j in range(self.MAX_EMPLOYEES):
                if not visited[j] and distance[j] <= min_distance:
                    min_distance = distance[j]
                    min_index = j

            if min_index == -1:
                break

            visited[min_index] = True

            for j in range(self.MAX_EMPLOYEES):

                if (
                    not visited[j]
                    and self.adjacency_matrix[min_index][j] != 0
                    and distance[min_index] != 9999
                    and distance[min_index]
                    + self.adjacency_matrix[min_index][j]
                    < distance[j]
                ):
                    distance[j] = (
                        distance[min_index]
                        + self.adjacency_matrix[min_index][j]
                    )

        return distance[index2]

    # BFS
    def breadth_first_search(self, registration_number):
        index = self.find_employee_index(registration_number)

        if index == -1:
            return

        visited = [False] * self.MAX_EMPLOYEES

        q = Queue()
        q.put(index)
        visited[index] = True

        print(f"BFS Traversal starting from {registration_number}:")

        while not q.empty():

            current_index = q.get()

            print(
                self.employees[current_index].registration_number,
                end=" "
            )

            for i in range(self.MAX_EMPLOYEES):

                if (
                    not visited[i]
                    and self.adjacency_matrix[current_index][i] != 0
                ):
                    q.put(i)
                    visited[i] = True

        print()

    # DFS
    def depth_first_search(self, registration_number):
        index = self.find_employee_index(registration_number)

        if index == -1:
            return

        visited = [False] * self.MAX_EMPLOYEES

        stack = deque()
        stack.append(index)

        print(f"DFS Traversal starting from {registration_number}:")

        while stack:

            current_index = stack.pop()

            if not visited[current_index]:
                print(
                    self.employees[current_index].registration_number,
                    end=" "
                )
                visited[current_index] = True

            for i in range(self.MAX_EMPLOYEES):

                if (
                    not visited[i]
                    and self.adjacency_matrix[current_index][i] != 0
                ):
                    stack.append(i)

        print()

    def find_min_key(self, key, mst_set):
        min_key = 9999
        min_index = -1

        for v in range(self.MAX_EMPLOYEES):

            if not mst_set[v] and key[v] < min_key:
                min_key = key[v]
                min_index = v

        return min_index

    # Prim's MST
    def prim_mst(self):

        parent = [-1] * self.MAX_EMPLOYEES
        key = [9999] * self.MAX_EMPLOYEES
        mst_set = [False] * self.MAX_EMPLOYEES

        key[0] = 0

        for _ in range(self.MAX_EMPLOYEES - 1):

            u = self.find_min_key(key, mst_set)

            if u == -1:
                break

            mst_set[u] = True

            for v in range(self.MAX_EMPLOYEES):

                if (
                    self.adjacency_matrix[u][v] != 0
                    and not mst_set[v]
                    and self.adjacency_matrix[u][v] < key[v]
                ):
                    parent[v] = u
                    key[v] = self.adjacency_matrix[u][v]

        print("Minimum Cost Spanning Tree (MST):")

        for i in range(1, self.MAX_EMPLOYEES):

            if (
                parent[i] != -1
                and self.employees[i] is not None
                and self.employees[parent[i]] is not None
            ):
                print(
                    f"{self.employees[parent[i]].registration_number}"
                    f" - "
                    f"{self.employees[i].registration_number}"
                )