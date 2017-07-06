class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common = list(set(list1) & set(list2))
        dic = {r: list1.index(r) + list2.index(r) for r in common}
        min_sum = min(dic.values())

        ret = []
        for name in dic.keys():
            if dic[name] == min_sum:
                ret.append(name)
        return ret


def main():
    s = Solution()
    s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
                     ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])

if __name__ == '__main__':
    main()
