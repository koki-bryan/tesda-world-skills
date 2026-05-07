import json
arr1=["sean", "hello", "bryan"]
arr2=[0,1,2,3,4]
results=[]
for i in arr1:
    print(f"Model: {i}")
    for j, v in enumerate(arr2):
        print(f"[{j+1}/5] model answering:{i} | question:{v} ")
        record={
            "model": i,
            "prompt": v,
        }
        results.append(record)
        
print(results)

filePath="/home/competitor/project/testData.json"
with open(filePath, "w") as f:
    json.dump(results, f, indent=4)