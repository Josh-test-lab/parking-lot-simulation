"""
Information:
    Title = 'Data sortig for parking model for the parking lot in Zhixue station'
    Author = 'Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee'
    Version = [1131219]
    Reference = ['Class of Simulation Study by C. Wang at 2024 fall']
"""
import pandas as pd
import openpyxl
pd.set_option('display.encoding','utf-8')

#處理上下午問卷資料
day_df = pd.read_excel(r'datasets\before_collation\人流樣態表單 (1131204早).xlsx')
night_df = pd.read_excel(r'datasets\before_collation\人流樣態表單 (1131204晚).xlsx')
merge_df = pd.concat([day_df,night_df])
merge_df['時間戳記'] = pd.to_datetime(merge_df['時間戳記'])
merge_df['時間戳記'] = merge_df['時間戳記'].dt.time
merge_df['您此次到志學站：'] = merge_df['您此次到志學站：'].replace(['領車票', '即將搭乘火車', '晚點搭車', '取票'], '進站')
merge_df['您此次到志學站：'] = merge_df['您此次到志學站：'].replace(['剛抵達並下火車'], '出站')
merdf = merge_df.drop(['如果志學站停車場將進行收費，您一天願意支付多少錢停放機車？', 
                       '您此次到志學站的目的是什麼？ ', 
                       '您偏好使用何種交通工具 前往/離開 志學站？',	
                       '如果志學站停車場將進行收費，您一天願意支付多少錢停放汽車？', 
                       '其他建議'], 
                       axis = 1)
merdf.to_excel(r'datasets\after_collation\mergedf.xlsx', index = False)

#處理軒哥觀察資料
df = pd.read_excel(r'datasets\after_collation\mergedf.xlsx')
data2 = pd.read_excel(r'datasets\before_collation\觀察紀錄簿.xlsx')
drop_df = data2.drop(['日期','對應車種車次','方向','出站人數',	'進站人數','學生',	'其它人士'
,'期望步行','期望單車','期望機車','期望汽車','停車場汽車數量','停車場機車數量','停車場單車數量','機車格','汽車格'], axis = 1)
mapdf = drop_df.to_excel(r'datasets\after_collation\mapdf.xlsx', index = False)

