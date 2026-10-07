class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleet = []
        n = len(speed)
        arrival_times = []
        cars = sorted(zip(position,speed), reverse = True)
        for pos,spee in cars:
            time = (target-pos)/spee
            stack.append(time)
        for time in stack:
            if not fleet:
                fleet.append(time)
            elif time <= fleet[-1]:
                continue
            else:
                fleet.append(time)
        return(len(fleet))


        

           
        
            



        