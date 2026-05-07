import json, os

allowed_ch = "0123456789+-()*/^% ."

#main function
def safeCalculate(expr: str):
    conv_expr = expr.replace("^", "**")
    try: 
        for ch in conv_expr:
            if ch not in allowed_ch:
                return "Invalid Expression"
        # We use a dict for the result to safely handle the eval return
        return eval(conv_expr, {"__builtins__": None})
    except ZeroDivisionError:
        return "Math Error"
    except Exception:
        return "Invalid Expression"

def calculate(expression: str) -> int | float | str:
    
    return safeCalculate(expression)

#getting the weather data
def get_weather(city:str):
    fp="/home/competitor/data/weather_data.json"
    
    try:
        with open(fp, 'r') as f:
            data=json.load(f)
        
        for d in data:
            if(d.get('city').lower() == city.lower()):
                temp=d.get('temperature')
                cond=d.get('condition')
                
                if(temp is None or cond is None):
                    return "Weather Data not found"
                
                return f"{d['city']}: {temp} °C, {cond}"
        return "Weather Data not found"
    except (FileNotFoundError, json.JSONDecodeError):
        return "Weather Data not found"

#file reader
def read_file(filename:str):
    base_dir="/home/competitor/data/files/"
    abs_base_dir=os.path.abspath(base_dir)
    
    #requested directory
    req_dir=os.path.abspath(os.path.join(abs_base_dir, filename))
    
    if not req_dir.startswith(abs_base_dir):
        return "Restricted path"
    
    try:
        with open(req_dir, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)

print(read_file("tex.txt"))
