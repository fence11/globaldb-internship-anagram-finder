## Design Decisions and Program Logic

### Reading Input:
- All non-empty lines are stripped of whitespace and added to a list of words.

### Grouping Logic:
- Each word is sorted alphabetically (e.g., 'listen' → 'eilnst').
- When a word is sorted, its sorted version becomes a key. All anagrams  will have the same sorted output, so they will be grouped under the same key.
- I used `defaultdict` to initialize all non-existent keys with an empty list, eliminating `KeyErrors` that arise using normal dictionaries
  
**Maintainability:**  
- The maintainability is handled decently well, as there are no hardcoded values, thanks to the use of `input_file_name` and `output_file_name`.

**Scalability:**  
- The dictionary can grow very large, especially if there are many unique key/word combinations.

**Performance:**  
- Writing a large number of lines can be very slow.

### Writing Output:
- Each group of anagrams is joined with spaces and written to a new line in the output file.
- Since the dictionary's values are lists of grouped anagrams, this results in a list of lists, where each inner list contains strings that are anagrams of each other.

## Scalability Considerations

Because the dictionary used for grouping anagrams can grow very large when processing millions of words, it's more efficient to handle the input file in groups. If the input file contains 10 million lines, the input can be divided into groups of 1 million lines. The input file may be processed this way for larger data sets:

- split the input file into multiple smaller groups
- process each group independently
- write the processed group to the output file
- clear the dictionary to free memory
- get the next group until all groups are finished

Each group could be processed in parallel to improve efficiency.

> [!NOTE]  
> In order to support large datasets, we would need a database instead of a simple `.txt` file and we could make use of frameworks that are made for this like Dask and Pandas.
