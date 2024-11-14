"""
Problem #14 [Medium]
This problem was asked by Google.
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random

class DCP14:
    def estimate_pi_monte_carlo(self, radius:int = 1, iterations:int = 100000) -> float:
        inside_count, total_count = 0, 0

        for _ in range(iterations):
            rand_float_x = random.uniform(0, radius)
            rand_float_y = random.uniform(0, radius)

            rad_dist_computed = (rand_float_x**2 + rand_float_y**2)**0.5

            if rad_dist_computed <= radius:
                inside_count += 1
                total_count += 1
            else:
                total_count += 1

        pi_estimate = 4*inside_count/total_count
        # print("pi_estimate: ", pi_estimate)
        return pi_estimate
    
    def test(self):
        result = self.estimate_pi_monte_carlo(1)
        print("result: ", result)

if __name__ == "__main__":
    dcp = DCP14()
    dcp.test()