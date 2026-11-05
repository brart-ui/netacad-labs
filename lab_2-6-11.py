hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total = hour * 60 + mins + dura

end_hour = (total // 60) % 24
end_mins = total % 60
