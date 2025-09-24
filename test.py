data =[
 {'role': 'user',
        'username': 'Sai',
        'content': 'Hello!',
        'timestamp': '2023-10-01 10:00:00'},
 {'role': 'assistant',
        'username': 'Assistant',
        'content': 'Hi there!',
        'timestamp': '2023-10-01 10:01:00'}
]

def all_roleslist():
    return list(set(msg['role'] for msg in data))

print(all_roleslist())