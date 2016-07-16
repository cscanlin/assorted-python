import pandas as pd
import numpy as np

df =pd.DataFrame({'A': ['foo', 'foo', 'foo', 'foo',
                             'bar', 'bar', 'bar', 'bar',
                             'foo', 'foo', 'foo'],
                       'B': np.random.randn(11),
                       'C': np.random.randn(11)})

print(df)
#
aggs = {'B':'sum', 'C':'mean'}

agg_values_gen = (value for value in ['D', 'E'])

print(aggs.items())

pivot_output = pd.pivot_table(
    df,
    index=['A'],
    values=aggs.keys(),
    aggfunc=aggs,
)

print(pivot_output)
