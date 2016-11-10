import pydivert

print "Start!"
with pydivert.WinDivert("tcp.PayloadLength > 0") as wd:
    for packet in wd:
        if packet.is_outbound:
            data=packet.tcp.payload
            data=data.replace(b'Accept-Encoding: gzip',b'Accept-Encoding:   ')
            packet.tcp.payload = data
        if packet.is_inbound:
            data=packet.tcp.payload
            data=data.replace(b'Michael',b'Gilbert')
            packet.tcp.payload = data
        wd.send(packet, recalculate_checksum=True)
print "Finish!"
