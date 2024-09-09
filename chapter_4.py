def chapter_4_intro():
    print("The chamber was cold and dark.")
    while True:
        next_action = input("Do you want to study the artifact, access security recordings, or decide to take or leave the artifact? (study/recordings/decide): ")
        if next_action.lower() == "study":
            return study_artifact()
        elif next_action.lower() == "recordings":
            return access_security_recordings()
        elif next_action.lower() == "decide":
            return decide_artifact_fate()
        else:
            print("Invalid choice. Please try again.")

def study_artifact():
    print("You study the artifact, learning more about its mysterious origins and potentially dangerous capabilities.")
    return 'chapter_5'  # Directly returns 'chapter_5', to the next chapter.

def access_security_recordings():
    print("You access the security recordings, revealing the events that led to the current desolation of the artifact's chamber.")
    return 'chapter_5'  # Directly returns 'chapter_5', signaling a transition.

def decide_artifact_fate():
    print("You stand before the artifact, deciding whether to take it or leave it behind.")
    while True:
        decision = input("Do you want to take the artifact or leave it? (take/leave): ")
        if decision.lower() == "take":
            print("You have chosen to take the artifact, a choice that may have significant consequences.")
            return 'artifact_taken'  # Returns 'artifact_taken', will be handled by 'main.py' to determine outcomes.
        elif decision.lower() == "leave":
            print("You decide to leave the artifact behind, hoping that it is for the best.")
            return 'artifact_left'  # Returns 'artifact_left', will move the narrative towards a different path in Chapter 5.
        else:
            print("Invalid choice. Please try again.")

