import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

ui.page_opts(title="Tesheena's Shiny Interative App", fillable=True)

with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 150, 25)


@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), color="green", density=True)
    plt.title("A Random Histogram Example")
