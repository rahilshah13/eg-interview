import math
import matplotlib.pyplot as plt

# The class CarSimulator is a simple 2D vehicle simulator.
# The vehicle states are:
# - x,y: is the position on the xy plane
# - v is the vehicle speed in the direction of travel
# - theta: 0 rad means the vehicle is parallel to the x axis, in the (+)direction;
#   pi/2 rad = vehicle is parallel to the y axis in the (+)direction
# - UNITS: meters (m) for distances, seconds (s) for time, radians (rad) for angles...

# (1)
# Write the method "simulatorStep", which should update
# the vehicle states, given 3 inputs:
#  - a: commanded vehicle acceleration
#  - wheel_angle: steering angle, measured at the wheels;
#    0 rad means that the wheels are "straight" wrt the vehicle.
#    A positive value means that the vehicle is turning counterclockwise
#  - dt: duration of time after which we want to provide
#    a state update (time step)
#
# (2)
# Complete the function "main". This function should run the following simulation:
# - The vehicle starts at 0 m/s
# - The vehicle drives on a straight line and accelerates from 0 m/s to 10 m/s
#   at a constant rate of 0.4 m/s^2, then it proceeds at constant speed.
# - Once reached the speed of 10 m/s, the vehicle drives in a clockwise circle of
#   roughly 100 m radius
# - the simulation ends at 100 s
#
# (3)
# - plot the vehicle's trajectory on the xy plane
# - plot the longitudinal and lateral accelerations over time


class CarSimulator():
    def __init__(self, wheelbase, v0, theta0):
        # INPUTS:
        # the wheel base is the distance between the front and the rear wheels
        self.wheelbase = wheelbase
        self.x = 0
        self.y = 0
        self.v = v0
        self.theta = theta0

    def simulatorStep(self, a, wheel_angle, dt):
        # Update velocity using acceleration
        self.v += a * dt
        
        # Calculate turning radius based on wheel angle and wheelbase
        # R = wheelbase / tan(wheel_angle) for bicycle model
        if abs(wheel_angle) > 1e-6:  # Avoid division by zero
            turning_radius = self.wheelbase / math.tan(wheel_angle)
            # Angular velocity = v/r
            omega = self.v / turning_radius
        else:
            omega = 0
        
        # Update heading angle
        self.theta += omega * dt
        
        # Update position based on velocity and heading
        self.x += self.v * math.cos(self.theta) * dt
        self.y += self.v * math.sin(self.theta) * dt


def main():
    wheelbase = 4  # arbitrary 4m wheelbase
    v0 = 0
    theta0 = 0
    simulator = CarSimulator(wheelbase, v0, theta0)
    dt = 0.1  # arbitrarily set the time step to 0.1 s
    
    # Initialize lists to store data for plotting
    t_points = []
    x_points = []
    y_points = []
    a_long = []  # longitudinal acceleration
    a_lat = []   # lateral acceleration
    
    # Simulation time
    t = 0
    t_end = 100  # 100 seconds
    
    while t <= t_end:
        # Store current state
        t_points.append(t)
        x_points.append(simulator.x)
        y_points.append(simulator.y)
        
        # Calculate required wheel angle for 100m radius circle when v = 10 m/s
        # arctan(wheelbase/radius) gives required wheel angle
        target_radius = 100
        target_wheel_angle = math.atan(wheelbase/target_radius)
        
        # Control logic
        if simulator.v < 10:
            # Accelerate to 10 m/s
            a = 0.4
            wheel_angle = 0
        else:
            # Maintain speed and turn in circle
            a = 0
            wheel_angle = -target_wheel_angle  # negative for clockwise turn
        
        # Calculate accelerations for plotting
        a_long.append(a)
        if abs(wheel_angle) > 1e-6:
            a_lat.append(simulator.v**2 / target_radius)
        else:
            a_lat.append(0)
        
        # Update simulation
        simulator.simulatorStep(a, wheel_angle, dt)
        t += dt
    
    # Create plots
    plt.figure(figsize=(12, 5))
    
    # Trajectory plot
    plt.subplot(121)
    plt.plot(x_points, y_points)
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.title('Vehicle Trajectory')
    plt.axis('equal')
    
    # Acceleration plot
    plt.subplot(122)
    plt.plot(t_points, a_long, label='Longitudinal')
    plt.plot(t_points, a_lat, label='Lateral')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s²)')
    plt.title('Vehicle Accelerations')
    plt.legend()
    
    plt.tight_layout()
    plt.show()


main()