from collections import defaultdict

anagram_map = defaultdict(list)
input_file_name = "sample.txt"
output_file_name = "output.txt"

with open(input_file_name, "r") as input_file:
    for line in input_file:
        word = line.strip()
        if word:
            # add sorted word as key to dictionary
            key = "".join(sorted(word))
            anagram_map[key].append(word)

with open(output_file_name, "w") as output_file:
    for i, group in enumerate(anagram_map.values(), start=1):
        line = " ".join(group)
        output_file.write(line + "\n")
