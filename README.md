# 🐍 AI Search Maze Visualizer

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Comparative analysis of pathfinding algorithms (BFS, DFS, A*) with real-time maze visualization. Each algorithm controls a snake navigating through randomly generated mazes to reach target destinations.

## 🎯 Features

- **Three Search Algorithms**: BFS (Breadth-First), DFS (Depth-First), A* (Heuristic)
- **Visual Comparison**: Side-by-side runtime and path length analysis
- **Interactive Maze Generation**: Random maze creation with configurable complexity
- **Performance Metrics**: Time complexity and path optimality measurements
- **Snake-based Visualization**: Algorithms embodied as moving agents

## 📊 Algorithm Comparison

| Algorithm | Completeness | Optimality | Time Complexity |
|-----------|-------------|------------|------------------|
| **BFS**   | ✅ Yes      | ✅ Yes     | O(V + E)         |
| **DFS**   | ✅ Yes      | ❌ No      | O(V + E)         |
| **A***    | ✅ Yes      | ✅ Yes     | O(b^d)           |

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/masoud-rafiee/ai-search-maze-visualizer.git
cd ai-search-maze-visualizer

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
python Masoud-Rafiee-HW1.py
```

The program will:
1. Generate a random maze
2. Run all three algorithms simultaneously
3. Display visual paths with performance statistics
4. Output runtime comparisons

## 🛠️ Technical Details

### Dependencies
- `pyamaze`: Maze generation and visualization framework
- Python 3.8+

### Project Structure
```
ai-search-maze-visualizer/
├── Masoud-Rafiee-HW1.py  # Main implementation
├── pyamaze.py             # Maze framework library
├── requirements.txt       # Python dependencies
└── README.md
```

### Key Implementation

- **BFS**: Explores all neighbors level-by-level, guarantees shortest path
- **DFS**: Explores deep before backtracking, fast but not optimal
- **A***: Uses Manhattan distance heuristic for informed search

## 📈 Performance Analysis

Typical results on a 20x20 maze:
- **A***: ~0.02s (shortest path)
- **BFS**: ~0.05s (shortest path, slower than A*)
- **DFS**: ~0.01s (faster but longer path)

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional algorithms (Dijkstra, Greedy Best-First)
- Configurable maze sizes via CLI arguments
- Export performance data to CSV
- Support for weighted graphs

## 📄 License

MIT License - see LICENSE file

## 👤 Author

**Masoud Rafiee**  
GitHub: [@masoud-rafiee](https://github.com/masoud-rafiee)

---

*Developed for AI course - Artificial Intelligence Search Algorithms*
