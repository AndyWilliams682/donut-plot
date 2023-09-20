import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


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
                     marker_colors=central_color,
                     marker_line=dict(color='#000000', width=1))
        
    fig.add_trace(go.Pie(labels=outer_columns,
                     values=values[outer_columns].iloc[0, :],
                     scalegroup=1, hole=hole_radius, rotation=top_slice_angle,
                     direction='clockwise', sort=False,
                     marker_colors=outer_colors,
                     marker_line=dict(color='#000000', width=1)))
    
    fig.update_traces(textposition='inside', textinfo='value')
    
    fig.show()


if __name__ == '__main__':
    values = pd.DataFrame([[70, 3, 7, 20]], columns=['Success', 'Error 1', 'Error 2', 'Error 3'])
    color_map = pd.Series({
        'Success': 'rgb(100, 110, 250)',
        'Error 1': 'rgb(179, 23, 44)',
        'Error 2': 'rgb(245, 166, 130)',
        'Error 3': 'rgb(102, 0, 31)'
    }, name='Graph Color')
    create_donut_plot(values, central_column='Success', colors=color_map, center_top_slice=True)
