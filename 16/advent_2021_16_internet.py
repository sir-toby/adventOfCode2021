with open('2021_16.txt') as f:
    inp = f.read() 

bits = '' 
for x in inp: 
    bits += str(bin(int(x,16)))[2:].zfill(4)

def decode(packet, length=0): 
    packet_version = int(packet[:3],2) 
    packet_type = int(packet[3:6],2) 
    length += 6 
    packet_value = '' 
    if packet_type == 4: 
        remaining = packet[6:] 
        while True: 
            if remaining[0] == '0': 
                packet_value += remaining[1:5] 
                remaining = remaining[5:] 
                length += 5 
                break 
            packet_value += remaining[1:5] 
            remaining = remaining[5:] 
            length += 5
        packet_value = int(packet_value,2)
    else:
        type_id = packet[6]
        remaining = packet[7:]
        length += 1
        if type_id == '0':
            total_length = int(remaining[:15],2)
            remaining = remaining[15:]
            length += 15
            sub_packet_length=0
            values = []
            while sub_packet_length != total_length:
                remaining, sub_packet_length, value = decode(remaining, sub_packet_length)
                values.append(value)
            length += sub_packet_length
        elif type_id == '1':
            total_count = int(remaining[:11],2)
            remaining = remaining[11:]
            length += 11
            sub_packet_length = 0
            count=0
            values = []
            while count != total_count:
                remaining, sub_packet_length, value = decode(remaining, sub_packet_length)
                values.append(value)
                count += 1
            length += sub_packet_length
        
        if packet_type == 0:
            ans = sum(values)
        elif packet_type == 1:
            ans = 1
            for item in values:
                ans *= item
        elif packet_type == 2:
            ans = min(values)
        elif packet_type == 3:
            ans = max(values)
        elif packet_type == 5:
            ans = 1 if values[0]>values[1] else 0
        elif packet_type == 6:
            ans = 1 if values[0]<values[1] else 0
        elif packet_type == 7:
            ans = 1 if values[0]==values[1] else 0
            
        # print(packet_type, values, 'ans=', ans)  
        packet_value = ans
    
    return remaining, length, packet_value

print(decode(bits)[2])
