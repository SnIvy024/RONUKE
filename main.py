# main.py

# Import chapters
from chapter_1 import chapter_1_intro
from chapter_2 import chapter_2_intro
from chapter_3 import chapter_3_intro
from chapter_4 import chapter_4_intro
from chapter_5 import chapter_5_intro

def end_game():
    print("Thank you for playing! The fate of Ronuke and your decisions will linger in memory.")

def main():
    # start the game with the introduction chapter
    next_chapter = 'chapter_1'
    artifact_status = None  # To track the status of the artifact

    # Dictionary to reference chapter functions by name
    chapters = {
        'chapter_1': chapter_1_intro,
        'chapter_2': chapter_2_intro,
        'chapter_3': chapter_3_intro,
        'chapter_4': chapter_4_intro
    }

    # Game loop to continue game flow based on the returned value from each chapter
    while next_chapter != 'end_game':
        print(f"Transitioning to {next_chapter}") #Print the current chapter to transition to
        next_chapter_function = chapters.get(next_chapter, None)

        if next_chapter_function:
            # chapter function and get the next chapter
            next_chapter = next_chapter_function()
            print(f"Next chapter after function call: {next_chapter}")  # Debug: Print the next chapter to be executed

            #specific transitions related to the artifact
            if next_chapter == 'artifact_taken':
                artifact_status = 'artifact_taken'
                next_chapter = 'chapter_5'
            elif next_chapter == 'artifact_left':
                artifact_status = 'artifact_left'
                next_chapter = 'chapter_5'

            if next_chapter == 'chapter_5':
                next_chapter = chapter_5_intro(artifact_status)

        else:
            print(f"Error: Chapter identifier '{next_chapter}' not found or invalid return from function. Ending game.")
            break

    #the loop completes
    end_game()

if __name__ == "__main__":
    main()
