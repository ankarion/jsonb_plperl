str = "select test{0}({1}){2};"

versions = {
		"old":2,
		"new":1
		}

jsons = {
		"old":"\"0\":0",
		"new":"\"0\":0"
		}

step = 1000

for i in range(1,30*step,step):
	for version in versions.keys():
		print("tests/file"+repr(i)+"_"+version+".sql")
		with open("tests/file"+repr(i)+"_"+version+".sql","w") as f:
			f.write(
				str.format(
					versions[version],
					"\'{"+jsons[version]+("}\'::jsonb"if version=="new" else "}\'"),
					'::jsonb' if version=="old" else ""
					)
				)
		for j in range(step):
			jsons[version] += ",\""+repr(i+j)+"\":"+repr(i+j)
