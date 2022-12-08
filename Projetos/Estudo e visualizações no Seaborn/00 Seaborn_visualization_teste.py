# [J]efferson , Eng. De Produção
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

px.set_mapbox_access_token('pk.eyJ1IjoiamVmZmVyc29uMTcwNzEzIiwiYSI6ImNsYXk1dHB4dTB2dTEzcG9ib3J2N3RrdGMifQ.jztPaI0tQyqvRUDJDZsLJw')
df_sp = pd.read_csv('sao-paulo-properties-april-2019.csv')

df_rent = df_sp[df_sp['Negotiation Type'] == 'rent']

fig = px.scatter_mapbox(data_frame=df_rent, lat='Latitude', lon='Longitude', color='Price',
                       size='Size', color_continuous_scale=px.colors.cyclical.IceFire, size_max=10, zoom=10,
                        opacity=0.6)
#open-street-map aqui é um parâmetro de mapbox_style=""
#fig.update_layout(mapbox_style='open-street-map', overwrite=False)
#fig.update_layout(margin={"r":0,"t":0,"l":10,"b":5})
fig.update_coloraxes(
        colorscale=[
            [0,'rgb(166,206,227,0.5)'],
            [0.02,'rgb(31,120,180, 0.5)'],
            [0.05,'rgb(178,223,138, 0.5)'],
            [0.10,'rgb(51,160,44, 0.5)'],
            [0.15,'rgb(251,154,153, 0.5)'],
            [1,'rgb(227,26,28, 0.5)']
        ]
)
fig.update_layout(height=800, mapbox=dict(center=go.layout.mapbox.Center(lat=-23.543138, lon=-46.69486)))
fig.show()