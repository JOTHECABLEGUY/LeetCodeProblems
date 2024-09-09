import pytest
def version_compare(version1:str, version2:str)-> int:
    """
    Compare 2 versions represented as strings.
    Args:
        version1 (str): The first string to use in comparison.
        version2 (str): The second string to use in comparison.

    Returns:
        int:    -1 if the second string represents the more recent version,
                0 if the versions are identical, and
                1 if the first string represents the more recent version.
    """
    # split the version strings using the '.' as a delimiter, cast to int
    version1_tokens, version2_tokens = list(map(int, version1.split("."))), list(map(int, version2.split('.')))
    # use the shortest token list to compare at tokens from both strings
    smallest_num_tokens = min(len(version1_tokens), len(version2_tokens))
    for i in range(smallest_num_tokens):
        
        # get the elements to compare from the token lists
        first_elem, sec_elem = version1_tokens[i], version2_tokens[i]
        
        # if any differences in the tokens, compare and return the appropriate result
        #   otherwise, continue to next tokens
        if first_elem < sec_elem:
            return -1
        if first_elem > sec_elem:
            return 1
    
    # once all tokens are used from one string, just need to check for any extra tokens that aren't 0
    ver1_extra = [e for e in version1_tokens[smallest_num_tokens:] if e != 0]
    ver2_extra = [e for e in version2_tokens[smallest_num_tokens:] if e != 0]
    
    # if any extra non-zero tokens were found, need to return the appropriate result,
    #   otherwise the versions are identical
    return 1 if ver1_extra else -1 if ver2_extra else 0
@pytest.mark.parametrize("version1, version2, expected", [
    ("2", "2.0", 0), #1
    ("2", "2.0.0", 0), #2
    ("2", "2.0.0.0", 0), #3
    ("2", "2.0.0.0.1", -1), #4
    ("2", "2.1", -1), #5
    ("2.1.0", "2.0.1", 1), #6
    ("2.10.0.1", "2.1.0.10", 1), #7
    ("2.0.1", "1.2000.1", 1), #8
], ids=[
    "test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8"
])
def test_all(version1, version2, expected):

    # Act
    result = version_compare(version1, version2)

    # Assert
    assert result == expected

    
if __name__ == "__main__":
    print(version_compare("2", "2.0.0.0.1"))
