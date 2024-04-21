all: rebuild

# Setup the virtual environment
setup:
	python3 -m venv venv
	source venv/bin/activate

# Install the dependencies from `requirements.txt`
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Build the protobuf files
build:
	@echo "Building..."
	bash scripts/build.sh
	@echo "Building complete."

# Remove the generated files
clean:
	@echo "Cleaning..."
	bash scripts/clean.sh
	@echo "Cleaning complete."

rebuild:
	@$(MAKE) clean
	@$(MAKE) build