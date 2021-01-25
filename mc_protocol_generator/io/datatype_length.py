boolean_size = 1
byte_size = 1
ubyte_size = 1
short_size = 2
ushort_size = 2
int_size = 4
long_size = 8
float_size = 4
double_size = 8
position_size = 8
angle_size = 1
uuid_size = 16

def string_size(string):
    encode_length = len(string.encode('utf8'))
    return varint_length(encode_length) + encode_length

def chat_size(chat):
    return string_length(chat)

def identifier_size(identifier):
    return string_length(identifier)

def varint_size(value):
    if value < -0x80000000:
        raise Exception(f'{value} is too small. Expected values between -2147483648 and 2147483647')
    elif value < 0x0:
        return 5
    elif value < 0x80:
        return 1
    elif value < 0x4000:
        return 2
    elif value < 0x200000:
        return 3
    elif value < 0x10000000:
        return 4
    elif value < 0x80000000:
        return 5
    raise Exception(f'{value} is too large. Expected values between -2147483648 and 2147483647')

def varlong_size(value):
    if value < -0x8000000000000000:
        raise Exception(f'{value} is too small. Expected values between -9223372036854775808 and 9223372036854775807')
    elif value < 0x0:
        return 10
    elif value < 0x80:
        return 1
    elif value < 0x4000:
        return 2
    elif value < 0x200000:
        return 3
    elif value < 0x10000000:
        return 4
    elif value < 0x800000000:
        return 5
    elif value < 0x40000000000:
        return 6
    elif value < 0x2000000000000:
        return 7
    elif value < 0x100000000000000:
        return 8
    elif value < 0x8000000000000000:
        return 9
    raise Exception(f'{value} is too large. Expected values between -9223372036854775808 and 9223372036854775807')

def entity_metadata_size(entity_metadata):
    raise NotImplementedError()

def slot_size(slot):
    raise NotImplementedError()

def nbt_size(nbt):
    raise NotImplementedError()

def byte_array_size(byte_array):
    return len(byte_array)
