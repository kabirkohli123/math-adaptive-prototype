from .puzzle_generator import LEVEL_EASY, LEVEL_MEDIUM, LEVEL_HARD

FAST_THRESHOLD = 5.0 # seconds

SCORE_FAST_CORRECT = 2
SCORE_SLOW_CORRECT = 1
SCORE_INCORRECT = -2

LEVEL_UP_THRESHOLD = 5
LEVEL_DOWN_THRESHOLD = -3

class AdaptiveEngine:
    """
    Uses rule-based logic to decide the next difficulty level.
    """
    def __init__(self, initial_level):
        self.current_level = initial_level
        self.level_score = 0
        print(f"AdaptiveEngine initialized. Start level: {self.current_level}, Score: 0")

    def get_current_level(self):
        return self.current_level

    def update_level(self, correct, time_taken):
        """
        Updates the score and level based on the last puzzle's performance.
        Returns the *next* level.
        """
        
        # 1. Update the score
        if correct:
            if time_taken < FAST_THRESHOLD:
                self.level_score += SCORE_FAST_CORRECT
                print(f"  > Performance: FAST & CORRECT. Score +{SCORE_FAST_CORRECT}")
            else:
                self.level_score += SCORE_SLOW_CORRECT
                print(f"  > Performance: SLOW & CORRECT. Score +{SCORE_SLOW_CORRECT}")
        else:
            self.level_score += SCORE_INCORRECT
            print(f"  > Performance: INCORRECT. Score {SCORE_INCORRECT}")
            
        print(f"  > New score for this level: {self.level_score}")

        # 2. Check for level transitions
        if self.level_score >= LEVEL_UP_THRESHOLD:
            self.level_up()
        elif self.level_score <= LEVEL_DOWN_THRESHOLD:
            self.level_down()
        
        print(f"  > Next puzzle level: {self.current_level}")
        return self.current_level

    def level_up(self):
        """Increases difficulty and resets score."""
        if self.current_level == LEVEL_EASY:
            self.current_level = LEVEL_MEDIUM
            print("  *** LEVEL UP! -> MEDIUM ***")
        elif self.current_level == LEVEL_MEDIUM:
            self.current_level = LEVEL_HARD
            print("  *** LEVEL UP! -> HARD ***")
        
        self.level_score = 0

    def level_down(self):
        """Decreases difficulty and resets score."""
        if self.current_level == LEVEL_HARD:
            self.current_level = LEVEL_MEDIUM
            print("  *** LEVEL DOWN! -> MEDIUM ***")
        elif self.current_level == LEVEL_MEDIUM:
            self.current_level = LEVEL_EASY
            print("  *** LEVEL DOWN! -> EASY ***")
            
        self.level_score = 0