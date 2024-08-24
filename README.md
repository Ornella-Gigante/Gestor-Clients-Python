# Client Management Program

## Overview
    This Python program is from a Python course that I made from https://github.com/hektorprofe that  allows you to manage clients through a command-line interface and is designed to test basic Python skills. 

## The program includes functionality to:

    List all clients.
    Search for a client by their ID (DNI).
    Add a new client with fields for name, surname, and DNI.
    Update a client's name and surname based on their DNI.
    Delete a client by DNI.
    Exit the program.
    The program operates with initial test data and does not save data to the disk, ensuring no two clients have the same DNI.

## Repository

    GitHub Repository

## List all clients.

    Search for a client by their ID (DNI).
    Add a new client with fields for name, surname, and DNI.
    Update a client's name and surname based on their DNI.
    Delete a client by DNI.
    Exit the program.
    The program operates with initial test data and does not save data to the disk, ensuring no two clients have the same DNI.

## Organization

* Folder Structure:

      Gestor de clientes/
      requirements.txt (empty)
      README.md (empty)
      gestor/ (directory for scripts)
      run.py - Main script to start the application.
      menu.py - CLI menu interface.
      database.py - Manages client data.
      helpers.py - Contains utility functions.
  
* Mock Database:

      Client Class: Defines client attributes and methods for displaying client information.
      Clients Class: Static methods to handle client operations (search, create, update, delete) using a mock list.

* Unit Testing:

      Directory tests/ with __init__.py for test discovery.
      test_database.py for unit tests using unittest.
      Install pytest for running tests: pip install pytest.
      Run tests with: pytest -v.

  
* Menu Implementation:

      Menu options are handled in menu.py.
      Utilizes helpers.py for input validation and clearing the screen.

* CSV Persistence:

      Clients are initially loaded from clientes.csv.
      Changes are saved back to clientes.csv.
      A separate test CSV file tests/clientes_test.csv is used to avoid modifying real data during tests.
  
* GUI Development:
      
      Future enhancements include a GUI using Tkinter:
      MainWindow Class: Main window with Treeview for displaying clients and buttons for actions.
      CreateClientWindow Class: Secondary window for adding new clients with real-time validation.
      Installation and Running

  
* Install Dependencies:
      
      Ensure Python is installed.
      Install required packages (if any) using pip.
  
* Run the Program:

      Execute run.py to start the CLI interface.
  
* Testing:

      Run unit tests with pytest to ensure the program functions correctly.



## License and Copyright

      This project is licensed under the MIT License and belongs to @hektorprofe
      
      For more information, visit--->  https://github.com/hektorprofe
