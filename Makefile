.PHONY: setup test

setup:
	bash scripts/setup.sh

test:
	uv run pytest
