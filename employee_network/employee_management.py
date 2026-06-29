import csv

from employee import Employee
from graph_algorithms import (
    bfs,
    dfs,
    dijkstra,
    prim_mst
)


class EmployeeManagementSystem:

    def __init__(self):
        self.employees = {}
        self.graph = {}

    def add_employee(self, employee):
        self.employees[
            employee.registration_number
        ] = employee

        self.graph.setdefault(
            employee.registration_number,
            []
        )

    def remove_employee(self, reg_num):

        if reg_num not in self.employees:
            return

        del self.employees[reg_num]

        self.graph.pop(reg_num, None)

        for node in self.graph:
            self.graph[node] = [
                edge
                for edge in self.graph[node]
                if edge[0] != reg_num
            ]

    def connect_employees(
        self,
        emp1,
        emp2,
        weight
    ):

        self.graph[emp1].append(
            (emp2, weight)
        )

        self.graph[emp2].append(
            (emp1, weight)
        )

    def shortest_path(
        self,
        source,
        destination
    ):
        distances = dijkstra(
            self.graph,
            source
        )

        return distances[destination]

    def bfs_traversal(self, start):
        return bfs(self.graph, start)

    def dfs_traversal(self, start):
        return dfs(self.graph, start)

    def minimum_spanning_tree(self):
        return prim_mst(self.graph)

    def total_employees(self):
        return len(self.employees)

    def load_csv(self, filename):

        with open(
            filename,
            newline='',
            encoding='utf-8'
        ) as file:

            reader = csv.reader(file)

            for row in reader:

                employee = Employee(
                    row[0],
                    int(row[1]),
                    row[2],
                    row[3],
                    row[4],
                    int(row[5]),
                    int(row[6])
                )

                self.add_employee(employee)
