# Employee Network Management System

A comprehensive Python application that manages employee data and analyzes workplace relationships using graph algorithms. This system stores employee information and models connections between employees as a weighted graph network.

## Features

### Core Functionality
- **Employee Management**: Add, remove, and view employee records
- **Network Connections**: Create and manage relationships between employees with weighted connections
- **Graph Algorithms**: Leverage advanced algorithms to analyze the employee network:
  - **Dijkstra's Algorithm**: Find the shortest path between two employees
  - **Breadth-First Search (BFS)**: Traverse the network level by level
  - **Depth-First Search (DFS)**: Traverse the network depth by depth
  - **Prim's Minimum Spanning Tree (MST)**: Identify the most efficient network structure

### Employee Attributes
Each employee record includes:
- Registration Number (unique identifier)
- Age
- Gender
- Education Level
- Job Title
- Years of Experience
- Salary

## Project Structure

```
employee_network_management/
├── README.md                      # Project documentation
├── main.py                        # Entry point with interactive menu
├── employee.py                    # Employee class definition
├── employee_management_system.py  # Core system logic with graph algorithms
└── data.csv                       # Employee data (CSV format)
```

## Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Setup
1. Clone the repository:
```bash
git clone <repository-url>
cd employee_network_management
```

2. Ensure `data.csv` is in the project root directory with the following format:
```csv
registration_number,age,gender,education_level,job_title,years_of_experience,salary
E001,28,Male,Bachelor,Software Engineer,5,75000
E002,35,Female,Master,Senior Manager,10,95000
E003,32,Male,Bachelor,Product Manager,7,85000
```

## Usage

### Running the Application

```bash
python main.py
```

This launches an interactive menu with the following options:

### Menu Options

| Option | Description |
|--------|-------------|
| 1 | Print all employees and their details |
| 2 | Add a new employee to the system |
| 3 | Remove an employee by registration number |
| 4 | Connect two employees (create a relationship with weight) |
| 5 | Disconnect two employees (remove a relationship) |
| 6 | Find shortest distance between two employees |
| 7 | Perform BFS traversal from a starting employee |
| 8 | Perform DFS traversal from a starting employee |
| 9 | Generate and display the Minimum Spanning Tree |
| 10 | Display total number of employees |
| 11 | Exit the program |

### Example Workflow

```
1. Load employees from data.csv (automatic)
2. Select option 4 to connect employees (e.g., E001 and E002 with weight 5)
3. Select option 6 to find the shortest path between E001 and E003
4. Select option 7 to visualize network connections via BFS
5. Select option 9 to see the most efficient network structure
```

## How It Works

### Data Structure
The system uses an **adjacency matrix** to represent the employee network:
- Rows and columns represent employee indices
- Matrix values represent connection weights (0 = no connection)
- Maximum capacity: 100 employees

### Algorithm Explanations

#### Dijkstra's Algorithm
Finds the shortest path between two employees by calculating cumulative weights along different routes through the network.

#### Breadth-First Search (BFS)
Explores all employees connected directly and indirectly to a starting employee, level by level.

#### Depth-First Search (DFS)
Explores as far as possible along each branch before backtracking in the employee network.

#### Prim's Minimum Spanning Tree
Identifies the minimum-cost subset of connections that keeps all employees connected, useful for optimizing network communication.

## System Limitations

- **Maximum Employees**: 100 (configurable via `MAX_EMPLOYEES` in `EmployeeManagementSystem`)
- **CSV Format**: Requires exactly 7 comma-separated fields per employee
- **Memory**: Uses a 100×100 adjacency matrix regardless of actual employee count

## File Specifications

### data.csv
- **Format**: CSV (Comma-Separated Values)
- **Required Fields**: 7 fields in this exact order
  1. Registration Number (string)
  2. Age (integer)
  3. Gender (string)
  4. Education Level (string)
  5. Job Title (string)
  6. Years of Experience (integer)
  7. Salary (integer)
- **Example**:
  ```csv
  E001,28,Male,Bachelor,Software Engineer,5,75000
  E002,35,Female,Master,Senior Manager,10,95000
  ```

## Error Handling

The system handles:
- Missing `data.csv` file (displays error message)
- Invalid CSV format (checks for 7 fields per row)
- Invalid registration numbers (returns -1 or None)
- Empty employee network traversals

## Performance Considerations

| Operation | Time Complexity |
|-----------|-----------------|
| Add Employee | O(1) |
| Remove Employee | O(MAX_EMPLOYEES) |
| Find Employee | O(n) where n = number of employees |
| Dijkstra's Algorithm | O(MAX_EMPLOYEES²) |
| BFS/DFS | O(MAX_EMPLOYEES + edges) |
| Prim's MST | O(MAX_EMPLOYEES²) |

## Future Enhancements

- [ ] Support for dynamic array resizing beyond 100 employees
- [ ] Export employee network data to file
- [ ] Visualize network as graph
- [ ] Add employee search filters
- [ ] Implement graph coloring algorithm
- [ ] Add data persistence to database
- [ ] Web interface for management

## License

This project is open source and available for educational purposes.

## Author

**sasiakula006-prog**

## Support

For issues or questions, please open an issue on the GitHub repository.
