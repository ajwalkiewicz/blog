.PHONY: setup check-uv clean clean_venv clean_cache format check_format \
	check_type prepare publish \

setup: check-uv uv.lock
	@echo "Setting up project..."
	uv sync
	
check-uv:
	@if ! command -v uv > /dev/null; then \
		echo "UV is not installed"; \
		echo "Installing UV"; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	fi

clean: clean_venv clean_cache

clean_venv:
	@echo "Removing virtual environment.."
	rm -rf .venv

clean_cache:
	@echo "Removing all cache files and directories int the project..." 
	find . -name "*cache*" -type d | xargs -t -I {} rm -rf "{}"

format:
	@echo "Formatting project files with ruff..."
	uv run ruff format

check_format:
	@echo "Checking project files with ruff..."
	uv run ruff check

check_type:
	@echo "checking typing with mypy..."
	uv run mypy .

prepare:
	@echo "coping files to the hugo page"
	uv run ./scripts/move.py

publish: scripts/publish.sh
	@echo "publishing changes..."
	./scripts/publish.sh