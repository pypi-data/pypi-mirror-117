import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import numpy as np
import cv2

def overall_growth(df,ax=None, **kwargs):
    """
    This is a function to generate growth curve plots
    
    Args:
        df (pandas.DataFrame):
            Pandas Dataframe containing biomass data over time

        ax (plt.ax):
            Axis to plot data on
        
        **kwargs
    """
    Biomass = df
    ax.plot(Biomass.iloc[:,1],label='S. elongatus',color='#2ca25f')
    ax.plot(Biomass.iloc[:,2],label='E. coli', color ='#de2d26')
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Biomass (fg)')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(frameon=False)
    ax.set_yscale('log')
    return ax
    
def average_nutrients(df,nutrient,ax=None,legend = None,**kwargs):
    """
    This is a function to plot the nutrient concentration over time
    
    Args:
        df (pandas.DataFrame):
            Pandas Dataframe containing nutrient data

        nutrient (str):
            Name of the nutrient to plot, e.g., ``'Sucrose'``

        ax:
            Axis on which to make the plot

        legend (bool):
            Include legend in the plot

        **kwargs:
            Additional arguments to pass to plt.plot
    """
    sns.set_context('talk')
    sns.set_style('white')
    avgc = df

    ax = ax or plt.gca()
    if nutrient == 'Sucrose':
        ax.plot(avgc.iloc[:,1],label='Sucrose',**kwargs)
    elif nutrient == 'CO2':
        ax.plot(avgc.iloc[:,2],label='CO2',**kwargs)
    elif nutrient == 'O2':
        ax.plot(avgc.iloc[:,0],label='O2',**kwargs)
    else:
        print('No nutrient specified')
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Concentration (mM)')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    if legend:
        ax.legend(frameon=False)
    return ax
def biomass_time(df,id=None,ax=None,legend = None,**kwargs):
    """
    This is a function to plot the cell biomass over time
    
    Args:
        df (pandas.DataFrame):
            Pandas Dataframe containing biomass data

        ax:
            Axis on which to make the plot

        legend (bool):
            Include legend in the plot

        **kwargs:
            Additional arguments to pass to plt.plot
    """
    ax = ax or plt.gca()
    #plot cell size vs time
    palette = sns.color_palette("mako_r", 6)
    if not id:
        print('No cell ID specified')
    else:
        data = df[df.id==id].reset_index()
        ax.plot(data.time,data.biomass,color='#2ca25f')

        for line in find_peaks(data.biomass):
            ax.vlines(data.time[line],data.biomass.min(),data.biomass.max()*1.1,color='#bdbdbd',ls=':')
        ax.set_xlabel('Time (hours)')
        ax.set_ylabel('Biomass (fg)')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        sns.despine()
        if legend:
            ax.legend(frameon=False)
        return ax
def growth_curve_panel(df,**kwargs):
    """
    Make growth curves panel with all cells

    Args:
        df (pandas.DataFrame):
            Pandas Dataframe containing biomass data

        **kwargs:
            Additional arguments to pass to plt.plot
    """

    rows=round(np.sqrt(len(df.id.unique())))
    cols = int(np.ceil(len(df.id.unique())/rows))
    fig ,axes = plt.subplots(nrows=rows,ncols=cols,sharex=True,figsize=(14,8))
    axs = axes.ravel()
    for i in df.id.unique():
        celltype=df[(df.id==i) & (df.time ==0)].type.values[0]
        if celltype==1:
            color = '#2ca25f'
        elif celltype ==2:
            color = '#de2d26'
        elif celltype ==0:
            print('Celltype is 0',i,celltype)
        axs[i-1].plot(df[(df.id==i)].biomass.values,c=color)
        #axs[i].set_title(f['type']['0'][c])
    for ax in axs:
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_axis_off()
    return fig

