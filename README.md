# 🧙‍♂️ AI Dungeon Master — RAG-Powered RPG Adventure

## 📌 Overview
This project is an **AI-powered Dungeon Master (DM)** designed to run immersive **text-based Role-Playing Games (RPGs)**.  
Unlike traditional RPGs with fixed scripts, this system uses **Large Language Models (LLMs)** combined with **Retrieval-Augmented Generation (RAG)** to create **dynamic, adaptive adventures** where player choices shape the world.

The AI DM can:
- Generate unique quests, characters, and lore.
- Simulate battles, negotiations, puzzles, and exploration.
- Remember player decisions and adapt the story world accordingly.
- Use a **knowledge base (via ChromaDB)** to ground responses in consistent lore.

This allows for endless replayability while maintaining **coherent storytelling** and **game-like mechanics**.

---

## 🎮 Features
- 🎲 **Procedural Storytelling** — no two adventures are the same.  
- 📚 **RAG-powered Knowledge Base** — retrieves rules, lore, and backstories for consistency.  
- 🧠 **LLM-driven Dungeon Master** — generates dialogues, NPCs, and branching storylines.  
- ⚔️ **Interactive Mechanics** — AI can handle combat rolls, skill checks, and decision trees.  
- 🗺️ **Dynamic World State** — remembers player actions and changes the environment.  
- 💻 **Full-Stack Project** — includes backend (API + game engine), vector database, and frontend UI.  

---

## 🏗️ Architecture

flowchart TD
    A[Player Input] --> B[RAG Retriever (ChromaDB)]
    B --> C[Relevant Lore & Rules]
    A --> D[LLM Dungeon Master]
    C --> D
    D --> E[Game Engine (State + Memory)]
    E --> F[Frontend UI]
    F --> A
🔹 Workflow

Player Input: Natural language command (attack the dragon, negotiate with the guard, etc.).

Retriever (ChromaDB): Fetches relevant knowledge (world lore, NPC history, D&D-like rules).

LLM Dungeon Master: Generates creative, rule-consistent responses.

Game Engine: Updates world state, logs memory, tracks player stats.

Frontend: Displays narration, actions, and game progression.

📂 Repository Structure
-AI-Dungeon-Master---RAG-RPG-Adventure/
│── .github/workflows/        # GitHub Actions for CI/CD
│   └── python-app.yml
│── backend/                  # Core backend logic
│   ├── api/                  # REST/GraphQL endpoints
│   ├── game_engine.py        # Game state manager
│   ├── rag_pipeline.py       # RAG (Retriever + Generator)
│   └── dm_agent.py           # AI Dungeon Master logic
│── chroma_db/                # Vector database (lore, rules, NPC memory)
│── frontend/                 # UI layer (React/Streamlit)
│── app.py                    # Entry point for local run
│── requirements.txt          # Dependencies
│── .env                      # API keys & configs
│── README.md                 # Documentation

⚙️ Tech Stack

Backend: Python (FastAPI/Flask)

Frontend: React or Streamlit

LLMs: Hugging Face Transformers / OpenAI GPT API

Vector Database: ChromaDB

RAG Framework: Custom Retriever + Generator pipeline

Deployment: Docker + GitHub Actions CI/CD

🚀 Installation
1️⃣ Clone Repository
git clone https://github.com/meer25800/-AI-Dungeon-Master---RAG-RPG-Adventure.git
cd -AI-Dungeon-Master---RAG-RPG-Adventure

2️⃣ Setup Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure .env

Create a .env file with your API keys:

OPENAI_API_KEY=your_api_key_here
HF_API_KEY=your_huggingface_key_here
CHROMA_DB_PATH=./chroma_db

5️⃣ Run Application
python app.py


Frontend (React) → http://localhost:3000

Frontend (Streamlit) → http://localhost:8501

🕹️ Gameplay

Choose your character: name, class, backstory.

The AI DM sets the scene (e.g., "You awaken in a medieval tavern…").

You interact with the world using natural language:

>> Talk to the innkeeper
>> Attack the goblin with my sword
>> Sneak past the guards


The AI generates outcomes, updates game state, and retrieves lore.

Continue adventuring until victory… or defeat!

📊 Example Interaction

Player: "I want to sneak into the king’s chamber."
AI Dungeon Master:
"You press your back against the cold stone wall as the guards march past. The golden door of the king’s chamber glimmers faintly. Roll for stealth (Difficulty 14)… You succeed! Inside, the chamber glows with candlelight. A forbidden scroll lies on the desk."

📖 Future Enhancements

🎤 Voice Integration: Speak with the Dungeon Master (STT + TTS).

👥 Multiplayer Mode: Cooperative or competitive RPG adventures.

🗺️ Procedural Maps: Auto-generate dungeons, towns, and quests.

🎯 D&D 5e Rule Engine: Full dice-roll mechanics.

💾 Save/Load Campaigns: Persistent adventures across sessions.

🏆 Achievements

Built a RAG-powered AI Dungeon Master that can adapt dynamically.

Combines knowledge retrieval + generative storytelling.

Full-stack project (backend, frontend, database, CI/CD).
