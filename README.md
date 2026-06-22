# Pytest Automation Framework
 
Site Docs:
 
- Base URL: https://www.calculator.net/
- Endpoint: /repayment-calculator.html (Financial section)
 
### Table of Contents
 
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Running Tests](#running-tests)
4. [Contact](#contact)
 
---
 
### Prerequisites
 
Before you begin, ensure you have the following installed:
 
- [Python 3.10+](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
 
---
 
### Installation
 
**For this repository:**
 
1. Clone the repository:
   ```bash
   git clone https://github.com/Malith-Senadheera/playwright-pytest-framework.git
   cd <repository-directory>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
---
 
### Running Tests
 
```bash
# Run all tests
pytest
 
# Run only smoke (positive) tests
pytest -m smoke
 
# Run negative & edge-case tests
pytest -m edge
```
 
An HTML report is generated at `reports/`.
 
---

### Important

- **Note:** The repayment calculator currently shows **"postivie"** instead of **"positive"**. The test matches the current UI text so it passes. - minor bug.

### Contact
 
For questions or support, open an issue or reach out via the repository’s contact channels.
malith.akalanka@outlook.com
 
---