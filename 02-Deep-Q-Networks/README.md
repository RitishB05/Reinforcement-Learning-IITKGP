# Deep Q-Networks (DQN) for Discrete Control

## Overview
Implementing a stable DQN agent to solve the Gymnasium CartPole-v1 control task.

## Mathematical & Technical Foundations
- Bellman Optimality: Approximating the Q-value function using Neural Networks.
- Target Networks: Using a quasi-static network to reduce target oscillations and ensure stability.
- MSE Loss: Minimizing the Temporal Difference (TD) error.

## Implementation Details
- Experience Replay: Utilizing a circular buffer to remove temporal correlations in transitions.
- Epsilon-Decay: Annealing the exploration rate from 1.0 to 0.01 for better optimization.
- Framework: Neural network implementation using PyTorch with Adam optimizer.

## Technologies
- PyTorch, Gymnasium (OpenAI Gym), NumPy, Matplotlib
