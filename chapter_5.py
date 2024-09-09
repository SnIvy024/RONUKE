def chapter_5_intro(artifact_status):
    if artifact_status == 'artifact_taken':
        print("With the artifact in your possession, you feel its power influencing everything around you.")
    elif artifact_status == 'artifact_left':
        print("You left the artifact behind, a decision that weighs heavily on your mind as you proceed.")
    else:
        print("Continuing without a clear decision on the artifact...")

    while True:
        next_action = input("Analyze the final logs, send a distress signal, or prepare for departure? (logs/signal/departure): ")
        if next_action.lower() == "logs":
            return analyze_final_logs()
        elif next_action.lower() == "signal":
            return send_distress_signal()
        elif next_action.lower() == "departure":
            return prepare_for_departure()
        else:
            print("Invalid choice. Please try again.")

def analyze_final_logs():
    print("You pour over the logs, uncovering hidden truths about the colony's last days.")
    return 'end_game'

def send_distress_signal():
    print("You send out a distress signal, hoping that someone will heed the call.")
    return 'end_game'

def prepare_for_departure():
    print("You prepare your ship for the journey back home, reflecting on your experiences.")
    return 'end_game'

def end_game():
    print("Thank you for playing! The fate of Ronuke and your decisions will linger in memory.")

#FINALLY I FINISHED THE GAME THIS WAS THE HARDEST THING I DID AT NLU I KNOW PYTHON A BIT BUT THIS WAS CRAZY
