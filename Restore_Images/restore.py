# Bytes Bitwise Operation
def bitwise_and_bytes(a, b):
    result_int = int.from_bytes(a, byteorder="big") & int.from_bytes(b, byteorder="big")
    return result_int.to_bytes(max(len(a), len(b)), byteorder="big")

# Retuen True in case JPG signature else return False
def is_jpg(buffer_bytes):
     return (buffer_bytes[0:1] == b'\xff' and buffer_bytes[1:2] == b'\xd8' and buffer_bytes[2:3] == b'\xff' 
            and (bitwise_and_bytes(buffer_bytes[3:4], (b'\xf0')) == b'\xe0'))

# Open memory card raw file
#  Counting number of photos
#  Counting each photo buffers
with open('card.raw', 'rb') as file:
    image_counter = 0
    image = None

    # Initiate buffer to store card bytes
    buffer = file.read(512)
    while buffer:
        # Check JPG Signature
        jpg = is_jpg(buffer)
        if jpg:
            if image_counter > 0:
                image.close()
            image = open(f'{image_counter:03d}.JPG', 'wb')
            image.write(buffer)
            image_counter += 1

        # Writing bytes into image
        elif image_counter > 0:
            image.write(buffer)        

        buffer = file.read(512)
    image.close()
