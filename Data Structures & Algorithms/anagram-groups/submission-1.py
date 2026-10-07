class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # frequency_dict = defaultdict(list)
        # for s in strs:
        #     print(s)
        #     sorted_list = "".join(sorted(s))
        #     print(sorted_list)
        #     frequency_dict[sorted_list].append(s)
        # return list(frequency_dict.values())

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 
            for char in s:
                count[ord(char) - ord('a')] += 1

            res[tuple(count)].append(s)
        return list(res.values())
        
    
        
        
        