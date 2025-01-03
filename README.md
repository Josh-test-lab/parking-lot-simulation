# Parking Lot Simulation

## Description

This simulation is about the parking problem in the parking lot of Zhixue station, and it is also a part of the final project for class of simulation study, NDHU, R.O.C. (Taiwan) at fall 2024. In this parking lot simulation, we want to know whether the current and renovated parking lots at Zhixue Station can solve the problem of insufficient parking spaces, and propose improvement projects based on the results of the simulation experiment.

| *Info*                  | *Contents*                                                                                                                                  |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Title**           | Parking model for the parking lot in Zhixue station                                                                                           |
| **Author**          | Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee                                                                                                     |
| **Version**         | 1140102                                                                                                                                       |
| **Reference**       | Please view the complete reference below                                                                                                      |
| **Github**          | https://github.com/Josh-test-lab/parking-lot-simulation/                                                                                      |
| **Google Calender** | https://calendar.google.com/calendar/embed?src=c_7b5c1307c48fd66cdba1307b1c698cf1d1f71d90f64bf6466efbace8e6649e35%40group.calendar.google.com |
| **Flowchart**       | https://github.com/Josh-test-lab/parking-lot-simulation/tree/main/flowchart                                                                   |
| **Report**          | https://github.com/Josh-test-lab/parking-lot-simulation/blob/main/report.pdf                                                                  |
| **Presentation**    | https://github.com/Josh-test-lab/parking-lot-simulation/blob/main/presentation.pdf                                                            |

## The datasets

- Before collation

1. Google forms                    >> https://forms.gle/pb4kDFdQ7t1DetKK8
2. `觀察紀錄簿.xlsx`               >> A data set manually recorded during the interview, including the complete number of people entering and exiting the station and the status of the parking lot.
3. `人流樣態表單 (1131204早).xlsx` >> Questionnaire data of 2024.12.04 morning.
4. `人流樣態表單 (1131204晚).xlsx` >> Questionnaire data of 2024.12.04 afternoon.

- After collation

1. `dataset_sort1.0.xlsx`                >> The organized dataset.
2. `Estimate num_passengers_v1226.xlsx`  >> The trial estimation for many parameters of target distributions.

## The Python files

1. `main_program.py` >> The main program (simulation) project.
2. `parking_test.py` >> To test whether all the events in `event.py` executes as expected.
3. `event.py`        >> The events of the simulation.
4. `function.py`     >> Other functions.

## The R files

1. `Parking_Lot_System.Rmd` >> The simple model with car and motorcycle only.

## The Scenarios

1. Scenarios 1 >> Unlimited Parking Spaces.
2. Scenarios 2 >> Pre-Renovation Parking Lot.
3. Scenarios 3 >> Post-Renovation Parking Lot.

## References

1. 李婉寧 (2015)。 *路外停車場服務評鑑指標設計之研究：以台北市公有委外平面停車場為例。* 臺灣博碩論文知識加值系統。https://hdl.handle.net/11296/zzqjxr
2. 法務部 (2022)。 *利用空地申請設置臨時路外停車場辦法。* 全國法規資料庫。 https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0040034
3. 張存薇 (2018)。 *台東火車站汽機車停車收費 10月上路。* 自由時報。 https://news.ltn.com.tw/news/life/breakingnews/2555469
4. 國立東華大學 (2023)。 *花蓮縣議會徐雪玉副議長協調臺鐵局增設志學站前停車場，解決東華學子及居民停車問題。* 東華新聞。 https://www.ndhu.edu.tw/p/406-1000-213698,r4956.php?Lang=zh-tw
5. 國營臺灣鐵路股份有限公司 (2023)。 *停車場收費標準一覽表。* https://www.railway.gov.tw/tra-tip-web/tip/file/bc00c5d2-2184-4dbd-bbc4-530a9a3fb83a
6. 國營臺灣鐵路股份有限公司 (2024)。 *臺鐵每日各站點進出站人數。* 政府資料開放平臺。 https://data.gov.tw/dataset/8792
7. 國營臺灣鐵路股份有限公司 (2024)。 *臺鐵每日各站點進出站人數。* 交通部政府資料開放專區。 https://www.motc.gov.tw/201506260001/app/govdata_list/view?module=&id=1615&uid=201705110158
8. 國營臺灣鐵路股份有限公司 (2024)。 *臺鐵全線剩餘票。* 政府資料開放平臺。 https://data.gov.tw/dataset/37933
9. A. M. Law, & W. D. Kelton (2007). *Simulation Modeling and Analysis* (4th ed.). Mcgraw-Hill.
10. Chia-Li Wang (2024). *AM 609 Simulation Study.* National Dong Hwa University. https://sys.ndhu.edu.tw/RD/TeacherTreasury/tlist.aspx?tcher=19
11. R. C. Larson, & A. R. Odoni (1981). *Urban Operation Research.* Massachusetts Institute of Technology. https://web.mit.edu/urban_or_book/www/book/index.html

