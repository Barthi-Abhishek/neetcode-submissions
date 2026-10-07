class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        cars = sorted(zip(position,speed), reverse = True)
        for pos,spee in cars:
            time = (target-pos)/spee
            if not fleet or time > fleet[-1]:
                fleet.append(time)
        return len(fleet)

           
        
            



        