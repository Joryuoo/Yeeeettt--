class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()

        a, b = 0, len(people) - 1
        boats = 0
        while a <= b:
            res = people[a] + people[b]

            if res <= limit:
                a += 1
                b -= 1
            else:
                b -= 1 #the heaviest goes alone dead ass
            
            boats += 1

        return boats
        