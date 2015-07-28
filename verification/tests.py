"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [(4, 7, 7, 5), (1, 2, 1, 5), (1, 5, 4, 7), (1, 2, 7, 2)],
            "answer": [(4, 7, 7, 5), (1, 2, 1, 5), (1, 5, 4, 7), (1, 2, 7, 2)],
        },
        {
            "input": [(1, 2, 1, 5), (1, 2, 7, 2), (7, 5, 1, 2), (4, 7, 7, 5), (1, 5, 4, 7), (7, 5, 7, 2), (1, 5, 7, 2)],
            "answer": [],
        },
        {
            "input": [(1, 2, 1, 5), (1, 2, 7, 2), (7, 5, 1, 2), (4, 7, 7, 5), (1, 5, 4, 7), (7, 5, 7, 2), (1, 5, 7, 5),
                      (1, 5, 7, 2)],
            "answer": [(1, 2, 1, 5), (1, 2, 7, 2), (7, 5, 1, 2), (4, 7, 7, 5), (1, 5, 4, 7), (7, 5, 7, 2), (1, 5, 7, 5),
                       (1, 5, 7, 2)],
        },
    ],
    "Edge": [
        {
            "input": [(1, 1, 9, 9)],
            "answer": [(1, 1, 9, 9)],
        },
        {
            "input": [(1, 1, 1, 99), (99, 99, 1, 99), (99, 99, 99, 1), (99, 1, 1, 1)],
            "answer": [(1, 1, 1, 99), (99, 99, 1, 99), (99, 99, 99, 1), (99, 1, 1, 1)],
        },
        {
            "input": [(8, 4, 8, 6), (4, 8, 6, 2), (6, 8, 8, 6), (4, 8, 8, 6), (2, 6, 4, 2), (6, 2, 8, 4), (6, 8, 6, 2),
                      (2, 6, 6, 2), (2, 4, 8, 4), (6, 8, 8, 4), (4, 2, 6, 2), (4, 2, 8, 6), (2, 4, 2, 6), (4, 2, 6, 8),
                      (4, 2, 4, 8), (2, 4, 6, 2), (2, 4, 4, 8), (4, 8, 6, 8), (6, 2, 8, 6), (4, 8, 8, 4), (2, 6, 8, 6),
                      (2, 6, 6, 8), (2, 4, 4, 2), (4, 2, 8, 4), (2, 4, 6, 8), (2, 6, 4, 8), (2, 6, 8, 4), (2, 4, 8, 6)],
            "answer": [],
        },
        {
            "input": [(4, 2, 6, 8), (2, 4, 6, 2), (4, 8, 6, 2), (2, 4, 6, 8), (6, 8, 6, 2), (6, 2, 8, 4), (4, 2, 8, 4),
                      (2, 6, 4, 8), (2, 6, 6, 8), (2, 6, 4, 2), (4, 2, 4, 8), (2, 4, 4, 8), (4, 8, 6, 8), (2, 4, 4, 2),
                      (2, 4, 8, 4), (6, 8, 8, 4), (2, 6, 6, 2), (2, 6, 8, 4), (4, 2, 6, 2), (4, 8, 8, 4), (2, 4, 2, 6)],
            "answer": [(4, 2, 6, 8), (2, 4, 6, 2), (4, 8, 6, 2), (2, 4, 6, 8), (6, 8, 6, 2), (6, 2, 8, 4), (4, 2, 8, 4),
                       (2, 6, 4, 8), (2, 6, 6, 8), (2, 6, 4, 2), (4, 2, 4, 8), (2, 4, 4, 8), (4, 8, 6, 8), (2, 4, 4, 2),
                       (2, 4, 8, 4), (6, 8, 8, 4), (2, 6, 6, 2), (2, 6, 8, 4), (4, 2, 6, 2), (4, 8, 8, 4),
                       (2, 4, 2, 6)],
        },
    ],
    "Extra": [
        {
            "input": [(97, 8, 3, 3), (3, 3, 50, 50), (50, 50, 97, 8)],
            "answer": [(97, 8, 3, 3), (3, 3, 50, 50), (50, 50, 97, 8)],
        },
        {
            "input": [(50, 40, 60, 40), (60, 10, 70, 20), (20, 40, 30, 40), (50, 10, 60, 10), (30, 10, 40, 25),
                      (10, 30, 20, 40), (40, 25, 50, 10), (30, 40, 40, 25), (20, 10, 30, 10), (10, 20, 10, 30),
                      (60, 40, 70, 30), (10, 20, 20, 10), (40, 25, 50, 40), (70, 30, 70, 20)],
            "answer": [(50, 40, 60, 40), (60, 10, 70, 20), (20, 40, 30, 40), (50, 10, 60, 10), (30, 10, 40, 25),
                       (10, 30, 20, 40), (40, 25, 50, 10), (30, 40, 40, 25), (20, 10, 30, 10), (10, 20, 10, 30),
                       (60, 40, 70, 30), (10, 20, 20, 10), (40, 25, 50, 40), (70, 30, 70, 20)],
        },
        {
            "input": [(11, 11, 55, 66), (22, 33, 33, 56), (22, 33, 55, 66), (11, 11, 22, 33), (55, 66, 33, 56)],
            "answer": [(11, 11, 55, 66), (22, 33, 33, 56), (22, 33, 55, 66), (11, 11, 22, 33), (55, 66, 33, 56)],
        },
        {
            "input": [(55, 30, 55, 55), (40, 20, 55, 55), (55, 30, 70, 44), (10, 50, 55, 55), (10, 50, 40, 20),
                      (40, 20, 70, 44), (40, 20, 55, 30), (55, 55, 70, 44), (10, 50, 55, 30), (10, 50, 70, 44)],
            "answer": [(55, 30, 55, 55), (40, 20, 55, 55), (55, 30, 70, 44), (10, 50, 55, 55), (10, 50, 40, 20),
                       (40, 20, 70, 44), (40, 20, 55, 30), (55, 55, 70, 44), (10, 50, 55, 30), (10, 50, 70, 44)],
        },
        {
            "input": [(1, 1, 2, 2), (2, 1, 2, 2), (2, 1, 3, 2), (2, 1, 3, 1), (1, 1, 0, 2), (1, 1, 0, 0), (3, 2, 3, 1),
                      (0, 0, 0, 2)],
            "answer": [(1, 1, 2, 2), (2, 1, 2, 2), (2, 1, 3, 2), (2, 1, 3, 1), (1, 1, 0, 2), (1, 1, 0, 0), (3, 2, 3, 1),
                       (0, 0, 0, 2)],
        },
        {
            "input": [(0, 0, 0, 1), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 3, 0),
                      (3, 0, 4, 0), (3, 0, 4, 1), (4, 0, 4, 1)],
            "answer": [(0, 0, 0, 1), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 3, 0),
                       (3, 0, 4, 0), (3, 0, 4, 1), (4, 0, 4, 1)],
        },
    ],
}
