import pandas as pd

data = pd.read_csv("2019_kbo_for_kaggle_v2.csv")

pd.set_option("display.max_columns", None)

print("======== 2-1-1 ========")
year_list = [2015, 2016, 2017, 2018]
for year in year_list:
    data_divided_by_year = data[data["year"] == year]
    H_top_10_batters = data_divided_by_year.sort_values(by="H", ascending=False)[:10]
    avg_top_10_batters = data_divided_by_year.sort_values(by="avg", ascending=False)[:10]
    HR_top_10_batters = data_divided_by_year.sort_values(by="HR", ascending=False)[:10]
    OBP_top_10_batters = data_divided_by_year.sort_values(by="OBP", ascending=False)[:10]
    
    print("=== ", year, " ===")
    print("H Top 10")
    print(H_top_10_batters[["batter_name", "H"]].to_markdown(index=False))
    print("avg Top 10")
    print(avg_top_10_batters[["batter_name", "avg"]].to_markdown(index=False))
    print("HR Top 10")
    print(HR_top_10_batters[["batter_name", "HR"]].to_markdown(index=False))
    print("OBP Top 10")
    print(OBP_top_10_batters[["batter_name", "OBP"]].to_markdown(index=False))
    print()

print("======== 2-1-2 ========")
data_2018 = data[data["year"] == 2018]
cp_list = ["포수", "1루수", "2루수", "3루수", "유격수", "좌익수", "중견수", "우익수"]
highest_war_players = pd.DataFrame()
for cp in cp_list:
    highest_war_player = data_2018[data_2018["cp"] == cp].sort_values(by="war", ascending=False)[:1]
    highest_war_players = pd.concat([highest_war_players, highest_war_player])

print("=== 2018 highest war player ===")
print(highest_war_players[["cp","batter_name", "war"]].to_markdown(index=False))
print()

print("======== 2-1-3 ========")
property_data = data[["R", "H", "HR", 'RBI', 'SB', 'war', "avg", 'OBP', "SLG"]]
correlation_with_salary_by_property = property_data.corrwith(data.salary)
highest_correlation_with_salary = correlation_with_salary_by_property.sort_values(ascending=False)[:1]

print("=== correlation with salary ===")
print(correlation_with_salary_by_property)
print("=== highest correlation with salary ===")
print(highest_correlation_with_salary)
print()