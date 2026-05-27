import json, os


allowed_ch = "0123456789-+*/^"
def calculate(expr:str):
    
    for ch in expr:
        if ch not in allowed_ch:
            return "Invalid expression"

        try:
            return eval(expr, {'__builtins__' : None})
        except ZeroDivisionError:
            return "Cannot divide a number to 0"
        except Exception:
            return "Error"
        
def get_weather(city:str):
    fp = "/home/competitor/data/weather_data.json"
    
    with open(fp, 'r') as f:
        data = json.load(f)
        
    for d in data:
        if d.get("city").lower() == city.lower():
            return d
        return "not found"
  
def read_file(file:str):
    base_dir = "/home/competitor/data/files/"
    abs_path = os.path.abspath(base_dir)
    
    req_dir = os.path.abspath(os.path.join(base_dir, file))
    
    if not req_dir.startswith(abs_path):
        return "Restricted"
    
    try:
        with open(req_dir, 'r') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        return "file not found"
    except Exception as e:
        return f"Error {str(e)}"
    