## Version history

- 1140103
1. Upload the `Parking_Lot_System.Rmd`.

- 1140102

1. Upload the report v1 and the presentation v1.

- 1131230

1. Update report.
2. Update briefing.
3. Update simulation results.
4. Make GIF.

- 1131229

1. Update report.
2. Update briefing.
3. Update simulation results.
4. Make GIF.

- 1131228

1. Detailed parameter adjustment.
2. Update main porgram and main function `parking simulate()`.
3. Update `Estimate num_passengers_v1226.xlsx`.
4. Update all initial values.
5. Release version 1.0 (not contain `vehicle_occupied_long_term_event()`).
6. Add new event `vehicle_occupied_long_term_event()`.
7. Release version 2.0 (contain `vehicle_occupied_long_term_event()`).
8. Update `README.md`.

- 1131227

1. Bug fixed.
2. Add new features into the picture.
3. Update all probabilities in `initial_value_example.json` and other files about initial values.

- 1131226

1. Make three results to csv files.
2. Analysis results.

- 1131225

1. Upload `parking_test.py` for some details.
2. Update `initial_value_example.json` and update more initial values for each scenario for adding more values.
3. Update `parking_simulate()`, `generate_new_passengers_per_hour()`, `generate_new_vehicles_per_hour()` in `function.py`.
4. Update `main_program.py`.
5. Add `save_result_to_csv()` function to save the results from data frame to csv files.

- 1131224

1. Upload `parking_test.py` for testing all events.
2. Update `README.md`.
3. Update `initial_value_example.json` and upload more initial values for each scenario.
4. Update `Estimate num_passengers_v1224.xlsx`.
5. Update flowcharts.
6. Update `bicycle_parked_in_motorcycle_space_event()` and `bicycle_left_motorcycle_space_event()` in `event.py`.
7. Update `main_program.py`.
8. Add the function `parking_simulate()` in `function.py` to simulate of different scenarios, which is built from `main_program.py`.

- 1131223

1. Report writing.
2. Briefing production.

- 1131222

1. Modified some names of parameters.
2. Upload the parameters estimation file `Estimate num_passengers_v1222.xlsx`.
3. Update `README.md`.
4. Finish the flowcharts of events.

- 1131221

1. Upload the parameters estimation file `Estimate num_passengers_1221.xlsx`.
2. Update flowcharts.

- 1131220

1. Modify parts of the code in `main_program.py` and `event.py` to simplify the model.
2. Create a `function.py` file to store functions other than those related to events.
3. Organize the references and create the report.

- 1131219

1. Fix problems in `event.py`.
2. Improve the code for simulation experiments in `main_program.py` (except passenger distribution).
3. Update `README.md`.

- 1131218

1. Complete all departure events.
2. `README.md` file update.
3. Data sorting and uploading.
4. Try to convert initial values into a json file.

- 1131217

1. Parking events bug fixed.
2. Plan to leave events.

- 1131216

1. Start the project.
2. Build the repository of [parking-lot-simulation](https://github.com/Josh-test-lab/parking-lot-simulation) in Github.
3. build `main_program.py`, `event.py`, `README.md` files.
4. Complete the parking events.

- ~ 1131215

1. Data collection (questionnaire survey).

## Future plans

* [X] Initial system setup. (To be completed by Hsu.)
* [X] Organize references and format them in APA style. (To be completed by Sin.)
* [X] Add data on the number of people entering and exiting stations during different time periods and the proportions of transportation modes used. (To be completed by Sin.)
* [X] Passenger distribution across different time periods. (To be completed by Xie and Hsu.)
* [X] Create the main flowchart. (To be completed by Xie and Hsu.)
* [X] Create flowcharts for individual events. (To be completed by Hsu and Sin.)
* [X] Identify parameters that may need to be collected for the model.
* [X] Optimize and debug the model.
* [X] Complete system setup. (To be completed by Hsu, Xie, and Sin.)
* [ ] Phase 2: Increase model complexity (e.g., incorporate holidays, festivals, or other conditions).
* [X] Weekly meetings.
