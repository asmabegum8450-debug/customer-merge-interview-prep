# Tech Interview Prep: Merging Customer Data

## Clarifying Questions
1. Are both arrays sorted in non-decreasing order?
2. Are duplicates allowed?
3. Are the trailing zeros in customerData1 placeholders?
4. Can m or n be zero?



## Approach
Use three pointers from the end:
- i = m-1 (last real element in customerData1)
- j = n-1 (last element in customerData2)
- k = m+n-1 (last slot in customerData1)

Fill from the back to avoid overwriting.

## Complexity
Time: O(m + n)  
Space: O(1)

## Running Tests
pip install pytest  
pytest -q
