# Lab Assignment Sheet-2  
**School of Engineering and Technology**  
**Course Code & Name:** ENCS351 / Operating System  

---

## Student Details
- **Name:** Jai  
- **Program:** B.Tech CSE (Data Science)  
- **Roll Number:** 2301420045  

---

## Problem Statement
Design and implement a Python program to simulate a basic system startup sequence. The program should demonstrate multiprocessing concepts, logging, and proper process lifecycle management. The expected outputs include console messages during system startup/shutdown and a log file (`process_log.txt`) recording process activity.

---

## Tasks Overview
1. **System Startup Simulation**  
   Simulate a simple system boot by printing startup and shutdown messages.  

2. **Child Processes with Multiprocessing**  
   Use Python’s `multiprocessing` module to create at least two child processes running concurrently.  

3. **Logging Process Activity**  
   Configure logging to capture timestamped messages for process start and end times.  

4. **Process Termination and Verification**  
   Ensure proper termination (`join()`) of all processes and verify log file output.  

---

## Implementation Details
- **Language:** Python 3  
- **Modules Used:** `multiprocessing`, `logging`, `time`  
- **Log File:** `process_log.txt`  
- **Execution Steps:**
  ```bash
  # Navigate to project folder
  cd assignment_2

  # Run the script
  python3 2301420045_assignment2.py

  # View generated logs
  cat process_log.txt
