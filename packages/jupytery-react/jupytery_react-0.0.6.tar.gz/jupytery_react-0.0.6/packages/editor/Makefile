# Copyright (c) Datalayer https://datalayer.io
# Distributed under the terms of the Apache License, Version 2.0
# https://www.apache.org/licenses/LICENSE-2.0.txt

SHELL=/bin/bash

.PHONY: typedoc typedoc-deploy

all: typedoc typedoc-deploy

typedoc: ## generated typedoc
	yarn typedoc

typedoc-deploy: ## deploy typedoc
	aws s3 cp \
		typedoc \
		s3://datalayer-typedoc/datalayer-jupyter/0.0.4/editor/ \
		--recursive \
		--profile datalayer
	echo open ✨  https://typedoc.datalayer.io/datalayer-jupyter/0.0.4/editor
