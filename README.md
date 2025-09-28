# CSCI717_Assignment0
Repository for CSCI 717 Assignment 0

DESCRIPTION:
This README is for Assignment 0 for CSCI 717. This contains instructions on how to run the aristocrat_solver.py script.

ARISTOCRAT_SOLVER.PY SCRIPT:
This python script is capable of recovering plaintext from an Aristocrat cipher.
It has a default Aristocrat cipher for the following plaintext:
    SOFTWARE DEVELOPERS SHOULD WRITE CODE THAT IS EASY TO READ, TEST, AND MAINTAIN OVER TIME.
    THIS COURSE IN SOFTWARE CONSTRUCTION FOCUSES ON HOW TO DEVELOP SOFTWARE THAT IS FREE FROM BUGS, UNDERSTANDABLE, AND EASY TO MAINTAIN.
If one wishes to test solving a different Aristocrat cipher, a different cipher string can be specified by the user (See "RUNNING THE SCRIPT").

RUNNING THE SCRIPT:
The following steps should be followed to successfully run the aristocrat_solver.py script:
  - Navigate to the directory that the aristocrat_solver.py script is located.
  - Ensure that the english_quadgrams.txt file is located at this directory. If it is not located here,
    make sure to checkout the entire repository from github (see below).
  - Open a new command terminal at this directory.
  - Run the script with the following command:
      python aristocrat_solver.py
  - Note that this uses the default Aristocrat cipher that is embedded in the code.
  - A user can run the script with the following command if they want to test out a different aristocrat cipher:
      python aristocrat_solver.py [different aristocrat cipher]

GITHUB:
Here are some notes about each of the files in the repository: https://github.com/WillyJahner/CSCI717_Assignment0
  - aristocrat_solver.py: The python script that is capable of recovering plaintext from an Aristocrat cipher.
  - english_quadgrams.txt: Quadgram file used by the python script.
  - CSCI717_Assignment0_ExperienceReport_WillyJahner.docx: Experience Report (needed for assignment 0 submission).
  - ChatGPT_VibeCoding.docx: Transcript of the vibe coding session with ChatGPT.
  - GoogleGemini_VibeCoding.docx: Transcript of the vibe coding session with Google Gemini.
