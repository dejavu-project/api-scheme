all: rebuild

rebuild:
	@$(MAKE) clean
	@$(MAKE) build

build:
	@echo "Building..."
	bash scripts/build.sh
	@echo "Building complete."

clean:
	@echo "Cleaning..."
	bash scripts/clean.sh
	@echo "Cleaning complete."