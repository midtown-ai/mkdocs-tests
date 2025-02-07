import graphviz
print(graphviz.__version__)
graphviz.Source("digraph G { A -> B }").render("test_output", format="png", view=True)

