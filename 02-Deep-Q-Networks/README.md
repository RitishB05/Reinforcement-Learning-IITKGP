# Deep Q-Networks (DQN) for Discrete Control

## Project Overview
Implementing a stable DQN agent to solve the Gymnasium CartPole-v1 control task using PyTorch.

## Mathematical Foundations
- Bellman Optimality: Approximating the optimal action-value function Q*(s, a).
- Stability Mechanisms: Implementation of Experience Replay and Target Networks to reduce temporal correlation and target oscillation.
- Loss Function: Minimizing Mean Squared Error (MSE) between the predicted Q-values and Temporal Difference (TD) targets.

## Implementation Details
- Experience Replay: Circular buffer for uniform sampling of historical transitions.
- Target Network: A quasi-static network updated periodically to stabilize the learning objective.
- Epsilon-Decay: Strategy for smooth transition from exploration to exploitation.

## Technologies Used
- Python, PyTorch, Gymnasium (OpenAI Gym), NumPy, Matplotlib
