# Contributing to 🗺️ Py_Leeds_Poster

Thank you for your interest in improving this project!

## 🛠️ Local Development Setup

This project uses `uv` for environment management. To get started:

1. Fork and clone the repository.
2. Initialize the isolated environment and install dependencies:
   ```powershell
   uv sync
Test the baseline rendering pipeline to ensure your environment is valid:

```PowerShell
uv run generate_leeds.py
```
## 🔀 Contribution Workflow
- Create a Branch: Please branch off of main with a descriptive name (e.g., feature/parallel-processing or fix/windows-path).

- Write Clean Code: Follow standard PEP 8 formatting guidelines. Ensure all subprocess logic handles native Windows executable calls cleanly.

- Keep it Lean: Do not commit any generated .png or .json assets from the posters/ folder. Ensure your local .gitignore is active.

- Submit a Pull Request: Open a PR against the main branch with a clear description of your changes, the bug fixed, or the feature added.

## 💡 Areas for Contribution
- Upgrading the pipeline loop to support parallel multi-processing.

- Implementing a dynamic JSON layout configuration structure for
multiple global cities.