def growth_rate_div(df, **kwargs):
    """
    Plot a heatmap of the single cell growth rates relative to each division

    Args:
        df (pandas.DataFrame):
            Pandas Dataframe containing biomass data

        **kwargs:
            Additional arguments to pass to plt.plot
    """
    fig, axes = plt.subplots(ncols=2,figsize=(14,7))
    celltypes = df.type.unique()
    celltypes.sort()
    for ct in celltypes:
        divs = pd.DataFrame(columns=['id','division','rate'])
        cells = df.id.unique()
        #cells.sort()
        for cell in cells:
            data = df[(df.id==cell) & (df.type==ct)].reset_index()
            pks,_ = find_peaks(data.biomass)
            p0 = 0
            for i,p1 in enumerate(pks):
                #plt.plot(data.time[p0:p1],data.diameter[p0:p1])
                #plt.show()
                dt = data.time[p1]-data.time[p0]
                dy = data.biomass[p1]-data.biomass[p0]
                dydt = dy/dt
                divs = divs.append(pd.DataFrame([[cell,i+1,dydt]],columns=['id','division','rate']),ignore_index=True)
                #print(dydt)
                p0=p1+1
        #plot cell id vs division rate over time
        piv = divs.pivot_table(index='id', columns='division', values='rate')
        g = sns.heatmap(piv, cmap='coolwarm',ax=axes[ct-1])
        cbar = g.collections[0].colorbar
        cbar.ax.set_ylabel(r'Growth rate ($\frac{fg}{hr}$)')
    axes[0].set_title('S. elongatus')
    axes[1].set_title('E. coli')
    fig.tight_layout()
    return
def growth_rate_time(df, period =3):
    """
    Plot a heatmap of the single cell growth rates over time

    Args:
        df (pandas.DataFrame):
            Pandas Dataframe containing biomass data

        period (int):
            Number of timesteps to average growth rate calculation over

        **kwargs:
            Additional arguments to pass to plt.plot
    Returns:
        matplotlib.figure.Figure
    """
    periods = period
    df['rate'] = df.diff(periods=periods).biomass/df.diff(periods=periods).time
    df['rate'][df.rate < 0] = 0

    sns.set_context('talk')
    df.time = df.time.round(1)
    fig, axes = plt.subplots(ncols=2,figsize=(14,7))
    celltypes = df.type.unique()
    celltypes.sort()
    for ct in celltypes:
        rates = df[df.type==ct][['id','time','rate']]
        #plot cell id vs division rate over time
        piv = rates.pivot_table(index='id',columns='time', values='rate')
        g = sns.heatmap(piv, cmap='coolwarm',ax=axes[ct-1])
        cbar = g.collections[0].colorbar
        cbar.ax.set_ylabel(r'Growth rate ($\frac{fg}{hr}$)')
        #axes[ct-1].xaxis.set_major_locator(plt.MaxNLocator(5))
        axes[ct-1].set_xticklabels(axes[ct-1].get_xticklabels(), rotation=0) 
        axes[ct-1].locator_params(axis="x", nbins=6)
        axes[ct-1].set_xlabel('Time (hrs)')
        
    axes[0].set_title('S. elongatus')
    axes[1].set_title('E. coli')

    fig.tight_layout()
    return

def get_growth_intervals(dataframe,cellID):
    df = dataframe[dataframe.id==cellID].reset_index(drop=True)
    biomass = df.biomass
    time = df.time
    pks = find_peaks(biomass)[0]
    intervals = list()
    for i in range(len(pks)+1):
        if i == 0:
            intervals.append([df.index[0],pks[0]+1])
        elif i < len(pks):
            intervals.append([pks[i-1]+1,pks[i]+1])
        else:
            intervals.append([pks[i-1]+1,df.index[-1]])
    def func(t,y0,mu):
        return y0*np.exp(t*mu)
    cell_type = df.type.unique()[0]
    mu = list()
    for interval in intervals:
        y0 = df.iloc[interval[0],3]
        t = np.linspace(df.iloc[interval[0],2],df.iloc[interval[1],2],1000)
        t_measured = df.iloc[interval[0]:interval[1],2]
        biomass_measured = df.iloc[interval[0]:interval[1],3]
        popt, pcov = curve_fit(func, t_measured, biomass_measured)
        plt.plot(df.iloc[interval[0]:interval[1],2],df.iloc[interval[0]:interval[1],3])
        plt.plot(t_measured,func(t_measured, *popt),ls='--')
        mu.append(round(popt[1],4))
    return mu

