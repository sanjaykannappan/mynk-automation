# Selenium Automation script

### Steps:-
    1. Create a Virtual enivronment
        python -m venv testingenv

    2. Source the virtual environment
        cd testingenv\Scripts\
        activate.bat
    
    3. Install the packages from requirement.txt
        pip install -r reuirements.txt

    4. Run the tests
        - make sure chrome driver is there in the environment
        - cd <path to base project dir>
        - run the command
            pytest  tests\