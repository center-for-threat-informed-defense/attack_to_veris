SOURCEDIR = docs/
BUILDDIR = docs/_build/

.PHONY: docs

docs:
	sphinx-build -M html "$(SOURCEDIR)" "$(BUILDDIR)"

docs-server:
	sphinx-autobuild -b dirhtml -a "$(SOURCEDIR)" "$(BUILDDIR)"

docs-pdf:
	poetry export --dev --without-hashes -f requirements.txt -o docs/requirements.txt
	docker run --rm -v "$(PWD)/docs":/docs sphinxdoc/sphinx-latexpdf:4.3.1 \
		bash -c "pip install -r requirements.txt && sphinx-build -M latexpdf /docs /docs/_build"
	rm docs/requirements.txt

test:
	pytest --cov=src/ --cov-report=term-missing

test-ci:
	pytest --cov=src/ --cov-report=xml
