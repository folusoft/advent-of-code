
line =  open('day6.txt', 'r').read().strip()
packet = []
packet_length = 4
message_length = 14
for index in range(len(input)):
    char = input[index]
    #check for repeat
    if char in packet:
        bad_index = packet.index(char)
        while bad_index >= 0:
            packet.pop(bad_index)
            bad_index = bad_index - 1
    packet.append(char)
    #first check do we have the right length of packets?
    if len(packet) == message_length:
        print("result ", index + 1)
        break
    