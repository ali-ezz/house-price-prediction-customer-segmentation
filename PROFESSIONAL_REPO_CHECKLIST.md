# Professional Repo Checklist

Use this checklist to make any repository look professional, clear, and easy for a reviewer to understand in 2–5 minutes.

## 1. Strong README
- Project title
- One-line summary
- Problem solved
- Features
- Tech stack
- Installation
- Usage
- Project structure
- Environment variables
- Results / metrics
- Future improvements
- License

## 2. Clean repo structure
- `README.md`
- `LICENSE`
- `requirements.txt` / `pyproject.toml`
- `.gitignore`
- `tests/`
- `docs/` or `HOW_TO_RUN.md`
- `data/` for small/sample data only
- `notebooks/` for DS/ML workflows
- avoid checking in huge model files when possible
- `assets/` for images, screenshots, diagrams

## 3. Proper project files
- `README.md`
- `.gitignore`
- `LICENSE`
- `requirements.txt` or `environment.yml`
- `.env.example`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `CHANGELOG.md`

## 4. License
- Include an open source license for clear reuse permission
- Recommended: MIT, Apache 2.0, GPL
- MIT is a good default for general projects

## 5. Good commits
- Avoid vague messages: `update`, `fix`, `new`
- Use meaningful commit messages:
  - `feat: add user authentication`
  - `fix: handle missing dataset values`
  - `docs: improve installation guide`
  - `refactor: clean preprocessing pipeline`

## 6. Clear setup instructions
- Show how to clone, install, and run the project
- Example:
  - `git clone ...`
  - `cd project`
  - `pip install -r requirements.txt`
  - `python app.py`

## 7. Tests
- Add at least one basic test to improve trust
- Example files:
  - `tests/test_preprocessing.py`
  - `tests/test_api.py`
  - `tests/test_model.py`

## 8. Badges
- Keep badges minimal
- Useful badges include:
  - License
  - Python version
  - Last commit

## 9. GitHub templates
- Add `.github/ISSUE_TEMPLATE/bug_report.md`
- Add `.github/ISSUE_TEMPLATE/feature_request.md`
- Add `.github/pull_request_template.md`

## Minimal required files for a professional repo
- `README.md`
- `LICENSE`
- `.gitignore`
- `requirements.txt`
- `.env.example`
- `tests/`
