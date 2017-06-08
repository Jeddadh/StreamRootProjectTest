
# import different modules
import pandas as pd

##### DATA IMPORTATION
file_name = "data (1).csv"
stream_data = pd.DataFrame(pd.read_csv(file_name))

# stream are numbers, so we must convert them to not be interpreted as numbers
stream_data['#stream'] = stream_data['#stream'].astype(object)

# adding the tree columns
stream_data['data_downloaded'] = stream_data['p2p'] + stream_data['cdn']
stream_data['p2p_percentage'] = stream_data['p2p']/stream_data['data_downloaded']
stream_data['cdn_percentage'] = stream_data['cdn']/stream_data['data_downloaded']

# Data Global description
data_describe = stream_data.describe(include="all")
print( "-- this is the first data description : ")
print(data_describe)
print("--")

# delete rows that contains nan
stream_data = stream_data.dropna(axis=0, how='any')
data_describe = stream_data.describe(include="all")
print("-- this is an other data description after deleting nans: ")
print(data_describe)
print("--")
print("-- Head of data")
print(stream_data.head())
print("--")

# Grouped by different variables
data_group_stream = stream_data.groupby(["#stream"]).mean()
print("-- data grouped by stream id")
print(data_group_stream)
print("--")
data_group_isp = stream_data.groupby(["isp"]).mean()
print("-- data grouped by isp : ")
print(data_group_isp)
print("--")
print("-- data grouped by browser")
data_group_browser = stream_data.groupby(["browser"]).mean()
print(data_group_browser)
print("--")

data_group_connected = stream_data.groupby(["connected"]).mean()
print("-- data grouped by connected")
print(data_group_connected)
print("--")


# frequence of utilisation of every browser
freq_use_browser = stream_data['browser'].value_counts(normalize=True)
print(" percentage of use of browsers")
print(freq_use_browser)
print("--")



# number of connected users by browser
n_connect_browser = pd.pivot_table(stream_data, values='p2p_percentage', index=['browser'],columns=['connected'], aggfunc="count")
def f(x):
    return(x/sum(x))
# frequence of connected users by browser
freq_connect_browser = n_connect_browser.apply(f, axis=0)
print("percentage of connected users by browser")
print(freq_connect_browser)
print("--")

# mean of p2p_percentage by isp and browser
mean_p2p_isp_browser = pd.pivot_table(stream_data, values='p2p_percentage', index=['isp'],columns=['browser'], aggfunc="mean")
print("mean of p2p_percentage by isp and browser")
print(mean_p2p_isp_browser)
print("--")

# mean of p2p_percentage by steam and browser
mean_p2p_vdeo_browser = pd.pivot_table(stream_data, values='p2p_percentage', index=['#stream'],columns=['browser'], aggfunc="mean")
print("mean of p2p_percentage by vdeo and browser")
print(mean_p2p_vdeo_browser)
print("--")

# mean of p2p_percentage by steam and isp
mean_p2p_vdeo_isp = pd.pivot_table(stream_data, values='p2p_percentage', index=['#stream'],columns=['isp'], aggfunc="mean")
print("mean of p2p_percentage by vdeo and isp")
print(mean_p2p_vdeo_isp)
print("--")
