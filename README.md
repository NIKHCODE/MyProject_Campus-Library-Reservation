# Digital Campus Library Reservation Gateway

**Course:** Software Engineering  
**Problem Statement:** #08 – Campus & Academic Operations  
**Repository:** [MyProject_Campus-Library-Reservation](https://github.com/NIKHCODE/MyProject_Campus-Library-Reservation)

## Project Overview

The Digital Campus Library Reservation Gateway is designed to simplify library operations for students and the Head Librarian. The system focuses on book catalogue searching, reservation requests, FIFO waiting queues, loan and return management, notifications and fine tracking.

This repository contains the work completed across Software Engineering Labs 1 to 7, including requirements engineering, UML modelling, architectural design, project management, code analysis, test coverage and fuzz testing.

## Lab 1 – Requirements Engineering and UML Use-Case Modelling

**Objective:** Identify system requirements and represent the interactions between users and the system using UML use-case modelling.

### Work Completed

1. Identified the main actors: Student Member, Head Librarian and Payment Gateway.
2. Prepared five Functional Requirements (FR-001 to FR-005).
3. Prepared two Non-Functional Requirements (NFR-001 and NFR-002).
4. Defined priorities, acceptance criteria and rationale for each requirement.
5. Created a UML Use-Case Diagram showing actors, system functions and relationships using `include` and `extend`.
6. Prepared a Use-Case Flow for the Place Hold Request functionality.

### Deliverables

| File | Description |
|---|---|
| `Requirement_table.pdf` | Functional and non-functional requirements |
| `Uml.drawio.pdf` | UML Use-Case Diagram |
| `Campus_Library_Use_Case_Flow.pdf` | Main and alternate use-case flows |

## Lab 2 – Agile Project Management

**Objective:** Understand and apply Agile project management practices using Jira.

### Work Completed

1. Created a Jira project named `Kanban_BPS#25`.
2. Prepared a Kanban board to organise and track project tasks.
3. Created a Scrum board to manage work through sprints.
4. Added and organised project issues based on the identified requirements.
5. Worked with Jira issues KBPS-5 to KBPS-8.
6. Used the boards to understand task tracking, workflow management and sprint planning.

### Deliverables

| File | Description |
|---|---|
| `Jira_kanban.pdf` | Kanban board and workflow |
| `Jira_scrum.pdf` | Scrum board and sprint management |

## Lab 3 – Component Modelling and Architectural Design

**Objective:** Study architectural styles and select a suitable architecture for the system.

### Architectural Style Selected

**Layered Architecture**

The system is organised into three main layers.

1. **Presentation Layer:** Provides the web and mobile interface for students and the Head Librarian.
2. **Application Layer:** Handles the core operations through the API Gateway and individual application services.
3. **Data Layer:** Stores catalogue information, library records and reservation queue details.

### Main Components

- Web / Mobile Interface
- API Gateway
- Catalog Search Service
- Reservation / Hold Queue Service
- Notification Service
- Loan & Return Service
- Fine Management Service
- Catalog Database
- Library Database
- Queue Store
- External Email / SMS Service

### Reasons for Selection

1. Separating the presentation, application and data layers makes the system easier to maintain and modify.
2. Individual services handle specific operations such as catalogue search, reservations, loans and fines.

The API Gateway also provides a central point for authentication and authorization. Catalogue indexing and a separate FIFO queue store help improve the handling of frequently used operations.

### Deliverables

| File | Description |
|---|---|
| `Digital Campus Library_Architecture Diagram.png` | System architecture diagram |
| `Campus_Library_Architecture_Justification.pdf` | Architecture selection and justification |

## Lab 4 – Software Implementation and Debugging

**Objective:** Work with an existing Python application, understand its implementation and make changes to its functionality.

### Work Completed

The repository contains the helicopter game assignment package, which focuses on the following functionality:

1. Helicopter movement and screen boundary handling.
2. Collision detection and game-over conditions.
3. Distance-based score calculation.
4. One-hit shield functionality.

The implementation work involves modifying the existing Python code and checking the behaviour of the application after changes.

### Tools Used

- Python
- Pygame
- VS Code

### Deliverables

`SE_Lab04_08_helicopter-main.zip`

The archive contains the helicopter game source files and related project material.

## Lab 5 – Static Code Analysis

**Objective:** Analyse source code to identify potential coding issues, security weaknesses and maintainability problems.

### Work Completed

1. Used Pylint to analyse Python code quality.
2. Checked code structure, naming conventions and possible programming errors.
3. Used Bandit to identify potential security-related issues.
4. Reviewed the reported warnings and made improvements to the source code.
5. Rechecked the code after making the changes.

### Tools Used

- Python
- Pylint
- Bandit

### Result

The code analysis and improvements resulted in a Pylint score of **9.86/10**.

### Deliverables

`Lab5_Static_Code_Analysis/`

Contains the source code and static analysis related files.

## Lab 6 – Code and Branch Coverage Testing

**Objective:** Measure how much of the source code is executed by the test cases and identify untested execution paths.

### Work Completed

1. Worked with `ski_resort_pass.py`.
2. Created test cases using pytest.
3. Performed line coverage testing to identify executed and unexecuted statements.
4. Performed branch coverage testing to check different decision paths.
5. Added additional test cases to cover previously missed statements and branches.
6. Generated coverage reports to verify the results.

### Tools Used

- Python
- Pytest
- Coverage.py

### Test Results

| Metric | Result |
|---|---:|
| Statements | 59 |
| Line Coverage | 100% |
| Branch Coverage | 100% |
| Branches | 42 |

### Deliverables

`Lab6_Code_Branch_Coverage/`

- `ski_resort_pass.py`
- `test_ski_resort.py`
- `CodeCoverageTest_ski_resort_pass.py`
- `BranchCoverageTest_ski_resort_pass.py`
- Coverage reports

## Lab 7 – Fuzz Testing

**Objective:** Test the application with automatically generated inputs to identify unexpected behaviour and improve input validation.

### Work Completed

1. Used Hypothesis for property-based testing.
2. Created fuzz tests for different input conditions.
3. Tested date validation in season pass processing.
4. Tested trail gradient calculations with different input values.
5. Tested lift access tier calculations, including boundary and zero-distance cases.
6. Checked how the application handles invalid and unexpected inputs.
7. Improved validation for dates, gradients, zero distance and lift zones.

### Main Functions Tested

- `parse_season_pass_validity`
- `compute_trail_gradient`
- `calculate_lift_access_tier`

### Tools Used

- Python
- Pytest
- Hypothesis

### Deliverables

`Lab7_Fuzz_Testing/`

- `processor.py`
- `test_processor.py`

## Technologies and Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Game Development | Pygame |
| Requirements Modelling | UML, Draw.io |
| Project Management | Jira |
| Static Code Analysis | Pylint, Bandit |
| Unit Testing | Pytest |
| Code Coverage | Coverage.py |
| Fuzz Testing | Hypothesis |
| Version Control | Git, GitHub |

## Repository Structure

```text
MyProject_Campus-Library-Reservation/
│
├── Lab5_Static_Code_Analysis/
│
├── Lab6_Code_Branch_Coverage/
│
├── Lab7_Fuzz_Testing/
│
├── Requirement_table.pdf
├── Uml.drawio.pdf
│
├── Digital Campus Library_Architecture Diagram.png
├── Campus_Library_Architecture_Justification.pdf
├── Campus_Library_Use_Case_Flow.pdf
│
├── Jira_kanban.pdf
├── Jira_scrum.pdf
│
├── SE_Lab04_08_helicopter-main.zip
│
└── README.md
```

## Conclusion

The work across these labs covers different stages of software engineering, starting with requirements identification and UML modelling, followed by architectural design and Agile project management. The later labs focus on source code quality, test coverage and fuzz testing.

Together, these exercises provide practical experience with software requirements, design, project tracking, code analysis and software testing.

## Repository

[GitHub – MyProject Campus Library Reservation](https://github.com/NIKHCODE/MyProject_Campus-Library-Reservation)
