test:
	pytest --tb=short

watch-tests:
	ls tests/*.py | entr pytest --tb=short
