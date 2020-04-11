
def is_value_in_string( the_string: str, value: str):
    return value in the_string


def tenseChoser(str: str):
    result=""
    if(is_value_in_string(str,'IS') or is_value_in_string(str,'is') or is_value_in_string(str,'Are') or is_value_in_string(str,'ARE')):
        result="PRESENT TENSE"
    elif(is_value_in_string(str,'WAS') or is_value_in_string(str,'was') or is_value_in_string(str,'were') or is_value_in_string(str,'WERE')):
        result="PAST TENSE"
    elif(is_value_in_string(str,'WILL') or is_value_in_string(str,'will') or is_value_in_string(str,'shall') or is_value_in_string(str,'SHALL')):
        result="Future TENSE"
    return result


if __name__ == '__main__':
    print("Please enter a sentence")
    inputValue = input()
    outPutValue = tenseChoser(inputValue)
    if(outPutValue is None):
        pass
    else:
        print(outPutValue)