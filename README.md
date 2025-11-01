# BusStationX

BusStationX is a Python-based bus station management system that automates trip scheduling, ticketing, user and driver registration, and real-time status control. It supports Persian calendar formats and includes GUI dialogs via customtkinter.

---

## Key Features
### User & Driver Management

- Complete CRUD Operations: Add, edit, and delete users and drivers with full input validation
- Smart Status Tracking: Fire drivers with automatic cancellation of their active trips and related tickets
- Quick Search: Filter users and drivers by various criteria for easy access

### Trip Management

- Trip Lifecycle: Create, modify, and cancel trips with seat tracking

- Automatic Status Updates: Trip status automatically updates after departure

- Driver Assignment: Assign drivers to trips with conflict prevention

- Cascade Cancellation: Canceling a trip automatically cancels all associated tickets

### Ticket Reservation System

- Seat Selection: Interactive seat selection with real-time availability

- PDF Ticket Generation: Automatically generate PDF tickets for reservations

- Flexible Cancellation: Cancel reservations with automatic seat release

- Status Tracking: Monitor ticket status throughout the reservation lifecycle

### Technical Features

- Modern GUI: Built with customtkinter for an enhanced user experience

- Persian Calendar Support: Integrated jdatetime for Persian calendar functionality

- CSV-Based Storage: No database required - uses CSV files for data persistence

- Advanced Search: Search and filter across users, drivers, trips, and tickets

- Smart Sorting: View sorted lists with detailed information display

- Quick Access: Click on any ID, name, or bus plate to view detailed information

- Comprehensive Status Tracking: Real-time status monitoring for drivers, trips, and tickets

### Data Management

- Click-to-View Details: Direct access to detailed information by clicking on:

    - Trip ID, Ticket ID, User ID, Driver ID
    - User names and driver names
    - Bus license plates
    - Smart Filters: Filter data by specific values across all entities

- Sorted Views: Organized lists for efficient data browsing

### Automated Workflows

- Status Automation: Automatic trip status updates post-departure

- Cascade Operations: Firing drivers or canceling trips automatically handles all dependencies

- Real-time Updates: Instant reflection of changes across the system

- Input Validation: Comprehensive validation ensures data integrity
---

## Installation

Clone the repo:
```bash
git clone https://github.com/TAYMAZ328/BusStationX.git
cd BusStationX
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
python main.py
```