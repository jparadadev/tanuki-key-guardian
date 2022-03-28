# Build project
.PHONY = build
build:
	python3 -m venv env
	pip install -r requirements.txt

# Install dependencies
.PHONY = deps
deps:
	pip install -r requirements.txt

# Run tests
.PHONY = test
test:
	python -m unittest discover -s ./tests -p '*Test.py'

# Run backoffice app
.PHONY = run/kms
run/kms:
	python main.py --service kms