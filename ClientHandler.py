from threading import Thread
import os
import hashlib
from cryptography.fernet import Fernet

BUFSIZE = 1024

class ClientHandler(Thread):
    if os.path.exists("fernet.key"):
        with open("fernet.key", "rb") as f:
            key = f.read().strip()
    else:
        key = Fernet.generate_key()
        with open("fernet.key", "wb") as f:
            f.write(key)
            
    cipher = Fernet(key)
    # Handles communication with client in respective thread
    def __init__(self, client_socket):
        Thread.__init__(self)
        self.client = client_socket

    # Programming
    programs = {
        "Powerlifting": {
            "Description": "Increase strength in Squat, Bench, and Deadlift.",
            "General Plan": [
                {"exercise": "Low Bar Squats", "sets": 2, "reps": 6, "weight": "75 percent of max", "frequency": "3x/week", "progression": "Add 2.5 - 5.0 percent weekly"},
                {"exercise": "Pause Squats", "sets": 4, "reps": 5, "weight": "65 percent of max", "frequency": "1x/week"},
                {"exercise": "Pin Squats", "sets": 3, "reps": 6, "weight": "60 percent of max", "frequency": "1x/week"},
                {"exercise": "Tempo Squats", "sets": 3, "reps": 5, "weight": "65 percent of max", "frequency": "1x/week"},
                {"exercise": "Flat Bench", "sets": 3, "reps": 6, "weight": "80 percent of max", "frequency": "3x/week", "progression": "Add 2.5 - 5.0 percent weekly"},
                {"exercise": "Tempo Bench", "sets": 3, "reps": 5, "weight": "70 percent of max", "frequency": "1x/week"},
                {"exercise": "Long Pause Bench", "sets": 3, "reps": 3, "weight": "70 percent of max", "frequency": "1x/week"},
                {"exercise": "Incline Bench", "sets": 3, "reps": 3, "weight": "75 percent of max", "frequency": "1x/week"},
                {"exercise": "Deadlift", "sets": 3, "reps": 3, "weight": "85 percent of max", "frequency": "2x/week", "progression": "Add 2.5 - 5.0 percent weekly"},
                {"exercise": "Romanian Deadlift", "sets": 3, "reps": 6, "weight": "75 percent of max", "frequency": "1x/week"},
                {"exercise": "Barbell Row", "sets": 3, "reps": 5, "weight": "65 percent of max", "frequency": "1x/week"},
                {"exercise": "Pullups", "sets": 2, "reps": 6, "weight": "bodyweight", "frequency": "1x/week"}
            ],
            "Specializations": {
                "Squat": [
                    {"exercise": "Low Bar Squats", "sets": 4, "reps": 6, "weight": "75 percent of max", "frequency": "4x/week", "progression": "Add 2.5 - 5.0 percent weekly"},
                    {"exercise": "Pause Squats", "sets": 4, "reps": 5, "weight": "65 percent of max", "frequency": "2x/week"},
                    {"exercise": "Front Squats", "sets": 3, "reps": 8, "weight": "65 percent of max", "frequency": "1x/week"},
                    {"exercise": "Flat Bench", "sets": 3, "reps": 8, "weight": "70 percent of max", "frequency": "2x/week"},
                    {"exercise": "Deadlift", "sets": 3, "reps": 3, "weight": "75 percent of max", "frequency": "1x/week"},
                ],
                "Bench": [
                    {"exercise": "Flat Bench", "sets": 4, "reps": 6, "weight": "80 percent of max", "frequency": "4x/week", "progression": "Add 2.5 - 5.0 percent weekly"},
                    {"exercise": "Tempo Bench", "sets": 3, "reps": 6, "weight": "70 percent of max", "frequency": "2x/week"},
                    {"exercise": "Wide Grip Bench", "sets": 3, "reps": 8, "weight": "65 percent of max", "frequency": "1x/week"},
                    {"exercise": "Close Grip Bench", "sets": 3, "reps": 8, "weight": "70 percent of max", "frequency": "2x/week"},
                    {"exercise": "Low Bar Squats", "sets": 3, "reps": 8, "weight": "80 percent of max", "frequency": "1x/week"},
                    {"exercise": "Deadlift", "sets": 3, "reps": 6, "weight": "80 percent of max", "frequency": "1x/week"},
                ],
                "Deadlift": [
                    {"exercise": "Deadlift", "sets": 4, "reps": 6, "weight": "80 percent of max", "frequency": "3x/week", "progression": "Add 2.5 - 5.0 percent weekly"},
                    {"exercise": "Deficit Deadlift", "sets": 3, "reps": 6, "weight": "65 percent of max", "frequency": "2x/week"},
                    {"exercise": "Single Arm Dumbbell Row", "sets": 3, "reps": 10, "weight": "heavy", "frequency": "3x/week"},
                    {"exercise": "Romanian Deadlift", "sets": 4, "reps": 8, "weight": "55 percent of max", "frequency": "1x/week"},
                    {"exercise": "Neutral Grip Pull Ups", "sets": 3, "reps": 8, "weight": "weighted", "frequency": "2x/week"},
                    {"exercise": "Rack Pulls", "sets": 3, "reps": 3, "weight": "105 percent of max", "frequency": "1x/week"},
                ],
            }
        },
        "Bodybuilding": {
            "Description": "Hypertrophy training for muscle growth",
            "General Plan": [
                {"exercise": "Smith Machine Incline Bench", "sets": 3, "reps": 15, "frequency": "2x/week"},
                {"exercise": "Machine Chest Fly", "sets": 4, "reps": 12, "frequency": "2x/week"},
                {"exercise": "Cable Overhead Tricep Extension", "sets": 3, "reps": 20, "frequency": "2x/week"},
                {"exercise": "Cable Tricep Pushdown", "sets": 3, "reps": 15, "frequency": "2x/week"},
                {"exercise": "Leg Extension", "sets": 3, "reps": 12, "frequency": "2x/week"},
                {"exercise": "Seated Leg Curl", "sets": 3, "reps": 15, "frequency": "2x/week"},
                {"exercise": "High Bar Squat", "sets": 3, "reps": 12, "frequency": "2x/week"},
                {"exercise": "Barbell Row", "sets": 4, "reps": 12, "frequency": "2x/week"},
                {"exercise": "Pull Ups", "sets": 3, "reps": "failure", "frequency": "3x/week"},
                {"exercise": "Hammer Curls", "sets": 3, "reps": 12, "frequency": "3x/week"},
                {"exercise": "Preacher Curls", "sets": 2, "reps": "failure", "frequency": "2x/week"},
                {"exercise": "Dumbbell Lateral Raises", "sets": 4, "reps": 15, "frequency": "2x/week"},
                {"exercise": "Cable Lateral Raises", "sets": 3, "reps": 12, "frequency": "3x/week"}
            ],
            "Lacking Muscle Groups": {
                "Rear Delts": [
                    {"exercise": "Reverse Pec Deck", "sets": 3, "reps": 12, "frequency": "3x/week"},
                    {"exercise": "Single Arm Sideways Reverse Pec Deck", "sets": 3, "reps": 15, "frequency": "2x/week"},
                    {"exercise": "Cable Face Pulls", "sets": 4, "reps": 15, "frequency": "2x/week"}
                ],
                "Traps": [
                    {"exercise": "Smith Machine Shoulder Shrug", "sets": 4, "reps": 12, "frequency": "3x/week"},
                    {"exercise": "Dumbbell Shoulder Shrug", "sets": 3, "reps": 12, "frequency": "2x/week"},
                    {"exercise": "Cable Face Pulls", "sets": 3, "reps": 15, "frequency": "2x/week"},
                    {"exercise": "T-Bar Rows", "sets": 3, "reps": 12, "frequency": "3x/week"}
                ],
                "Calves": [
                    {"exercise": "Standing Smith Machine Calf Raises", "sets": 4, "reps": 20, "frequency": "2x/week"},
                    {"exercise": "Seated Calf Raises", "sets": 4, "reps": 15, "frequency": "2x/week"},
                    {"exercise": "Deficit Calf Raises", "sets": 5, "reps": 25, "frequency": "2x/week"}
                ],
                "Forearms": [
                    {"exercise": "Cable Forearm Curls", "sets": 3, "reps": 15, "frequency": "3x/week"},
                    {"exercise": "Dumbbell Wrist Extension", "sets": 3, "reps": 12, "frequency": "2x/week"},
                    {"exercise": "Dumbbell Wrist Flexion", "sets": 3, "reps": 12, "frequency": "2x/week"},
                    {"exercise": "EZ-Bar Reverse Wrist Curls", "sets": 3, "reps": 20, "frequency": "2x/week"}
                ],
            }
        }
        }



    # Functions


    def encrypt_info(self, info: str):
        return self.cipher.encrypt(info.encode()).decode()
    
    def decrypt_info(self, token: str):
        return self.cipher.decrypt(token.encode()).decode() if isinstance(token, bytes) else self.cipher.decrypt(token.encode("utf-8")).decode()
    

    def hash_password(self, password: str):
        return hashlib.sha256(password.strip().encode()).hexdigest()
    

    def authenticate(self, username, password):
        if not os.path.exists("accounts.txt"):
            return False
        with open("accounts.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) < 2:
                    continue
                stored_user = parts[0].strip()
                stored_pass_hash = parts[1].strip()
                if username.strip() == stored_user and self.hash_password(password) == stored_pass_hash:
                    return True
        return False
    
    def create_new_account(self, username, password):
        username = username.strip()
        password_hash = self.hash_password(password)
        self.client.send("Enter your age: ".encode())
        age = self.client.recv(BUFSIZE).decode().strip()
        encrypted_bio = self.encrypt_info(f"Age: {age}")
        if os.path.exists("accounts.txt") and os.path.getsize("accounts.txt") > 0:
            with open("accounts.txt", "a") as f:
                f.write(f"\n{username},{password_hash},{encrypted_bio}")
        else:
            with open("accounts.txt", "a") as f:
                f.write(f"{username},{password_hash},{encrypted_bio}")

    def load_profile(self, username):
        if not os.path.exists("accounts.txt"):
            return "No profile found"
        with open("accounts.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == username:
                    if len(parts) > 2 and parts[2]:
                        try:
                            return self.decrypt_info(parts[2])
                        except Exception:
                            return "Bio info could not be decrypted"
                    else:
                        return "No bio info found"
        return "No profile found"

    def select_program(self, username):
         # Program Selection Block
        self.client.send(f"{username}, would you like a powerlifting or bodybuilding Program? (Powerlifting/Bodybuilding)".encode())
        choice = self.client.recv(BUFSIZE).decode().strip().capitalize()

        plan = []

        if choice.lower() == "powerlifting":
            self.client.send("Do you want the General Plan or a Specialization Program? (General/Specialization)".encode())
            option = self.client.recv(BUFSIZE).decode().strip().capitalize()
            
            if option.lower() in ["general", "general plan"]:
                plan = self.programs["Powerlifting"]["General Plan"]
            elif option == "Specialization":
                self.client.send("Which specialization would you like? (Squat/Bench/Deadlift)".encode())
                spec = self.client.recv(BUFSIZE).decode().strip().capitalize()
                plan = self.programs["Powerlifting"]["Specializations"].get(spec, [])

        elif choice.lower() == "bodybuilding":
            self.client.send("Do you want the General Plan or do you want to focus on a Common Lacking Muscle Group? (General Plan/Lacking)".encode())
            option = self.client.recv(BUFSIZE).decode().strip().title()

            if option.lower() in ["general", "general plan"]:
                plan = self.programs["Bodybuilding"]["General Plan"]
            elif option == "Lacking":
                self.client.send("Which muscle group would you like to focus on? (Rear Delts/Traps/Calves/Forearms)".encode())
                muscle = self.client.recv(BUFSIZE).decode().strip().title()
                plan = self.programs["Bodybuilding"]["Lacking Muscle Groups"].get(muscle, [])
        
        # Returning the Plan to the User
        if plan:
            self.client.send("Press Enter for your tailored program:".encode())
            for exercise in plan:
                line = f"{exercise['exercise']}: {exercise['sets']}x{exercise['reps']} ({exercise['frequency']})\n"
                self.client.send(line.encode())
                if "progression" in exercise:
                    self.client.send(f"Progression: {exercise['progression']}\n".encode())

            self.client.send("Would you like to quit or go back to choose another program? (Quit/Back)".encode())
            next_action = self.client.recv(BUFSIZE).decode().strip().lower()
            if next_action == "back":
                return self.select_program(username)
            else:
                self.client.send("Thank you for using Serverside Fitness! Goodbye.".encode())
                self.client.close()
                return
        else:
            self.client.send("No plan found or Invalid choice.".encode())
            return

    def run(self):
        self.client.send("Welcome to Serverside Fitness!".encode())

        # Authentication Block
        self.client.send("Do you have a Serverside Fitness Account? (Yes/No): ".encode())
        response = self.client.recv(BUFSIZE).decode().strip()
        if response == "Yes":
            self.client.send("Please Enter Your Username:   ".encode())
            username = self.client.recv(BUFSIZE).decode().strip()
            self.client.send("Please Enter Your Password:   ".encode())
            password = self.client.recv(BUFSIZE).decode().strip()

            if self.authenticate(username, password):
                self.client.send(f"Login successful! Welcome back {username}! Please press Enter to continue".encode())
                bio_info = self.load_profile(username)
                self.client.send(f"Your profile: {bio_info}\n".encode())
                self.select_program(username)
                return
            else:
                self.client.send("Invalid credentials. Connection closing".encode())
                self.client.close()
                return
        
        # Account Creation Block
        elif response == "No":
            self.client.send("Enter a new username:    ".encode())
            username = self.client.recv(BUFSIZE).decode().strip()
            self.client.send("Enter a new password:    ".encode())
            password = self.client.recv(BUFSIZE).decode().strip()
            self.create_new_account(username,password)
            self.client.send("Account created successfully! Please press Enter to continue".encode())

        # Calls Program Selection Function
        self.select_program(username)
        return

