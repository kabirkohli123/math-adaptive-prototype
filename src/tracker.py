class PerformanceTracker:
    """
    A simple class to log metrics for each puzzle.
    """
    def __init__(self):
        self.history = []

    def log_result(self, level, problem, correct, time_taken):
        """Logs the performance of a single puzzle."""
        result = {
            "level": level,
            "problem": problem,
            "correct": correct,
            "time_taken": time_taken
        }
        self.history.append(result)
        print(f"Logged: {result}") 

    def get_history(self):
        """Returns the full performance history."""
        return self.history

    def get_summary(self):
        """Generates an end-of-session performance summary."""
        if not self.history:
            return "No puzzles attempted."

        total_puzzles = len(self.history)
        total_correct = sum(1 for r in self.history if r["correct"])
        total_time = sum(r["time_taken"] for r in self.history)
        
        accuracy = (total_correct / total_puzzles) * 100
        avg_time = total_time / total_puzzles

        summary = (
            f"\n--- Session Summary ---\n"
            f"Total Puzzles: {total_puzzles}\n"
            f"Accuracy:        {accuracy:.2f}%\n"
            f"Average Time:    {avg_time:.2f} seconds\n"
        )
        return summary