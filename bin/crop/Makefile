CROP?= python3 ./crop.py

INPUT_PNG?= ./input.png
OUTPUT_PNG?= ./output.png

_default: usage

usage:
	$(CROP) --help

example_1:
	$(CROP) --in $(INPUT_PNG) --out $(OUTPUT_PNG) --x 100 --y 100 --width 100 

example_2:
	$(CROP) --in $(INPUT_PNG) --out $(OUTPUT_PNG) --width 100 --height 100 --crop-x-align middle --crop-y-align middle

show_input:
	ls -al $(INPUT_PNG)
	file $(INPUT_PNG)
	open $(INPUT_PNG)

show_output:
	ls -al $(OUTPUT_PNG)
	file $(OUTPUT_PNG)
	open $(OUTPUT_PNG)
