import pandas as pd


def calc_D(d:pd.Series) -> pd.Series:
    D = (4/(math.pi*kwargs['tau']))*(np.square(((kwargs['m']*kwargs['V'])/(kwargs['M']*kwargs['S'])))*np.square(divDelta))    
    return D

def calculate_deltaet(dchg_df: pd.DataFrame) -> pd.Series:
    voltage_groupby = dchg_df.groupby(['Cycle ID', 'Step ID', 'Record ID'])['Voltage(V)']
    deltaet = abs(voltage_groupby.nth(1) - voltage_groupby.last())
    return deltaet

def calculate_deltaes(rest_df: pd.DataFrame) -> pd.Series:
    voltage_groupby = rest_df.groupby(['Cycle ID', 'Step ID', 'Record ID'])['Voltage(V)']
    deltaes = abs(voltage_groupby.last() - voltage_groupby.last().shift(-1))
    return deltaes

def calculate_rohm(df: pd.DataFrame) ->pd.Series:
    voltage_groupby = df.groupby(['Cycle ID', 'Step ID', 'Record ID'])['Voltage(V)']
    rohm = abs(voltage_groupby.last() - voltage_groupby.nth(1).shift(1))
    return rohm

def calculate_rpol(rest_df: pd.DataFrame) -> pd.Series:
    voltage_groupby =  df.groupby(['Cycle ID', 'Step ID', 'Record ID'])['Voltage(V)']
    rpol = abs(voltage_groupby.last() - voltage_groupby.nth(1))
    return rpol

def calculate_utitr(dchg_df: pd.DataFrame) -> pd.Series:
    voltage_groupby =  df.groupby(['Cycle ID', 'Step ID', 'Record ID'])['Voltage(V)']
    utitr = voltage_groupby.last()
    return utitr

def calculate_d(deltaet:pd.Series, deltaes:pd.Series) -> pd.Series:
    d = deltaes/deltaet
    D = calc_D(d)
    return D


def calculate_mean_if_rest(df:pd.DataFrame) -> pd.Series:
    groupby_df = df.shift(5).groupby(['Cycle ID', 'Record ID'])['Voltage(V)']
    mean_vol = groupby_df.mean()
    return mean_vol

def calculate_mean_no_rest(df:pd.DataFrame) -> pd.Series:
    groupby_df = df.groupby(['Cycle ID', 'Record ID'])['Voltage(V)']
    mean_vol = groupby_df.mean()
    return mean_vol
