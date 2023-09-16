# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
import heapq
from heapq import heappush, heappop
from lab2_utils import TextbookStack, apply_sequence
from collections import deque


def calculate_heuristic(stack: TextbookStack):
    num_books = stack.num_books
    orientations = stack.orientations
    order = stack.order

    # Initialize variables to count different types of pairs
    type_1_pairs = 0
    type_2_pairs = 0
    type_3_pairs = 0
    type_4_pairs = 0

    for i in range(num_books):
        for j in range(i + 1, num_books):
            book_i = order[i]
            book_j = order[j]
            orient_i = orientations[i]
            orient_j = orientations[j]

            # Condition (a): If the pair of books are not adjacent in the ordered stack
            if abs(book_i - book_j) > 1:
                type_1_pairs += 1

            # Condition (b): If the pair has a book facing up and one facing down
            if (orient_i == 1 and orient_j == 0) or (orient_i == 0 and orient_j == 1):
                type_2_pairs += 1

            # Condition (c): If the pair is wrongly ordered but with correct orientations
            if book_i > book_j and orient_i == 1 and orient_j == 1:
                type_3_pairs += 1

            # Condition (d): If the pair is correctly ordered but with wrong orientations
            if book_i < book_j and orient_i == 0 and orient_j == 0:
                type_4_pairs += 1

    # Calculate the total heuristic value as a sum of all types
    total_heuristic = type_1_pairs + type_2_pairs + type_3_pairs + type_4_pairs

    return total_heuristic


def a_star_search(stack):
    flip_sequence = []
    open_set = [(0, stack)]  # Initialize the open set with (f, stack)
    while open_set:
        # Pop the state with the lowest f value (f, stack) from the priority queue
        _, current_stack = heappop(open_set)

        # Calculate the heuristic value for the current stack
        h = calculate_heuristic(current_stack)

        # Check if the goal state is reached
        if current_stack.check_ordered():
            # Generate the sequence of actions (flips) from the root to the current node
            while current_stack is not stack:
                flip_sequence.insert(0, current_stack.order[0] + 1)
                current_stack = current_stack.parent
            return flip_sequence

        # Generate successor stacks (apply all possible flips)
        for flip_position in range(1, current_stack.num_books + 1):
            successor_stack = stack.copy()
            apply_sequence(successor_stack, flip_sequence + [flip_position])

            # Calculate the cost g for the successor stack
            successor_g = len(flip_sequence) + 1

            # Calculate the heuristic value h for the successor stack
            successor_h = calculate_heuristic(successor_stack)

            # Calculate the f value for the successor stack
            f = successor_g + successor_h

            # Add the successor stack to the open set
            heappush(open_set, (f, successor_stack))

    # If no solution is found, return an empty flip_sequence
    return flip_sequence


def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
