# https://docs.python.org/3/library/codecs.html#standard-encodings

import binascii

def chars_to_bin(content):
  return [bin(x) for x  in content]

def bin_to_chars(bin_repr,encoding):
  int_repr = [int(bin(x),2) for x  in content]
  return bytes(int_repr).decode(encoding, "strict")


# Standard ASCII
# content = "ABCD".encode("us-ascii")
# print(content)
# print(chars_to_bin(content))
# print(bin_to_chars(chars_to_bin(content), "us-ascii"))


# print(bin_to_chars(chars_to_bin(content), "latin1"))
# print(bin_to_chars(chars_to_bin(content), "latin4"))


# # Extended ASCII
content = "ABCDà".encode("latin-1", 'strict')
print(chars_to_bin(content))
print(bin_to_chars(chars_to_bin(content), "latin1"))
print(bin_to_chars(chars_to_bin(content), "greek"))
# print(bin_to_chars(content, "latin4"))

# content = "ABCD".encode("us-ascii")
# print(content)
# binary_rep = [bin(x) for x  in content]
# print(chars_to_bin(content))
# print(bin_to_chars(chars_to_bin(content), "latin1"))
# print(bin_to_chars(chars_to_bin(content), "latin4"))