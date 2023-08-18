# 5D Sort With Multiverse Time Travel
A sorting algorithm based on the game [5D Chess With Multiverse Time Travel](https://store.steampowered.com/app/1349230/5D_Chess_With_Multiverse_Time_Travel/). The algorithm is meant as a joke and has no real application.

- [5D Sort With Multiverse Time Travel](#5d-sort-with-multiverse-time-travel)
  - [Basic game rules](#basic-game-rules)
    - [The new axes](#the-new-axes)
    - [Playable boards](#playable-boards)
    - [Extra Rules](#extra-rules)
  - [Game to algorithm transformation](#game-to-algorithm-transformation)
    - [Notes](#notes)
  - [Future ideas](#future-ideas)


## Basic game rules
Check [this tutorial](https://5d-chess.fandom.com/wiki/Tutorial) for a more in-depth explanation.
Broken down, 5D Sort With Multiverse Time Travel (shortened 5DC) is a fancy name for an easy concept.
Think of a chess board as coordinates. 5DC adds a coordinate system consisting of multiple chess boards. Pieces can move between boards. The new system has the axes time (t) and multiverse (m).
### The new axes 
When playing a normal chess move, a new board appears on the left on the t-axis instead of updating the old board. This makes the t-axis show a history of moves. A piece can move backwards ('go back in time') on this line. If a piece does so, the target board copies on the m-axis. The time-traveling piece moves to the copy while the original board and timeline stay unchanged. Pieces can also move vertically between playable boards.
### Playable boards
5DC has an indicator called 'the present'. The present is always on the left-most playable board. Players must play a move on all boards without a future (haha) in the present. Players can optionally play a move on future boards. Checkmates only count on boards in the present, not in the future.  
### Extra Rules
- Time-travel is only possible to boards where it was the current players' move (every 2nd board).
- A player can split on the m-axis 2 more times than the opponent.

## Game to algorithm transformation
| Game             | Algorithm                                  |
| ---------------- | ------------------------------------------ |
| Chess board      | Sortable array                             |
| Basic chess move | One iteration of a basic sorting algorithm |
| t-m-axes move    | Move between arrays based on game rules    |
| Checkmate        | Sorted array                               |
### Notes
- The basic sorting algorithm is currently **bubble sort**
- The 3 basic actions 'Move on board', 'Move on t-axis', 'Move on m-axis' are chosen at random 
- The algorithm finishes if a sorted array is found in a playable array in the present (i.e if a checkmate is possible in the game)  
- 5DC pieces have different rules of moving in the t-m-axes based on their usual movement. The algorithm does not account for that and values can move freely to possible boards.
- A value is moved between arrays by keeping its index

## Future ideas
- Support duplicates.
- Assign the values chess pieces and implement the movement patterns of the game.  
- Choose between the 3 basic actions usefully instead of random (if possible).
- The concept of splitting up arrays for sorting seems similar to a Divide-and-Conquer algorithm. Maybe the algorithm can be ported to something like Merge-Sort which would be more interesting than an unnecessarily complicated bubble sort.