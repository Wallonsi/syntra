minutes = 42
seconds = 42

total_seconds = minutes * 60 + seconds
print(f"total seconds: {total_seconds}")

kilometer = 1
mile = kilometer / 1.61

miles_in_kilometers = (kilometer * 10) * mile
print(f"miles in kilometers: {miles_in_kilometers}")

ave_pace_seconds = (total_seconds / 10) / mile
print(f"average pace per seconds: {ave_pace_seconds}")

pace_minutes = ave_pace_seconds // 60
pace_seconds = ave_pace_seconds % 60
print(f"pace minutes: {pace_minutes} and seconds: {pace_seconds}")

hour = total_seconds / 3600
mph = miles_in_kilometers / hour
print(f"mph: {mph}")