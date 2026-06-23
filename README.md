# Volleyball Stats Tracker 🏐

An Object-Oriented Python application for tracking and analyzing live volleyball match statistics. *(Developed for the CENG113M Best Project Competition)*

## About the Project
This project is a Command Line Interface (CLI) application that allows you to track player statistics during a volleyball match in real-time. Built using Object-Oriented Programming (OOP) principles, it calculates match details dynamically and generates a comprehensive `.txt` report at the end of the game.

## Features
The application includes 5 main functionalities:
* **Add a New Player:** Create your team roster by entering a player's name and jersey number.
* **Record an Action:** Track in-game actions such as Attack (Kill), Block, Ace (Serve), Defense (Dig), Perfect Set (Assist), and Error by using the player's jersey number.
* **Live Team Statistics:** Dynamically calculates each player's total points contributed and their overall efficiency rate based on their actions.
* **Save Match Report (File I/O):** Once the match is finished, securely exports all individual statistics and the team's total score into a text file with a timestamp (e.g., `Match_Report_20260623_204700.txt`).

![Application Menu](menu.png)
<img width="1484" height="386" alt="menu" src="https://github.com/user-attachments/assets/7238e99d-147e-43e7-97c8-f85db13ad7ab" />

![Match Report Example](report.png)
<img width="1536" height="629" alt="report" src="https://github.com/user-attachments/assets/6dfa5639-8921-4419-9792-320111b7b7f1" />


## How to Run
To run this project on your local machine, follow these steps:

1. Ensure you have **Python 3.x** installed on your system.
2. Clone or download this repository to your local machine.
3. Open your Terminal (or Command Prompt) and navigate to the project directory.
4. Run the following command to start the application:
```bash
   python VolleyballStatsTracker.py
