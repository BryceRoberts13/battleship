### **Battleship AI Project Plan**  

---

#### **Table of Contents**  
1. **Project Vision**  
2. **Technical Breakdown**  
   - Core Components  
   - Decomposition Approaches  
   - Hierarchical Tree Structure  
3. **Implementation Plan**  
   - Task Table  
4. **Learning Resources**  

---

### **1. Project Vision**  
**Goal**: Build a Battleship solver with probabilistic AI using [Datagenetics' method](http://www.datagenetics.com/blog/december32011/).  
**Key Features**:  
- Flexible gameplay (Human vs Human, Human vs AI, AI vs AI)  
- Command-line interface with optional visualization  
- Modular AI system (probabilistic, random)  
- Simulation mode for AI benchmarking  
**Tech Stack**: Python, / for UI, UV/Ruff/Git for tooling.  

---

### **2. Technical Breakdown**  

#### **Core Components**  
| **Component**         | **Purpose**                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Game Core**         | Board logic, ship placement, move validation, win detection                 |
| **Player System**     | Human input handler, AI strategies (random, probabilistic)                  |
| **Game Orchestrator** | Manages turns, game modes (PvP, PvAI, AIvAI)                               |
| **Visualizer**        | Optional terminal UI for real-time board display                            |
| **Simulation Engine** | Runs batch AI vs AI games; collects win rates, move efficiency stats        |

#### **Decomposition Approaches**  
**Approach 1: By Functionality**  
| **Module**          | **Components**                                                                 |
|---------------------|-------------------------------------------------------------------------------|
| Game Logic          | , , ,                                  |
| AI System           | , ,  (heatmap logic)                       |
| User Interaction    |  (input handling),  (/)          |
| Simulation & Stats  | ,                                           |

**Approach 2: By Workflow**  
| **Module**          | **Components**                                                                 |
|---------------------|-------------------------------------------------------------------------------|
| Setup & Init        | ,                                                   |
| Game Execution      | ,  (human/AI selection)                           |
| AI Core             | ,                                           |
| Output & Analysis   | ,                                                 |

#### **Hierarchical Tree Structure**  


---

### **3. Implementation Plan**  
**Task Table** (Ordered by Dependencies)  

| **Task/Subtask**               | **Description**                                                                 | **Dependencies**                  | **Effort** | **Success Criteria**                                   |
|--------------------------------|---------------------------------------------------------------------------------|-----------------------------------|------------|--------------------------------------------------------|
| **1. Project Setup**           | Initialize Git, setup dirs, install tools (UV, Ruff)                           | None                              | Low        | Repo created; tools installed                          |
| **2. Board & Ship Logic**      | Implement 10x10 board; place ships (Carrier, Battleship, etc.) without overlap | Task 1                            | Medium     | Ships placed correctly; collision detection works      |
| **3. Game State Mgmt**         | Track hits/misses; detect sunk ships; win condition                            | Task 2                            | Medium     | Win detected when all ships sunk                       |
| **4. Move Validator**          | Validate coordinates (A1-J10); prevent duplicate moves                         | Task 2                            | Low        | Invalid moves rejected                                 |
| **5. CLI Input Handler**       | Parse human moves (e.g., A5) for PvP mode                                    | Task 4                            | Medium     | Moves parsed → valid board coordinates                 |
| **6. Random AI**               | AI that selects random valid moves                                             | Tasks 2, 4                        | Low        | AI plays full game without errors                      |
| **7. Game Orchestrator**       | Turn manager for PvP/PvAI/AIvAI modes                                          | Tasks 3, 5, 6                     | High       | Supports all gameplay modes                            |
| **8. Heatmap AI Core**         | Implement probability matrix (Datagenetics method)                             | Tasks 2, 4                        | High       | AI prioritizes high-probability cells                  |
| **9. Heatmap AI Integration**  | Connect AI to orchestrator; update heatmap after moves                         | Tasks 7, 8                        | Medium     | AI beats random AI >70% of games                       |
| **10. Basic Visualizer**       | Print ASCII board to terminal after each move                                  | Tasks 2, 3                        | Low        | Board displayed with hits/misses                       |
| **11. Enhanced Visualizer**    | Upgrade to  (colors, grids) or  (interactive)                    | Task 10                           | Medium     | Visually polished board                                |
| **12. Simulation Runner**      | Run N AI vs AI games; log results                                              | Tasks 6, 8, 9                     | Medium     | Runs 1k games; outputs CSV of results                  |
| **13. Stats Analyzer**         | Calculate win rates, avg moves per game                                        | Task 12                           | Low        | Stats report generated (e.g., Prob AI win rate: 85%) |
| **14. Main Entry Point**       | CLI to choose mode (e.g., )                    | All tasks                         | Medium     | User can start any mode via flags                      |

> **Effort Scale**: Low (1-2 hrs), Medium (3-5 hrs), High (6+ hrs)  

---

### **4. Learning Resources**  
#### **Heatmap Algorithms**  
- [**Datagenetics Deep Dive**](http://www.datagenetics.com/blog/december32011/)  
- [**Efficient Heatmap Updates**](https://stackoverflow.com/questions/45526700) (StackOverflow)  
- [**Battleship Probability Theory**](https://arxiv.org/pdf/1401.5750.pdf) (arXiv Paper)  

#### **Terminal UI with **  
- [**Official Rich Docs**](https://rich.readthedocs.io/en/stable/)  
- [**CLI Game Tutorial**](https://www.twilio.com/blog/battleship-python-terminal-game-using-rich)  

#### **Terminal UI with **  
- [**Python curses Tutorial**](https://docs.python.org/3/howto/curses.html)  
- [**Curses BattleShip Example**](https://gist.github.com/taylorconor/1103713)  

#### **Project Structure**  
- [**Modular Python Design**](https://realpython.com/python-application-layouts/)  
- [**OOP Best Practices**](https://realpython.com/python3-object-oriented-programming/)  

---

**Next Steps**:  
1. Start with **Task 1-4** (Core logic)  
2. Build **Random AI + Orchestrator** (Tasks 5-7)  
3. Implement **Probabilistic AI** (Tasks 8-9)  
4. Add **UI/Simulation** layers (Tasks 10-14)
