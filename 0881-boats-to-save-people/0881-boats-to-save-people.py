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
                boats += 1
                a += 1
                b -= 1
            else:
                boats += 1
                b -= 1
            
        return boats 
        