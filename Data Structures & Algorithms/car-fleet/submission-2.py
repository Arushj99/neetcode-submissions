class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars.sort()
        for pos, speed in cars:
            time = (target - pos)/speed
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)
