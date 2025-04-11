COMPRESS?= python3 compress.py

INPUT_PNG?= input.png
OUTPUT_PNG?= output.png

_default: usage example_1 show_input show_output

usage:
	$(COMPRESS) --help

example_1:
	$(COMPRESS) --in $(INPUT_PNG) --out $(OUTPUT_PNG) --color-depth 8

example_2:
	cat input.png | $(COMPRESS) --in - --out - --color-depth 2 > $(OUTPUT_PNG)

show_input:
	ls -al $(INPUT_PNG)
	file $(INPUT_PNG)
	open $(INPUT_PNG)

show_output:
	ls -al $(OUTPUT_PNG)
	file $(OUTPUT_PNG)
	open $(OUTPUT_PNG)
