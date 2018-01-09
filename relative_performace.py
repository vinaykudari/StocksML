import pandas as pd 
import matplotlib.pyplot as plt
import os

def get_symbols():
    symbols = []

    for filename in os.listdir("data"):
        filename = os.path.join("data/",filename)
        symbols.append(filename)

    return symbols

def create_dataframe():
    start_date = input("Enter the start date : ")
    end_date = input("Enter the end date : ")
    dates = pd.date_range(start_date,end_date)
    df = pd.DataFrame(index=dates)

    return df

def append_to_dataframe(symbols,df):

    for sym in symbols:
        df_temp = pd.read_csv(sym,index_col='Date',
                                  parse_dates=True,
                                  usecols=['Date','Close'],
                                  na_values=['nan'])
        df_temp = df_temp.rename(columns={'Close' : sym})
        df = df.join(df_temp,how='inner')
    df = df / df.ix[0,:]
    return df

def plot_data(df):
    df.plot()
    plt.show()

if __name__ == "__main__":

    symbols = get_symbols()
    df = create_dataframe()
    dataframe = append_to_dataframe(symbols,df)
    plot_data(dataframe)
