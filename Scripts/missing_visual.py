import pandas as pd
import json

missing_data = pd.read_csv("../data/missing_data.csv")

split = [0.0, 12.5, 25.0, 37.5, 50.0, 62.5, 75.0, 87.5, 100.0]

result = {}

for i in range(len(split)):

	if i == 0:
		mask = (missing_data["Missing_percentage"] == split[i])
		result[split[i]] = missing_data.loc[mask, "Feature"].tolist()
	elif i == 1:
		mask = (missing_data["Missing_percentage"] > split[i-1]) & (missing_data["Missing_percentage"] < split[i])
		result[split[i]] = missing_data.loc[mask, "Feature"].tolist()
	else:

		if i == len(split) - 1:
			mask = (missing_data["Missing_percentage"] == split[i])
			result["Max"] = missing_data.loc[mask, "Feature"].tolist()

		mask = (missing_data["Missing_percentage"] >= split[i-1]) & (missing_data["Missing_percentage"] < split[i])
		result[split[i]] = missing_data.loc[mask, "Feature"].tolist()

	

tree_data = [
	{
		"name": "Missing data",
		"parent": "null",
		"children": [
			{
				"name": "data = 0.0",
				"parent": "Missing data",
				"children": [{"name": val, "parent": "data = 0.0"} for val in result[0.0]]
			},

			{
				"name": "0.0 < data < 50.0",
				"parent": "Missing data",
				"children": [
					{
						"name": "0.0 < data < 25.0",
						"parent": "0.0 < data < 50.0",
						"children": [
							{
								"name": "0.0 < data < 12.5",
								"parent": "0.0 < data < 25.0",
								"children": [{"name": val, "parent": "0.0 < data < 12.5"} for val in result[12.5]]
							},

							{
								"name": "12.5 <= data < 25.0",
								"parent": "0.0 < data < 25.0",
								"children": [{"name": val, "parent": "12.5 <= data < 25.0"} for val in result[25.0]]
							}
						]
					},

					{
						"name": "25.0 <= data < 50.0",
						"parent": "0.0 < data < 50.0",
						"children": [
							{
								"name": "25.0 <= data < 37.5",
								"parent": "25.0 <= data < 50.0",
								"children": [{"name": val, "parent": "25.0 <= data < 37.5"} for val in result[37.5]]
							},

							{
								"name": "37.5 <= data < 50.0",
								"parent": "25.0 <= data < 50.0",
								"children": [{"name": val, "parent": "37.5 <= data < 50.0"} for val in result[50.0]]
							}
						]
					}
				]
			},

			{
				"name": "50.0 <= data < 100.0",
				"parent": "Missing data",
				"children": [
					{
						"name": "50.0 <= data < 75.0",
						"parent": "50.0 <= data < 100.0",
						"children": [
							{
								"name": "50.0 <= data < 62.5",
								"parent": "50.0 <= data < 75.0",
								"children": [{"name": val, "parent": "50.0 <= data < 62.5"} for val in result[62.5]]
							},

							{
								"name": "62.5 <= data < 75.0",
								"parent": "50.0 <= data < 75.0",
								"children": [{"name": val, "parent": "62.5 <= data < 75.0"} for val in result[75.0]]
							}
						]
					},

					{
						"name": "75.0 <= data < 100.0",
						"parent": "50.0 <= data < 100.0",
						"children": [
							{
								"name": "75.0 <= data < 87.5",
								"parent": "75.0 <= data < 100.0",
								"children": [{"name": val, "parent": "75.0 <= data < 87.5"} for val in result[87.5]]
							},

							{
								"name": "87.5 <= data < 100.0",
								"parent": "75.0 <= data < 100.0",
								"children": [{"name": val, "parent": "87.5 <= data < 100.0"} for val in result[100.0]]
							}
						]
					}
				]
			},

			{
				"name": "data = 100.0",
				"parent": "Missing data",
				"children": [{"name": val, "parent": "data = 100.0"} for val in result["Max"]]
			}

		]
	}
]


with open("../data/tree_data.json", "w") as f:
	f.write(json.dumps(tree_data, indent = 4))