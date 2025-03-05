Dungeon Mentat (WIP)
===
An intelligent assistant for tabletop roleplaying games

How would you make a custom tool for managing RPG resources?
---
The tool I would make would be a combination of Obsidian+Elasticsearch+ChatGPT

1. Ground state. Have the data
    - Session notes
    - Maps
    - Rulebooks
2. Make sure all that data is machine readable/interpretable.
    - Extract text and metadata from text files, PDFs, folder structure
3. Make all the data searchable.
    - Index for full text and vector searching
4. Get a data assistant
    - Use RAG with a language model to search and discuss your game materials
5. Basic Prep assistance
    - Automatically create and export worldbuilding details (e.g. NPCs)
6. Advanced Prep assistance
    - Other models/tools to generate other artifacts (maps, artifacts, portraits, illustrations)
  
Stack
---

- Python
- Poetry
- LanceDB
- Kuzu?
- Some kind of local LLM
- OpenAI library
