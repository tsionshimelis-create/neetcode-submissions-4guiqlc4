class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(key = lambda x : x[0], reverse = True)

        # to say a car catches up to another car the time it takes it to reach the target point should be less than that of the time that takes the car infront of it to reach target

        fleet = []
        for car in cars:
            time = (target - car[0]) / car[1] 
            if not fleet or time > fleet[-1]:
                fleet.append(time)

        return len(fleet)