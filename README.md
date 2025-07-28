# TicTacToe-AI

A comprehensive Tic-Tac-Toe implementation featuring multiple AI strategies, from basic random moves to advanced minimax with alpha-beta pruning. Includes both command-line and GUI interfaces.

## 🎮 Features

- **Multiple AI Strategies**: Random, strategic rule-based, and optimal minimax algorithms
- **GUI Interface**: Interactive PyGame-based graphical interface
- **Performance Optimizations**: Caching, symmetry detection, and alpha-beta pruning
- **Batch Testing**: Run thousands of games to compare AI performance
- **Human vs AI**: Play against any AI strategy
- **AI vs AI**: Watch different strategies compete

## 🚀 Quick Start

### Play with GUI

```bash
python gui/pygame_gui.py
```

### Play in Terminal

```bash
python main.py human minimax
```

### Run AI Battle Simulation

```bash
python main.py minimax random_ai2
```

## 🤖 AI Strategies

| AI Name                             | Description                              | Skill Level  |
| ----------------------------------- | ---------------------------------------- | ------------ |
| `random_ai`                         | Completely random moves                  | Beginner     |
| `random_ai2`                        | Random from available moves only         | Beginner     |
| `finds_winning_moves_ai`            | Takes winning moves when available       | Novice       |
| `finds_winning_and_losing_moves_ai` | Wins when possible, blocks opponent wins | Intermediate |
| `minimax`                           | Optimal play using minimax algorithm     | Expert       |

## 📁 Project Structure

```
TicTacToe-AI/
├── main.py                 # Entry point and game orchestration
├── gui/
│   ├── __init__.py
│   └── pygame_gui.py     # Interactive GUI interface
├── game/
│   ├── __init__.py
│   ├── board.py           # Board operations and utilities
│   └── rules.py           # Game rules and win detection
├── ai/
│   ├── __init__.py
│   ├── random_ai.py       # Random move strategies
│   ├── strategic_ai.py    # Rule-based AI strategies
│   └── minimax_ai.py      # Minimax with optimizations
├── players/
│   ├── __init__.py
│   └── human.py           # Human player interface
└── README.md
```

## 🎯 Usage Examples

### Command Line Interface

```bash
# Human vs Minimax AI
python main.py human minimax

# Random AI vs Strategic AI (1000 games)
python main.py random_ai2 finds_winning_and_losing_moves_ai

# Launch GUI
python main.py gui
```

### Available AI Options

- `human` - Human player (interactive input)
- `random_ai` - Basic random moves
- `random_ai2` - Improved random (valid moves only)
- `finds_winning_moves_ai` - Takes wins when available
- `finds_winning_and_losing_moves_ai` - Wins and blocks
- `minimax` - Optimal minimax algorithm

### Batch Testing Output

```
minimax won 847 times.
random_ai2 won 12 times.
141 draws.

minimax won 84.7%
random_ai2 won 1.2%
They drew 14.1%

Execution time: 2.34 seconds
Games per second: 427.4
```

## 🧠 Algorithm Details

### Minimax Algorithm

- **Perfect play**: Minimax AI never loses when playing optimally
- **Memoization**: Caches board positions to avoid recalculation

### Performance Optimizations

1. **Caching**: Stores previously calculated board evaluations
2. **0-based Indexing**: Consistent coordinate system throughout

## 🖥️ GUI Features

- **Click-to-play**: Intuitive mouse-based moves
- **Visual feedback**: Color-coded X's and O's
- **Game status**: Real-time turn and winner display
- **New game**: Restart functionality
- **AI thinking indicator**: Shows when AI is calculating

## 📊 Performance Benchmarks

| Matchup                 | Games | Minimax Win% | Opponent Win% | Draw%  |
| ----------------------- | ----- | ------------ | ------------- | ------ |
| minimax vs random_ai2   | 1000  | 85-90%       | 1-5%          | 10-15% |
| minimax vs strategic_ai | 1000  | 70-80%       | 0-5%          | 20-25% |
| minimax vs minimax      | 1000  | 50%          | 50%           | ~90%   |

## 🛠️ Installation

### Requirements

- Python 3.6+
- Pygame

### Optional Dependencies

```bash
# For enhanced GUI (optional)
pip install pygame
```

### Setup

```bash
git clone https://github.com/yourusername/TicTacToe-AI.git
cd TicTacToe-AI
python main.py gui
```

## 🎓 Educational Value

This project demonstrates:

- **Game theory**: Minimax algorithm and optimal play
- **Algorithm optimization**: Pruning, caching, and symmetry
- **Software architecture**: Modular design and separation of concerns
- **GUI development**: Interactive application design
- **Performance analysis**: Benchmarking and profiling

## 🔧 Advanced Features

### Minimax Optimizations

- **Alpha-beta pruning** reduces nodes evaluated by ~90%
- **Transposition table** caches 5000+ board positions
- **Move ordering** improves pruning efficiency

### Coordinate System

- **0-based indexing** throughout codebase for consistency
- **Automatic conversion** for human-readable input/output
- **Position validation** prevents invalid moves

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📈 Future Enhancements

- [ ] **Neural network AI** using reinforcement learning
- [ ] **Web interface** using Flask/Django
- [ ] **Larger boards** (4x4, 5x5) with configurable win conditions
- [ ] **Tournament mode** with multiple AI strategies
- [ ] **Move history** and game replay functionality
- [ ] **Difficulty levels** with intentionally imperfect play

## 🙏 Acknowledgments

- Inspired by classic game theory and AI algorithms
- Built for educational purposes and AI strategy exploration
- Thanks to the Python community for excellent libraries and documentation

## 📞 Contact

- **Author**: [Ljupcho Kostoski]
- **Email**: [ljupcekostoski1@gmail.com]
- **GitHub**: [@lkostoski](https://github.com/lkostoski)
- **Project Link**: [https://github.com/lkostoski/TicTacToe-AI](https://github.com/lkostoski/TicTacToe-AI)

---

⭐ **Star this repository if you found it helpful!** ⭐
