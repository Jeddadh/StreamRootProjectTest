
# import different modules
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
##### DATA IMPORTATION
file_name = "data (1).csv"
stream_data = pd.read_csv(file_name)
stream_data = pd.DataFrame(stream_data)


# stream_data["data_downloaded"] = stream_data["p2p"]+stream_data["cdn"]
stream_data['#stream'] = stream_data['#stream'].astype(object)

stream_data['data_downloaded'] = stream_data['p2p'] + stream_data['cdn']
stream_data['p2p_percentage'] = stream_data['p2p']/stream_data['data_downloaded']
stream_data['cdn_percentage'] = stream_data['cdn']/stream_data['data_downloaded']


#####
# Group data by strea id
data_group_stream = stream_data.groupby(["#stream"]).mean()

# ploting the mean of p2p_percentage by video id
plt.figure("figure 1 : mean of p2p_percentage by video")
plt.ylabel("mean of p2p_percentage")
plt.title("mean of p2p_percentage / video")
plt.ylim((0,1))
data_group_stream["p2p_percentage"].plot(kind='bar')

# frequence of every video
freq_video = stream_data['#stream'].value_counts(normalize=True)
plt.figure("figure 2 : percentage of every video")
plt.title("percentage of every video")
freq_video.plot.pie(autopct='%.2f',figsize=(4, 6))

# group data by isp name
data_group_isp = (stream_data.groupby(["isp"]).mean())
# ploting the mean of p2p_percentage by isp
plt.figure("figure 2 : mean of p2p_percentage by isp")
plt.ylabel("mean of p2p_percentage")
plt.title("mean of p2p_percentage / isp")
plt.ylim((0,1))
data_group_isp["p2p_percentage"].plot(kind='bar')

# group by browser
data_group_brower = stream_data.groupby(["browser"]).mean()
# ploting the mean of p2p_percentage by browser
plt.figure("figure 3 : mean of p2p_percentage by browser")
plt.ylabel("mean of p2p_percentage")
plt.title("mean of p2p_percentage / browser")
plt.ylim((0,1))
data_group_brower["p2p_percentage"].plot(kind='bar')

# percentage of use of browsers
freq_use_browser = stream_data['browser'].value_counts(normalize=True)
plt.figure("figure 4 : percentage of use of browsers")
plt.title("percentage of use of browsers")
freq_use_browser.plot.pie(autopct='%.2f',figsize=(4, 6))

# group by connected
data_group_connected = stream_data.groupby(["connected"]).mean()
# ploting the mean of p2p_percentage by connected
plt.figure("figure 4 : mean of p2p_percentage by connected")
plt.ylabel("mean of p2p_percentage")
plt.title("mean of p2p_percentage / connected")
plt.ylim((0,1))
data_group_connected["p2p_percentage"].plot(kind='bar')


# number of connected users by browser
n_connect_browser = pd.pivot_table(stream_data, values='p2p_percentage', index=['browser'],columns=['connected'], aggfunc="count")
def f(x):
    return(x/sum(x))
# frequence of connected users by browser
freq_connect_browser = n_connect_browser.apply(f, axis=0)
plt.figure("figure 5 : percentage of connected users by browser")
plt.title("percentage of connected users by browser")
freq_connect_browser.plot(kind='bar')


plt.ioff()
plt.show()
