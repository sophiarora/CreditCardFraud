import numpy as np
import pandas as pd


credit_card = pd.read_csv('/Users/MiroWang/Desktop/Github Repo/CreditFraudData/creditcard.csv', encoding = 'utf-8')
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row, widgetbox
from bokeh.models import Select, CategoricalColorMapper
from bokeh.application.handlers import FunctionHandler
from bokeh.palettes import Spectral5
from bokeh.plotting import curdoc, figure
from bokeh.application import Application
#from bokeh.palettes import RdYlGn

#output_notebook()

df = credit_card.copy()

#COLORS = Spectral5
#define color
df['color'] = np.where(df['Class'] == 0, 'grey', 'orange')
# data cleanup
del df['Time']
del df['Class']

columns = sorted(df.columns)


def create_figure():
    xs = df[x.value].values
    ys = df[y.value].values
    plot_color = df['color'].values
    x_title = x.value.title()
    y_title = y.value.title()

    kw = dict()
    kw['title'] = "%s vs %s" % (x_title, y_title)

    p = figure(plot_height=600, plot_width=800, tools='pan,box_zoom,reset', **kw)
    p.xaxis.axis_label = x_title
    p.yaxis.axis_label = y_title

    #color_mapper = CategoricalColorMapper(factors=["normal", "fraud"], palette=["pink", "yellow"])

    p.circle(x=xs, y=ys, color = plot_color, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5)

    return p


def update(attr, old, new):
    layout.children[1] = create_figure()
    #push updates to notebook
    push_notebook()

    #define xs
x = Select(title='X-Axis', value='V1', options=columns)
x.on_change('value', update)

y = Select(title='Y-Axis', value='V2', options=columns)
y.on_change('value', update)

controls = widgetbox([x, y], width=200)
layout = row(controls, create_figure())
curdoc().add_root(layout)
curdoc().title = "creditcard"
