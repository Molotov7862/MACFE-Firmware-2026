def rpm_to_speed(rpm, wheel_radius_m, gear_ratio):
    wheel_rpm = rpm / gear_ratio
    circumference = 2 * 3.14159 * wheel_radius_m
    return wheel_rpm * circumference * 60 / 1000


if __name__ == "__main__":
    print(f"{rpm_to_speed(3000, 0.2286, 3.5):.1f} km/h")