def growth_rate_mu(df, **kwargs):
    """
    Plot a heatmap of the single cell growth rates relative to each division

    Args:
        df (pandas.DataFrame):
            Pandas Dataframe containing biomass data

        **kwargs:
            Additional arguments to pass to plt.plot
    """
    def func(t,y0,mu):
        return y0*np.exp(t*mu)
    celltypes = df.type.unique()
    celltypes.sort()
    fig, axes = plt.subplots(ncols=2,figsize=(14,7))
    for ct in celltypes:
        divs = pd.DataFrame(columns=['id','division','rate'])
        cells = df[df.type==ct].id.unique()
        cells.sort()
        for cell in cells:
            data = df[(df.id==cell) & (df.type==ct)].reset_index(drop=True)
            pks,_ = find_peaks(data.biomass)
            intervals = list()
            for i in range(len(pks)+1):
                if i == 0:
                    intervals.append([data.index[0],pks[0]+1])
                elif i < len(pks):
                    intervals.append([pks[i-1]+1,pks[i]+1])
                else:
                    intervals.append([pks[i-1]+1,data.index[-1]])


            for i,interval in enumerate(intervals):
                y0 = data.iloc[interval[0],3]
                t = np.linspace(data.iloc[interval[0],2],data.iloc[interval[1],2],1000)
                t_measured = data.iloc[interval[0]:interval[1],2]
                biomass_measured = data.iloc[interval[0]:interval[1],3]
                if len(biomass_measured) > 4:
                    popt, pcov = curve_fit(func, t_measured, biomass_measured)
                    #print(round(popt[1],4))
                    divs = divs.append(pd.DataFrame([[cell,i+1,round(popt[1],4)]],columns=['id','division','mu']),ignore_index=True)
                    #plot cell id vs division rate over time

        #plot cell id vs division rate over time
        piv = divs.pivot_table(index='id', columns='division', values='mu')
        g = sns.heatmap(piv, cmap='coolwarm',ax=axes[ct-1])
        cbar = g.collections[0].colorbar
        cbar.ax.set_ylabel(r'Growth rate ($\frac{1}{hr}$)')
    axes[0].set_title('S. elongatus')
    axes[1].set_title('E. coli')
    fig.tight_layout()
    return
def plot_colony(obj,time,id=None,ax=None,**kwargs):
    """Plot bacterial colonies at a specific timepoint

    Args:
        obj (nufeb_tools.utils.get_data): 
            Object containing cell positions and mother cell ID.
        time (int): 
            Timestep to plot
        id (int, optional): 
            Plot a specific colony ID, based on the mother cell ID. Defaults to None.
        ax (matplotlib.pyplot.axes, optional): 
            Axes object. Defaults to None.


    Returns:
            matplotlib.pyplot.axes: 
                Axes object.
    """
    ax = ax or plt.gca()
    timepoint = time
    scale = 1
    if not hasattr(obj,'colonies'):
        obj.get_mothers()
    df = obj.colonies
    tp = df[df.Timestep == timepoint]
    img_size = 2000
    bk = 255 * np.ones(shape=[img_size, img_size, 3], dtype=np.uint8)
    for i, colony in enumerate(tp.mother_cell.unique()):
        colony_type = tp[tp.mother_cell==colony].type
        colors = tuple(np.random.randint(0,256, 3).astype('int'))
        if not colony_type.empty:

            for cell in tp[tp.mother_cell==colony].itertuples():
                xloc = round(cell[5]/obj.metadata['Dimensions'][0]*img_size)
                yloc = round(cell[6]/obj.metadata['Dimensions'][1]*img_size)
                radius = round(cell[4]/obj.metadata['Dimensions'][0]*img_size*scale)
                
                cv2.circle(bk,center = (xloc,yloc),radius = radius,color = (int(colors[0]),int(colors[1]),int(colors[2])),thickness = -1)
    ax.imshow(bk)
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    return ax