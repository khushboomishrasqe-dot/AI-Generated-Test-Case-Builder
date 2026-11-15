# AI-Generated Test Case Builder + Selenium Execution

## Project overview
This project demonstrates AI-assisted test design for the login functionality of [SauceDemo](https://www.saucedemo.com/) and automates one positive login scenario using Selenium and Pytest.

**Tools:** Python 3.10+, Selenium 4, Pytest  
**Design:** Page Object Model (POM)

## Requirement under test
As a user, I should be able to log in to SauceDemo with valid credentials. Invalid or incomplete credentials should not grant access and should produce an appropriate validation message.

## AI-generated test cases

The following scenarios were drafted with AI assistance from the requirement above and then reviewed for relevance and expected results.

| ID | Scenario | Test data | Expected result | Type |
|---|---|---|---|---|
| TC_LOGIN_001 | Login with valid credentials | `standard_user` / `secret_sauce` | User is redirected to the inventory page and products are visible. | Positive |
| TC_LOGIN_002 | Login with an incorrect password | `standard_user` / `wrong_password` | Login is rejected and an error message is displayed. | Negative |
| TC_LOGIN_003 | Submit with both fields empty | Username blank, password blank | Login is rejected and a required-field validation message is displayed. | Negative / boundary |
| TC_LOGIN_004 | Submit with username empty | Username blank, password `secret_sauce` | Login is rejected and a username-required message is displayed. | Negative |
| TC_LOGIN_005 | Login with a locked-out account | `locked_out_user` / `secret_sauce` | Login is rejected and a locked-out account message is displayed. | Negative / account state |

> Note: These are designed test scenarios. The automated script in this repository executes TC_LOGIN_001. The remaining cases are documented test designs, not claimed as automated executions.

## How AI helped test design
AI was used to expand the basic login requirement into different risk-based scenarios rather than testing only the happy path. It helped identify:
- A positive authentication flow.
- Incorrect credentials.
- Empty-field validation and a single-field boundary condition.
- A known locked-out account state.

The scenarios were reviewed against the public application's behavior and kept specific, independently executable, and associated with clear expected results. AI supported test design; the automation code was structured and reviewed separately.

## Automated test
`tests/test_login.py` automates **TC_LOGIN_001**:
1. Opens SauceDemo.
2. Enters valid standard-user credentials.
3. Clicks Login.
4. Verifies the inventory page URL and product container.

The page interactions and locators are maintained in `pages/login_page.py` using a simple Page Object Model.

## Project structure
```text
ai_login_test_builder/
├── pages/
│   └── login_page.py
├── tests/
│   └── test_login.py
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Setup and execution

### 1. Install Python
Use Python 3.10 or later. Confirm installation:
```bash
python --version
```

### 2. Create and activate a virtual environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the test
```bash
pytest -v
```

Selenium 4.6+ includes Selenium Manager, which can obtain a compatible browser driver automatically in many standard setups. Google Chrome must be installed.

### Optional: run Chrome headlessly
PowerShell:
```powershell
$env:HEADLESS="true"
pytest -v
```

macOS/Linux:
```bash
HEADLESS=true pytest -v
```

## Expected result
The test should pass when SauceDemo is reachable and its login page behaves as expected. Pytest reports the result in the terminal.

## Scope and limitations
- This is a small demonstration project, not a full production test framework.
- It automates one test case; four additional scenarios are documented for test-design evaluation.
- The test depends on the public demo website and an installed Chrome browser.
- No credentials for a real user account are used; only SauceDemo's publicly documented demo account is used.
