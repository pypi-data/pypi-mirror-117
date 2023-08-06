import pandas as pd
import pickle as pkl


# with open('/Users/wuhf/PycharmProjects/Hypernets/hypernets/hn_widget/hn_widget/test/pkls/4g_PDCPUL_AFE97F546A10368F.pkl', 'r') as f:
#     o = pkl.load(f)
# print(o)
df = pd.read_pickle('/Users/wuhf/PycharmProjects/Hypernets/hypernets/hn_widget/hn_widget/test/pkls/4g_PDCPUL_AFE97F546A10368F.pkl')
print(df)


