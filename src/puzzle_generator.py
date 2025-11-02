import random

LEVEL_EASY = 1
LEVEL_MEDIUM = 2
LEVEL_HARD = 3

def generate_puzzle(level):
    """
    Generates a math puzzle (problem, answer) based on the difficulty level.
    """
    if level == LEVEL_EASY:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        problem = f"{a} + {b}"
        answer = a + b
    
    elif level == LEVEL_MEDIUM:
        if random.choice([True, False]):
            a = random.randint(10, 99)
            b = random.randint(10, 99)
            problem = f"{a} + {b}"
            answer = a + b
        else:
            a = random.randint(20, 99)
            b = random.randint(10, a - 1) 
            problem = f"{a} - {b}"
            answer = a - b
            
    elif level == LEVEL_HARD:
        if random.choice([True, False]):
            a = random.randint(2, 20)
            b = random.randint(2, 20)
            problem = f"{a} * {b}"
            answer = a * b
        else:
            b = random.randint(2, 20)
            answer = random.randint(2, 20)
            a = a = b * answer
            problem = f"{a} / {b}"
            answer = answer

    return problem, answer

if __name__ == '__main__':
    print(f"Easy puzzle:   {generate_puzzle(LEVEL_EASY)}")
    print(f"Medium puzzle: {generate_puzzle(LEVEL_MEDIUM)}")
    print(f"Hard puzzle:   {generate_puzzle(LEVEL_HARD)}")