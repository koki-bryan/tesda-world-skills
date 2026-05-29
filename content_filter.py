import datetime
import json

result_fp='/home/competitor/project/filterlog.json'
result_logs=[]

filtered = []

prompt_redaction = ['ignore all previous', 'ignore all', 'ignore', 'tell', 'system prompt']
harmful_redaction = ['gun', 'knife', 'hate', 'fuck', 'kill', 'bomb', 'assault', 'die', 'hack', 'hacking', 'killing', 'murder', 'murdering']

email_redaction = ('.com', '.edu', '.net', '.org', '.gov', '.ph')
def filter(text:str):
    
    arr = text.split(' ')
    for i in arr:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if i.startswith('09') or i.startswith('+63') and len(i) <= 15:
            filtered.append('[PHONE REDACTED]')
        
        elif i.endswith('.com') or i.endswith('.net') or i.endswith('.edu'):
            filtered.append('[EMAIL REDACTED]')
        elif i in harmful_redaction:
            result_logs.append({'blocked': True, 'category': 'harmful content', 'message' : text, 'timestamp': time})
            return {'blocked': True, 'category': 'harmful content', 'message' : text, 'timestamp': time}
        elif i in prompt_redaction:
            result_logs.append({'blocked': True, 'category': 'prompt injection', 'message': text, 'timestamp': time})
            return {'blocked': True, 'category': 'prompt injection', 'message': text, 'timestamp': time}
        else:
            filtered.append(i)
            
    sanitized_input = ' '.join(filtered)
    result_logs.append({'blocked': False, 'sanitized_input' : sanitized_input, 'timestamp': time})
    return {'blocked': False, 'sanitized_input' : sanitized_input, 'timestamp': time}
        
with open(result_fp, 'a') as f:
    json.dump(result_logs, f, indent=4)

print(result_logs)
print(filter('my email is seanbryan.noces@gmail.com my number is 09453412'))