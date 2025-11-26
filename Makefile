GREEN  := \033[32m
RESET  := \033[0m

# Python from virtual environment
PYTHON = ./eval/bin/python3
PIP = ./eval/bin/pip

.PHONY: setup install train predict bonus clean

setup:
	@ python3 -m venv eval
	@ echo "$(GREEN)Virtual environment created$(RESET)"

install: setup
	@ $(PIP) install -r eval.txt
	@ echo "$(GREEN)Necessary packages installed$(RESET)"

train:
	@ $(PYTHON) ./src/train.py

predict:
	@ $(PYTHON) ./src/predict.py

bonus:
	@ $(PYTHON) ./src/bonus.py

clean:
	@ rm -f ./data/result*.json
	@ rm -f plot*.gif
	@ rm -rf src/__pycache__
	@ echo "$(GREEN)Done cleaning...$(RESET)"

