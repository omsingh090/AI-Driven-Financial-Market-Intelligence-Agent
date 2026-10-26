# Contributing to AI-Driven Financial Market Intelligence Agent

Thank you for your interest in contributing to the AI-Driven Financial Market Intelligence Agent! We welcome contributions from the community.

## Code of Conduct

Please maintain a respectful, constructive, and inclusive environment for everyone.

## Development Workflow

1. **Fork and Clone**:
   ```bash
   git clone https://github.com/<your-username>/AI-Driven-Financial-Market-Intelligence-Agent.git
   cd AI-Driven-Financial-Market-Intelligence-Agent
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux / macOS:
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-asyncio flake8
   ```

4. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

5. **Run Tests**:
   ```bash
   pytest -v
   ```

6. **Coding Standards**:
   - Follow PEP 8 guidelines.
   - Ensure clean function docstrings and type annotations.
   - Write unit tests for new modules and bug fixes.
   - Verify all tests pass before submitting a pull request.

7. **Submit a Pull Request**:
   - Provide a concise description of your changes.
   - Reference any relevant issues.
