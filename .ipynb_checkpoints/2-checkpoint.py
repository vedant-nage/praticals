#   Write a program to implement Huffman Encoding using a greedy strategy. 
# 23CO132
import heapq
from collections import Counter

def huffman_encoding(text):
    if not text:
        return {}

    frequency = Counter(text)
    heap = [[freq, char, None, None] for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = [left[0] + right[0], None, left, right]
        heapq.heappush(heap, merged)

    codes = {}

    def generate_codes(node, code=""):
        if node[1] is not None:
            codes[node[1]] = code or "0"
            return

        generate_codes(node[2], code + "0")
        generate_codes(node[3], code + "1")

    generate_codes(heap[0])
    return codes


text = input("Enter a string: ")

codes = huffman_encoding(text)

print("\nHuffman Codes:")
for char, code in sorted(codes.items()):
    print(f"{char}: {code}")

encoded = "".join(codes[char] for char in text)
print("\nEncoded string:", encoded)



# Enter a string: AABBC

# Huffman Codes:
# A: 0
# B: 11
# C: 10

# Encoded string: 00111110