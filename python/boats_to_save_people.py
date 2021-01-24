class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #keep track of the number of people for each weight
        num_people_per_weight = [0 for i in range(limit + 1)]
        for person in people:
            num_people_per_weight[person] += 1
        #light and heavy pointer will traverse the num_people_per_weight list from opossite directions, looking for matches
        light_pointer, heavy_pointer = 0, limit
        num_boats_with_two_people = 0
        while light_pointer < heavy_pointer and num_boats_with_two_people < len(people) / 2:
            #light_pointer will always point to the weight with the lightest remaining person
            while num_people_per_weight[light_pointer] == 0:
                light_pointer += 1
            #heavy_pointer will always point to the heaviest remaining person that can be paired with the weight that light_pointer points to
            while heavy_pointer > light_pointer and (limit - heavy_pointer < light_pointer or num_people_per_weight[heavy_pointer] == 0):
                heavy_pointer -= 1
            if heavy_pointer > light_pointer:
                num_boats_with_two_people += 1
                num_people_per_weight[light_pointer] -= 1
                num_people_per_weight[heavy_pointer] -= 1  
        #if the two pointers are pointing to the same weight and the weight is less than or equal to half the limit,
        #pair off the remaining people of that weight
        if light_pointer <= limit / 2:
            num_boats_with_two_people += num_people_per_weight[light_pointer] // 2
        return len(people) - num_boats_with_two_people