import os
import shutil

# Folder structure and high-detail content
structure = {
    "01-Multi-Armed-Bandits": {
        "files": ["Multi_Armed_Bandits_Exploration_Strategies.py", "Multi_Armed_Bandits_Exploration_Strategies.ipynb"],
        "title": "Multi-Armed Bandits: Exploration-Exploitation Trade-off",
        "desc": "A study on regret minimization in stochastic environments using classical bandit algorithms.",
        "mathematics": [
            "Regret Analysis: Theoretical comparison of cumulative regret bounds.",
            "Upper Confidence Bound (UCB): Implementing confidence intervals using the Hoeffding Inequality.",
            "Epsilon-Greedy: Balancing exploration vs. exploitation through a probability parameter."
        ],
        "highlights": [
            "Comparative study of Epsilon-Greedy, UCB, and Thompson Sampling.",
            "Simulation across stationary Gaussian reward distributions.",
            "Analysis of convergence rates based on Cumulative Regret curves."
        ]
    },
    "02-Deep-Q-Networks": {
        "files": ["Deep_Q_Learning_CartPole_PyTorch.py", "Deep_Q_Learning_CartPole_PyTorch.ipynb"],
        "title": "Deep Q-Networks (DQN) for Discrete Control",
        "desc": "Implementing a stable DQN agent to solve the Gymnasium CartPole-v1 control task.",
        "mathematics": [
            "Bellman Optimality: Approximating the Q-value function using Neural Networks.",
            "Target Networks: Using a quasi-static network to reduce target oscillations and ensure stability.",
            "MSE Loss: Minimizing the Temporal Difference (TD) error."
        ],
        "architecture": [
            "Experience Replay: Utilizing a circular buffer to remove temporal correlations in transitions.",
            "Epsilon-Decay: Annealing the exploration rate from 1.0 to 0.01 for better optimization.",
            "Framework: Neural network implementation using PyTorch with Adam optimizer."
        ]
    }
}

# 1. Create Structure
for folder, data in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file_name in data['files']:
        if os.path.exists(file_name):
            shutil.move(file_name, os.path.join(folder, file_name))

    # 2. Detailed Sub-folder README
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write(f"# {data['title']}\n\n")
        f.write(f"## Overview\n{data['desc']}\n\n")
        
        f.write("## Mathematical & Technical Foundations\n")
        if "mathematics" in data:
            for math in data['mathematics']: f.write(f"- {math}\n")
        
        f.write("\n## Implementation Details\n")
        details = data.get("highlights") or data.get("architecture")
        for item in details: f.write(f"- {item}\n")
        
        f.write("\n## Technologies\n- PyTorch, Gymnasium (OpenAI Gym), NumPy, Matplotlib\n")

# 3. Jist/Main README
with open("README.md", "w") as f:
    f.write("# Reinforcement Learning Labs\n")
    f.write("### M.Tech AI | IIT Kharagpur\n\n")
    f.write("This repository contains implementations of RL algorithms, covering fundamental bandit problems and Deep Q-Networks.\n\n")
    f.write("## Project Jist\n")
    for folder in sorted(structure.keys()):
        f.write(f"- **[{structure[folder]['title']}](./{folder})**: {structure[folder]['desc']}\n")

print("RL Labs organized with high-detail documentation!")