import pandas as pd
pd.set_option('display.encoding','utf-8')

day_df = pd.read_excel('C:/Users/wenle/Downloads/day.xlsx')
night_df = pd.read_excel('C:/Users/wenle/Downloads/night.xlsx')

merge_df = pd.concat([day_df,night_df])
merdf = merge_df.drop(['如果志學站停車場將進行收費，您一天願意支付多少錢停放機車？', '您此次到志學站的目的是什麼？ ', 	
               '您偏好使用何種交通工具 前往/離開 志學站？',	'如果志學站停車場將進行收費，您一天願意支付多少錢停放汽車？','其他建議'],axis=1)

merdf.to_excel(r'C:/Users/wenle/Downloads/mergedf.xlsx',index=False)

df = pd.read_excel('C:/Users/wenle/Downloads/mergedf.xlsx')
data2 = pd.read_excel('C:/Users/wenle/Downloads/observe.xlsx')
drop_df = data2.drop(['日期','對應車種車次','方向','出站人數',	'進站人數','學生',	'其它人士'
,'期望步行','期望單車','期望機車','期望汽車','停車場汽車數量','停車場機車數量','停車場單車數量','機車格','汽車格'],axis=1)
mapdf = drop_df.to_excel(r'C:/Users/wenle/Downloads/mapdf.xlsx',index=False)


