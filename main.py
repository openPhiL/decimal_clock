from datetime import datetime

def convert_microseconds_to_microphillys(given_microseconds):
    microseconds_in_a_day = 86400 * 1000 * 1000
    phil, left_over_microseconds = divmod(given_microseconds, microseconds_in_a_day / 100 )
    phillys, left_over_microseconds = divmod( left_over_microseconds, microseconds_in_a_day / 100 / 100  )
    miniphillys, left_over_microseconds = divmod( left_over_microseconds, microseconds_in_a_day / 100 / 100 / 100  )
    milliphillys, left_over_microseconds = divmod( left_over_microseconds, microseconds_in_a_day / 100 / 100 / 100 / 100 )
    microphillys, left_over_microseconds = divmod( left_over_microseconds, microseconds_in_a_day / 100 / 100 / 100 / 100 / 100)
    return int(phil), int(phillys), int(miniphillys), int(milliphillys), int(microphillys)

while True: 
    now = datetime.now()  
    microseconds_now = (now.hour * 3600 + now.minute * 60 + now.second ) * 1000000 + now.microsecond
    philtime = convert_microseconds_to_microphillys(microseconds_now)
    print(f'{philtime[0]}:{philtime[1]}:{philtime[2]}:{philtime[3]}')
    
        
