from bokeh.sampledata.iris import flowers
from bokeh.plotting import figure


def make_plot():
    colormap = {"setosa": "red", "versicolor": "green", "virginica": "blue"}
    colors = [colormap[x] for x in flowers["species"]]

    p = figure(title="Iris Morphology")
    p.xaxis.axis_label = "Petal Length"
    p.yaxis.axis_label = "Petal Width"

    p.circle(
        flowers["petal_length"],
        flowers["petal_width"],
        color=colors,
        fill_alpha=0.2,
        size=10,
    )

    return p
