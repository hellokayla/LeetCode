# I came for candy, ended up with a cavity in my brain.
# 1. start graph traversal from initialBoxes
#   2. Is that box open?
#       3. If not open -> is there a key to open the box?
#          4. If no key -> You can never open
#   5. Is the box open?
#      6. totalCandies add value from box
# 7. Check boxes inside the box
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        q = []
        total_candies = 0
        opened_boxes = set()
        can_open = set()

        for initialBox in initialBoxes:
            q.append(initialBox)
            can_open.add(initialBox)

        # put initialBox into the queue
        while len(q) > 0:
            curr_box = q.pop(0)

            # 1. check if that box is already open or I have a key
            if curr_box not in opened_boxes and status[curr_box] == 1:
                total_candies += candies[curr_box]
                opened_boxes.add(curr_box)
                
                # 3. Check if keys inside the box unlock other boxes + change their status
                for key in keys[curr_box]:
                    status[key] = 1

                    if key in can_open and key not in opened_boxes:
                        q.append(key)

                # check neighbors in adjacency list
                for containedBox in containedBoxes[curr_box]:
                    can_open.add(containedBox)
                    q.append(containedBox)

        return total_candies