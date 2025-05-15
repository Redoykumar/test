# Selenium Tests Project

## Project Structure

- `main.py` - Entry point to run test managers.
- `test_managers/` - Orchestrates tests per module.
- `tests/` - Contains module-wise test cases.
- `pages/` - Page Object Model classes.
- `utils/` - Helper functions, config, and driver management.
- `data/` - Test data files.
- `reports/` - Test reports and logs.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run tests:
   ```
   python main.py crm
   python main.py user_management
   ```

## Environment Variables

- BASE_URL: URL of the application under test
- TIMEOUT: Timeout for waits (default 10)
- BROWSER: Browser to use (default chrome)

## Adding New Tests

- Add Page Object classes in `pages/`.
- Add test cases in `tests/`.
- Add or update test data in `data/`.
- Extend `test_managers/` to handle new test workflows.

---

Happy Testing!
# test
