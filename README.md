# Reservation_app

The "Conference Room Management System" project focuses on creating a comprehensive tool for managing conference rooms and making reservations for various events. The primary goal is to provide users with an intuitive interface through which they can browse available rooms, make reservations, edit existing room data, and search for rooms based on specific criteria.

Key Features:

Homepage:
Upon entering the homepage, users are presented with a list of all available conference rooms along with information about their occupancy on a given day. For occupied rooms, the status information is displayed. Links for modifying room data and deleting the room are provided next to each room's name.

Detailed Room View:
Clicking on a room's name grants users access to detailed information about the room. This includes the room's name, capacity, and projector availability. Additionally, a list of upcoming days when the room is occupied is displayed, accompanied by links for reservation, deletion, and room modification.

Adding a New Room:
Users have the ability to add a new room through a form that allows them to input data such as the name, capacity, and projector availability.

Room Editing:
In the room editing section, users can input or modify data related to the room, such as its name, capacity, projector availability, and more.

Room Reservation:
Users are enabled to make room reservations by selecting a reservation date. The system automatically checks the room's availability on the specified day and prevents duplicate reservations as well as selecting dates from the past.

Room Search (Optional):
An optional feature allows users to search for rooms based on criteria such as the room's name, capacity, and projector availability.

Technology Stack:
The project is developed using the Django framework in Python. The backend logic, data management, and interaction with the database are implemented using Python and Django. The frontend user interface is created using HTML. For data storage and management, the project utilizes the PostgreSQL database.

The project aims to provide an efficient tool for organizations and users who wish to effectively manage conference rooms and make reservations in a transparent manner that aligns with their needs.
