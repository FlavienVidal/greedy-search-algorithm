# greedy-search-algorithm
Here is a basic search algorithm.

Search algorithms are one of the most important areas of Artificial Intelligence. They are usually approaches to solving problems for which we start from a given state, and by performing a series of different possible actions, we seek to reach a goal state. For example, when searching for the shortest path to go from an initial position to a final position, or when searching for the best sequence of actions to win a game. All these types of problems can be represented as a tree.

In this example the agent has at disposal pitchers P3 and P5 that can contain exactly 3L and 5L of liquid.
-	Initial state: P3 = 0L and P5 = 0L (empty)
-	Goal state: P5 = 4L
To achieve this objective, the agent can choose between 5 possible actions at each state:
-	action 1: fill P3 with water from the tap
-	action 2: pour the content of P3 into P5
-	action 3: pour the content of P5 into P3
-	action 4: empty the liquid content of P3
-	action 5: empty the liquid content of P5

We do not have any additional information that we can give the algorithm so that the agent can find the goal state more efficiently. The only solution would be to assess the volume of water for each possible state and choose the one that is the closest to goal state “G: P5 = 4L” but here it is meaningless: having P5 = 3L doesn’t mean that this state is a better state than P5 = 2L.
Thus, we are going to use a uniformed search algorithm. In order to determine an optimal sequence of actions the agent should take to reach the goal state we are thus going to use breadth-first search (BFS) (depth-first search is not optimal).

We first need to code the five possible actions.
Then, we need to code the breadth-first search algorithm. It will compute all the possible states, keep memory of all potential states that the algorithm will potentially visit in the future (frontier), and create an ordered sequence of actions that the algorithm is visiting (path).
Once we have the ordered sequence of action the algorithm is visiting (path), we need to get the optimal sequence of actions the agent should take to reach the goal state.
Finally, we initialize the capacity of pitchers P3 and P5 and print the results.

Proprieties of the greedy search algorithm:
- Complete: yes
- Optimal: yes
- Time complexity: can be slow if the problem is more complex
- Space complexity: requires memory to explore all branches of all layers
