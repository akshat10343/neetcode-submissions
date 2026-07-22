class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = list(zip(position, speed))
        paired = sorted(paired,reverse=True)

        stack = []
        for pos, spd in paired:
            time = (target - pos) / spd
            if len(stack) == 0 or stack[-1] < time:
                stack.append(time)
        return len(stack)