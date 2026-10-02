# MyProject_Campus-Library-Reservation
# Lab 1 — Requirements Engineering & UML Use-Case Modelling

**Course:** Software Engineering  
**Lab:** Lab 1  
**Problem Statement:** #08 — Campus & Academic Operations  
**System:** Digital Campus Library Reservation Gateway

---

## Overview

This repository contains the deliverables for **Software Engineering Lab 1**, focusing on Requirements Engineering and UML Use-Case Modelling.

The **Digital Campus Library Reservation Gateway** is designed to support digital library operations such as:

- Searching the physical ISBN catalog
- Managing book hold requests and FIFO waitlists
- Providing automated hold notifications
- Managing book availability
- Tracking overdue fine transactions

---

##  Repository Contents

### 1. Problem Statement

`8_SE_Lab1_SE_Problem_Statements.pdf`

Contains the problem statement provided for the Software Engineering Lab.

### 2. Requirements Engineering

`Requirement_table.pdf`

Contains the identified system requirements, including:

- **FR-001 to FR-005** — Functional Requirements
- **NFR-001 to NFR-002** — Non-Functional Requirements
- Requirement ID
- Requirement Type
- Description
- Priority
- Acceptance Criteria
- Rationale

### 3. UML Use-Case Model

`Uml.drawio.pdf`

The UML Use-Case Diagram represents the interaction between the system and its primary actors:

- **Student Member**
- **Head Librarian**
- **Payment Gateway**

The diagram also represents the required `«include»` and `«extend»` relationships between relevant use cases.

---

##  Architecture Method

A **Layered Architecture** was selected for the Digital Campus Library Reservation Gateway.

The Presentation Layer handles user interaction, while the Application Layer contains the core business logic. The Data Layer manages persistent information required by the system.

The **API Gateway** acts as the main entry point between the user interface and the application services. Individual services are responsible for specific library operations such as catalog search, reservations, notifications, loans, returns, and fines.

---

##  Why This Architecture?

The architecture was selected because it provides:

- **Modularity** — Each major library operation is handled by a separate service.
- **Maintainability** — Individual components can be modified without affecting the entire system.
- **Scalability** — Frequently used operations such as catalog search can be optimized independently.
- **Security** — Authentication and authorization can be handled at the API Gateway.
- **Separation of Responsibilities** — User interface, application logic, and data management remain clearly separated.
- **Requirement Alignment** — The architecture directly supports catalog searching, FIFO reservation queues, notifications, book availability, and fine management.

---

##  Architectural Diagram

The architecture diagram is available in:

`Architectural_diagram/Digital_Campus_Library_Architecture.png`

It provides a visual representation of the system layers, major services, databases, actors, and external notification services.

---

