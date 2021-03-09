# you live 4 miles from university. the bus drives at 25mbh but spends 2 minutes each of the stops on the way.
#how long will the bus journey take? alternatively you could run to unversity.you jog the first mile at 7 mph again.
#then run the next two at 15 mph, before jogging the last at 7 mph
# will this be quicker or slower than the bus?
distance_from_university = 4
speed_of_bus = 25
time_to_reach_unversity = distance_from_university / speed_of_bus
time_in_minutes = time_to_reach_unversity *60
#for spending 2 min in each 10 stops
time_spend_in_each_stop= 2*10
time_after_time_spend = time_in_minutes - time_spend_in_each_stop
#for time by jogging
speed_by_jog_in_first_mile =7
speed_by_jog_in_second_and_third_mile=15
speed_by_jog_in_fourth_mile=7
time_to_reach_unversity_by_jogging_in_first_mile = (1/ speed_by_jog_in_first_mile * 60)
time_to_reach_unversity_by_jogging_in_second_and_third= (2/speed_by_jog_in_second_and_third_mile *60)
time_to_reach_unversity_by_jogging_in_fourth=(1/speed_by_jog_in_fourth_mile *60)
time_to_reach_unversity_by_jogging_in_minutes=time_to_reach_unversity_by_jogging_in_second_and_third+time_to_reach_unversity_by_jogging_in_fourth+time_to_reach_unversity_by_jogging_in_first_mile

if (time_to_reach_unversity_by_jogging_in_minutes > time_after_time_spend):
    print("he can reach by jogging faster")
else:
    print("he can reach by bus faster")