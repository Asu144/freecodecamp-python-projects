distance_mi = 5
is_raining = True
has_bike = False
has_car = False
has_ride_share_app = False

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    print(True if not is_raining else False)
elif distance_mi <= 6:
    print(True if has_bike and not is_raining else False)
else:
    print(True if has_car or has_ride_share_app else False)