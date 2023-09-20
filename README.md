# donut-plot
This is a simple plotting function built upon the Plotly library. This plot is essentially a donut plot, but the radius of the donut hole scales with one of the data points, effectively plotting that "slice" in the center of the circle.

Outside of aesthetic purposes, the plot doesn't do anything special. My best example for it is shown below. I'd wager you are always better off using two pie charts or a single sunburst plot to convey the same information.

# Example
Given the following data out of 100 tests:
| Outcome  | Quantity |
| ------------- | ------------- |
| Success  | 70  |
| Error 1  | 3  |
| Error 2 | 7 |
| Error 3 | 20 |

You'd like to generate a plot that conveys 2 things:
1) The majority of our tests were successful (70%). This will be achieved through the AREA of the chart occupied by each category (proportional to total population).
2) The majority of errors fall under "Error 3" (66% of errors). This will be achieved through the ANGLE each slice occupies in the outer ring (proportional to error population).

Using this plotting function, we can plot the Success count in the middle of the donut. This takes up a large area of the plot, which conveys that many of our tests ran without errors.
The errors will then be plotted in the outer radius of the plot (the donut). This makes it easy to compare the prevalence of each error code in the tests that failed.

![alt text](https://github.com/AndyWilliams682/donut-plot/blob/main/image.jpg?raw=true)
