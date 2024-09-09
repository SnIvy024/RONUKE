def chapter_3_intro():
    print("The research facility is filled with an aura of secrets.")
    while True:
        next_action = input("Do you want to examine lab equipment, read research logs, or find the hidden passage? (equipment/logs/passage): ")
        if next_action.lower() == "equipment":
            return examine_lab_equipment()  #return here
        elif next_action.lower() == "logs":
            return read_research_logs()  #return here
        elif next_action.lower() == "passage":
            return find_hidden_passage()
        else:
            print("Invalid choice. Please try again.")

def examine_lab_equipment():
    print("You examine the broken lab equipment.")
    while True:
        next_action = input("Do you want to read research logs? (logs): ")
        if next_action.lower() == "logs":
            return read_research_logs()  #return here
        else:
            print("Invalid choice. Please try again.")

def read_research_logs():
    print("You read the research logs.")
    while True:
        next_action = input("Do you want to examine lab equipment or find the hidden passage? (equipment/passage): ")
        if next_action.lower() == "equipment":
            return examine_lab_equipment()  #return here
        elif next_action.lower() == "passage":
            return find_hidden_passage()
        else:
            print("Invalid choice. Please try again.")

def find_hidden_passage():
    print("You find a hidden passage leading to the artifact chamber.")
    return 'chapter_4'  # Correct transition to Chapter 4


