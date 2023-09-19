import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

COLOR_MAP = pd.Series({
    "C": 'rgb(153, 153, 153)',
    "W": 'rgb(251, 188, 4)',
    "U": 'rgb(66, 133, 244)',
    "B": 'rgb(103, 78, 167)',
    "R": 'rgb(234, 67, 53)',
    "G": 'rgb(52, 168, 83)'
}, name='Graph Color')


def create_donut_plot(values, central_column, colors=[], center_top_slice=False):
    outer_columns = values.columns.drop(central_column)
    total = values.sum(axis=1)[0]
    outer_total = total - values[central_column][0]
    hole_radius = np.sqrt(values[central_column][0] / total)
    
    top_slice_angle = 0
    if center_top_slice:
        top_slice_angle = -360 * values[outer_columns[0]][0] / outer_total / 2
    
    central_color = None
    outer_colors = None
    if len(colors) != 0:
        central_color = colors[colors.index == central_column]
        outer_colors = colors[colors.index != central_column]

    fig = go.Figure()

    fig.add_trace(go.Pie(labels=[central_column],
                     values=values[central_column],
                     marker_colors=central_color))
        
    fig.add_trace(go.Pie(labels=outer_columns,
                     values=values[outer_columns].iloc[0, :],
                     scalegroup=1, hole=hole_radius, rotation=top_slice_angle,
                     direction='clockwise', sort=False,
                     marker_colors=outer_colors,
                     marker_line=dict(color='#000000', width=1)))
    
    fig.update_traces(textposition='inside', textinfo='value')
    
    fig.show()


if __name__ == '__main__':
    values = pd.DataFrame([[5, 4, 1, 2, 1, 3]], columns=["C", "W", "U", "B", "R", "G"])
    create_donut_plot(values, central_column='C', colors=COLOR_MAP, center_top_slice=True)
