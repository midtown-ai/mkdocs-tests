RESIZE?= python3 resize.py

_default: usage example_2 show_input show_output

usage:
	$(RESIZE) --help

example_1:
	$(RESIZE) --in input.png --out output.png

example_2:
	$(RESIZE) --in input.png --out output.png --width 400 --keep-aspect-ratio

example_3:
	$(RESIZE) --in input.png --out output.png --height 210 --keep-aspect-ratio

example_4:
	$(RESIZE) --in input.png --out output.png --width 500 --height 100

example_5:
	cat input.png | $(RESIZE) --in - --out - --width 300 --height 500 > output.png

show_input:
	ls -al input.png
	file input.png
	open input.png

show_output:
	ls -al output.png
	file output.png
	open output.png
