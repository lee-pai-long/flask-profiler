# Flask Profiler Makefile
# -----------------------

# Switch to bash instead of sh
SHELL := /bin/bash

# Project constants
# -----------------
PROJECT_NAME    = flask-profiler

# Helpers
# -------
# Colors.
W	= \033[0m
R	= \033[31m
G	= \033[32m
Y	= \033[33m
B	= \033[34m
P	= \033[35m
C	= \033[36m


# Tasks
# -----

help: ## Show this message.

	@echo "usage: make [task]" \
	&& echo "available tasks:" \
	&& awk \
		'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / \
		{printf "$(C)%-8s$(W) : %s\n", $$1, $$2}' $(MAKEFILE_LIST)

todo: ## Print all code tags.

	@find . \
		-type f \
		! -name 'Makefile' \
		-not -path "./.git/*" \
		-exec \
			awk '/TODO:/ \
				|| /FIXME:/ \
				|| /CHANGE:/ \
				|| /XXX:/ \
				|| /REVIEW:/ \
				|| /BUG:/ \
				|| /REFACTOR:/ \
				{ \
					gsub("# ","", $$0); \
					gsub("// ","", $$0); \
					gsub(/^[ \t]+/, "", $$0); \
					gsub(/:/, "", $$0); \
					gsub(/\.\//,"", FILENAME); \
					TYPE = $$1; $$1 = ""; \
					MESSAGE = $$0; \
					LINE = NR; \
					printf "$(C)%s|$(W):%s|: $(C)%s$(W)($(B)%s$(W))\n"\
					, TYPE, MESSAGE, FILENAME, LINE \
				}' \
		{} \; | column -s '|' -t

# Declare tasks as phony targets.
.PHONY: help todo

# '||:' is a shortcut to '|| true' to avoid the
# 'make: [target] Error 1 (ignored)' warning message
