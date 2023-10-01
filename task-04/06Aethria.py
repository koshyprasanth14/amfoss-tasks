n = int(input())
travel_time = list(map(int, input().split()))

min_time = min (travel_time)


if travel_time.count(min_time)>1:
    print('Still Aetheria')
else:
    town = travel_time.index(min_time)+1
    print( town)
    