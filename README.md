# BFS_Pocket_Rubik_Cube

This project is a task taken from the course "6.006 Introduction to algorithms" of the MIT Open Courseware.

The purpose of the assignment is to use Breadth First Search to solve the 2 x 2 x 2 Rubik's Cube, also known as the Pocket Cube. 

It is used a two-way BFS, starting from each end at the same time, one end is the initial configuration of the cube and the other one is the solved position, and meeting in the middle.

My code is in the file solver.py, the files RubikAbstraction.py, util.py, rubik.py, rubik_solver_GUI_Win.py are given to the students so they can focus on applying BFS.

In the util.py file I only added the retorna_nodo function.

In the rubik.py file I only added the movimiento_inverso(move).

In order to run the program, you must execute the sentence python rubik_solver_GUI_Win.py in the terminal.