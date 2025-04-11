COMPRESS?= python3 ./compress/compress.py
RESIZE?= python3 ./resize/resize.py
CROP?= python3 ./crop/crop.py

INPUT_PNG?= ./input.png
OUTPUT_PNG?= ./output.png

_default: usage run show_input show_output

usage:
	$(COMPRESS) --help
	$(CROP) --help
	$(RESIZE) --help

run:
	cat $(INPUT_PNG) \
	| $(RESIZE) --width 1200 --keep-aspect-ratio \
	| $(CROP) --height 630 --crop-y-align middle \
	| $(COMPRESS) --color-depth 8 \
	> $(OUTPUT_PNG)


show_input:
	ls -al $(INPUT_PNG)
	file $(INPUT_PNG)
	open $(INPUT_PNG)

show_output:
	ls -al $(OUTPUT_PNG)
	file $(OUTPUT_PNG)
	open $(OUTPUT_PNG)
