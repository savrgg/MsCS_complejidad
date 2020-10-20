import numpy as np
import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

from src.merge_sort import mergeSort
from src.merge_sort import merge
from src.insertion_sort import insertionSort
from src.merge_time import merge_time
from src.insertion_time import insertion_time
from src.simular_arreglos import simular_arreglos

sns.set_theme(style="darkgrid")
%matplotlib inline

sim_array = simular_arreglos(tam = 3000)

df_times = pd.DataFrame(sim_array)
df_times["iter"] = range(1, 3000, 10)

df_times2 = pd.DataFrame.copy(df_times)
df_times2["c_insert"] = df_times2["insertion"]/(df_times2["iter"]*df_times2["iter"])
df_times2["c_merge"] = df_times2["merge"]/(df_times2["iter"]*sp.log2(df_times2["iter"]))
df_times2 = df_times2.loc[:,('iter','c_insert', 'c_merge')] 

df_times = pd.melt(df_times, id_vars = "iter", var_name = "algo", value_name = "time")
df_times2 = pd.melt(df_times2, id_vars = "iter", var_name = "algo2", value_name = "time_norm")

df_times3 = pd.concat([df_times.reset_index(drop=True), df_times2.loc[:,('time_norm') ]], axis=1)
df_times3 = pd.melt(df_times3, id_vars = ["iter", "algo"], var_name = "algo2", value_name = "time_norm")


plt.figure()
g = sns.set_style("whitegrid")
g = sns.FacetGrid(df_times3[df_times3['iter'] > 100], col="algo2", sharey=False, height=6)
g.fig.suptitle('Comparación del tiempo de Insertion Sort y Merge Sort') # can also get the figure from plt.gcf()
g = g.map(sns.lineplot, "iter", "time_norm", "algo")
g.axes[0,0].set_xlabel('Iteración')
g.axes[0,1].set_xlabel('Iteración')
g.axes[0,0].set_ylabel('Tiempo')
g.axes[0,0].set_title('Tiempo total de ejecución para cada algoritmo')
g.axes[0,1].set_title('Valor de la constante para cada algoritmo')
g.add_legend(title='Algoritmo')
plt.savefig("graphs/total_time.png")

plt.figure()
g = sns.set_style("whitegrid")
g = sns.FacetGrid(df_times3[(df_times3['iter'])> 2][df_times3['iter'] < 100], col="algo2", sharey=False, height=6)
g.fig.suptitle('Comparación del tiempo de Insertion Sort y Merge Sort') # can also get the figure from plt.gcf()
g = g.map(sns.lineplot, "iter", "time_norm", "algo")
g.axes[0,0].set_xlabel('Iteración')
g.axes[0,1].set_xlabel('Iteración')
g.axes[0,0].set_ylabel('Tiempo')
g.axes[0,0].set_title('Tiempo total de ejecución para cada algoritmo')
g.axes[0,1].set_title('Valor de la constante para cada algoritmo')
g.add_legend(title='Algoritmo')
plt.savefig("graphs/constant_time.png")

#print(df_times2)
#print(df_times3)

