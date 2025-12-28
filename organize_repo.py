import os
import shutil

# Folder structure and high-detail content
structure = {
    "01-Multi-Armed-Bandits": {
        "files": ["Multi_Armed_Bandits_Exploration_Strategies.py", "Multi_Armed_Bandits_Exploration_Strategies.ipynb"],
        "title": "Multi-Armed Bandits: Exploration-Exploitation Strategies",
        "desc": "An in-depth study of the fundamental exploration-exploitation trade-off using classical Bandit algorithms.",
        "math": [
            "Regret Bounds: Comparison of cumulative regret across epsilon-greedy, UCB, and Thompson Sampling.",
            "UCB Algorithm: Implementing Upper Confidence Bounds using Hoeffding's Inequality to minimize regret.",
            "Thompson Sampling: Bayesian approach using Beta distributions for optimal action selection."
        ],
        "analysis": "Evaluation focused on stationary vs. non-stationary reward distributions, demonstrating how the agent adapts its internal value estimates over 10,000+ iterations."
    },
    "02-Deep-Q-Networks": {
        "files": ["Deep_Q_Learning_CartPole_PyTorch.py", "Deep_Q_Learning_CartPole_PyTorch.ipynb"],
        "title": "Deep Q-Networks (DQN) for Discrete Control",
        "desc": "Implementing a stable DQN agent to solve the Gymnasium CartPole-v1 control task using PyTorch.",
        "math": [
            "Bellman Optimality: Approximating the optimal action-value function Q*(s, a).",
            "Stability Mechanisms: Implementation of Experience Replay and Target Networks to reduce temporal correlation and target oscillation.",
            "Loss Function: Minimizing Mean Squared Error (MSE) between the predicted Q-values and Temporal Difference (TD) targets."
        ],
        "architecture": [
            "Experience Replay: Circular buffer for uniform sampling of historical transitions.",
            "Target Network: A quasi-static network updated periodically to stabilize the learning objective.",
            "Epsilon-Decay: Strategy for smooth transition from exploration to exploitation."
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
        f.write(f"## Project Overview\n{data['desc']}\n\n")
        
        f.write("## Mathematical Foundations\n")
        for m in data['math']: f.write(f"- {m}\n")
        
        f.write("\n## Implementation Details\n")
        details = data.get("analysis") or data.get("architecture")
        if isinstance(details, list):
            for item in details: f.write(f"- {item}\n")
        else:
            f.write(f"{details}\n")
        
        f.write("\n## Technologies Used\n- Python, PyTorch, Gymnasium (OpenAI Gym), NumPy, Matplotlib\n")

# 3. Global README (The Jist)
with open("README.md", "w") as f:
    f.write("# Reinforcement Learning Labs\n")
    f.write("### M.Tech AI | IIT Kharagpur\n\n")
    f.write("This repository contains implementations of RL algorithms, covering both classical multi-armed bandit problems and Deep Reinforcement Learning methods.\n\n")
    f.write("## Repository Index (Jist)\n")
    for folder in sorted(structure.keys()):
        f.write(f"### [{structure[folder]['title']}](./{folder})\n")
        f.write(f"{structure[folder]['desc']}\n\n")

print("RL repository structured successfully!")
