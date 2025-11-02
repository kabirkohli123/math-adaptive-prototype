import time

from .puzzle_generator import generate_puzzle, LEVEL_EASY, LEVEL_MEDIUM, LEVEL_HARD
from .tracker import PerformanceTracker
from .adaptive_engine import AdaptiveEngine

def get_initial_level():
    """Gets the starting difficulty from the user."""
    while True:
        print("Choose your starting difficulty:")
        print("1: Easy")
        print("2: Medium")
        print("3: Hard")
        choice = input("Enter (1, 2, or 3): ")
        if choice == '1':
            return LEVEL_EASY
        elif choice == '2':
            return LEVEL_MEDIUM
        elif choice == '3':
            return LEVEL_HARD
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main_game_loop():
    """Runs the main application flow."""
    
    # 1. Start 
    print("---  Welcome to Math Adventures!  ---")
    start_level = get_initial_level()
    
    engine = AdaptiveEngine(start_level)
    tracker = PerformanceTracker()
    
    num_puzzles = 10 
    print(f"\nStarting session with {num_puzzles} puzzles. Good luck!\n")

    for i in range(num_puzzles):
        print(f"--- Puzzle {i+1} of {num_puzzles} ---")
        
        # 2. Get puzzle 
        current_level = engine.get_current_level()
        problem, correct_answer = generate_puzzle(current_level)
        
        # 3. Track Performance
        start_time = time.time()
        
        user_answer_str = input(f"Level {current_level} | What is {problem}? ")
        
        end_time = time.time()
        time_taken = end_time - start_time
        
        try:
            user_answer = int(user_answer_str)
            is_correct = (user_answer == correct_answer)
        except ValueError:
            is_correct = False 
            
        if is_correct:
            print(f"✅ Correct! (Took {time_taken:.2f}s)")
        else:
            print(f" Incorrect. The answer was {correct_answer}.")
            
        tracker.log_result(current_level, problem, is_correct, time_taken)
        
        # 4. Adaptive Logic 
        engine.update_level(is_correct, time_taken)
        print("-" * 20) 

    # 5. Summary
    print("\n🏁 Session Complete! 🏁")
    print(tracker.get_summary())
    
    print(f"Based on your performance, we recommend you start at \
Level {engine.get_current_level()} next time.")


if __name__ == "__main__":
    main_game_loop()