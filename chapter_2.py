def chapter_2_intro():
    print("The residential area was a ghost town, with homes left in disarray. The wind carried whispers of a forgotten panic.")
    
    while True:
        next_action = input("Do you want to investigate homes, access personal logs, or visit the marketplace? (homes/logs/marketplace): ")
        if next_action.lower() == "homes":
            return investigate_homes()
        elif next_action.lower() == "logs":
            return access_personal_logs()
        elif next_action.lower() == "marketplace":
            return visit_marketplace()
        else:
            print("Invalid choice. Please try again.")

def investigate_homes():
    print("You start investigating the deserted homes, finding personal belongings and cryptic messages.")
    
    while True:
        next_action = input("Do you want to access personal logs or move to the research facility? (logs/research): ")
        if next_action.lower() == "logs":
            return access_personal_logs()
        elif next_action.lower() == "research":
            result = move_to_research_facility()
            print(f"Transitioning to {result} from investigate_homes")
            return result
        else:
            print("Invalid choice. Please try again.")

def access_personal_logs():
    print("You access personal logs, discovering hints about a mysterious outbreak.")
    
    while True:
        next_action = input("Do you want to visit the marketplace or move to the research facility? (marketplace/research): ")
        if next_action.lower() == "marketplace":
            return visit_marketplace()
        elif next_action.lower() == "research":
            result = move_to_research_facility()
            print(f"Transitioning to {result} from access_personal_logs")
            return result
        else:
            print("Invalid choice. Please try again.")

def visit_marketplace():
    print("You visit the abandoned marketplace, gathering supplies.")
    
    while True:
        next_action = input("Do you want to investigate homes or move to the research facility? (homes/research): ")
        if next_action.lower() == "homes":
            return investigate_homes()
        elif next_action.lower() == "research":
            result = move_to_research_facility()
            print(f"Transitioning to {result} from visit_marketplace")
            return result
        else:
            print("Invalid choice. Please try again.")

def move_to_research_facility():
    print("You move to the research facility. The air is thick with the remnants of the colony who has turned to horrific beings.")
    print("Transitioning to chapter_3")
    return 'chapter_3'  #transition to Chapter 3



