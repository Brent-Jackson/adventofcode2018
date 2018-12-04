import re

def solve(lines):
    guard = 0
    asleep = False

    # sort events
    events = {}
    for line in lines:
        nums = re.findall(r'\d+',line)
        date = int("".join(n for n in nums[0:5])) #concat the strings and parse to int to sort by date
        events[date] = line

    dates = list(events.keys())
    dates.sort()
    # for d in dates:
    #     print(d,events[d])

    sleep_durations = {}
    sleep_log_by_minute = {}
    asleep_since = 0

    for d in dates:
        event = events[d]
        # print(event.strip())
        nums = re.findall(r'\d+',event)
        fell_asleep = True if re.findall(r'asleep',event.strip()) != [] else False
        minute = int(nums[4])

        if len(nums) > 5:   # new guard
            guard = int(nums[5])
        elif fell_asleep:
            asleep_since = minute
            # print("{} fell asleep at {}".format(guard,asleep_since))
        else:
            slept = minute - asleep_since
            # print("{} slept from {} to {}: {} minutes".format(guard,asleep_since,minute,slept))
            if guard not in sleep_durations:
                sleep_durations[guard] = 0
                sleep_log_by_minute[guard] = [0] * 60
            sleep_durations[guard] += slept
            for m in range(slept):
                sleep_log_by_minute[guard][asleep_since+m] += 1
            # print("{}'s sleep logs: \n{}".format(guard," ".join(str(i) for i in sleep_log_by_minute[guard])))
            # print("{} has now slept a total of {}".format(guard,sleep_durations[guard]))


        # print("{:40}\tguard {} is {} at {}".format(event.strip(),guard,"asleep" if fell_asleep else "awake ",minute))
        


    biggest_sleeper = max(sleep_durations,key=sleep_durations.get)
    most_slept_minute = sleep_log_by_minute[biggest_sleeper].index(max(sleep_log_by_minute[biggest_sleeper]))
    print("Biggest snoozer: {} ({} minutes total)".format(biggest_sleeper,sleep_durations[biggest_sleeper]))
    print(" ".join(str(i) for i in sleep_log_by_minute[biggest_sleeper]))
    print("Most slept minute:",most_slept_minute)
    q1 = most_slept_minute * biggest_sleeper

    max_given_minute_asleep_guard = max(sleep_log_by_minute,key=lambda x: max(sleep_log_by_minute[x]))
    most_sleepy_minute = sleep_log_by_minute[max_given_minute_asleep_guard].index(max(sleep_log_by_minute[max_given_minute_asleep_guard]))
    print("\nMost consistent sleeper: {} (on minute {})".format(max_given_minute_asleep_guard,most_sleepy_minute))
    print(" ".join(str(i) for i in sleep_log_by_minute[max_given_minute_asleep_guard]))
    q2 = max_given_minute_asleep_guard * most_sleepy_minute


    return q1, q2



with open("input.txt") as f:
    lines = f.readlines()

q1, q2 = solve(lines)
print("q1: {}\nq2: {}".format(q1, q2))