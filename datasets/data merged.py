import pandas as pd
pd.set_option('display.encoding','utf-8')

day_df = pd.read_excel('C:/Users/wenle/Downloads/day.xlsx')
night_df = pd.read_excel('C:/Users/wenle/Downloads/night.xlsx')

merge_df = pd.concat([day_df,night_df])

merge_df.to_excel(r'C:/Users/wenle/Downloads/mergedf.xlsx',index=False)

df = pd.read_excel('C:/Users/wenle/Downloads/mergedf.xlsx')
data2 = pd.read_excel('C:/Users/wenle/Downloads/observe.xlsx')
drop_df = data2.drop(['日期','對應車種車次','方向','期望步行',	'期望單車',
                      '期望機車','期望汽車','停車場汽車數量','停車場機車數量','停車場單車數量','機車格','汽車格'],axis=1)
mapdf = drop_df.to_excel(r'C:/Users/wenle/Downloads/mapdf.xlsx',index=False)

