def partitionString(s):

    def func(substr, curr_result, results):
        if len(substr) == 0:
            results.add(tuple(curr_result))
            return
        
        if len(substr) == 1:
            curr_result.append(substr)
            results.add(tuple(curr_result))
            return

        tmp_str = ""

        for idx, char in enumerate(substr):
            if char in tmp_str:
                break
            else:
                tmp_str += char

        curr_result.append(tmp_str)
        func(substr[idx:], curr_result, results)
        return
    
    results = set()
    func(s, [], results)
    return min([len(x) for x in results])

s= "cuieokbs"
partitionString(s)
