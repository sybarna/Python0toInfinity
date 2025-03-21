# hours minutes and seconds. ( converting seconds into these)

def calculating(seocnds):
    hours = seocnds // 3600
    minutes = (seocnds - hours * 3600) // 60

    remains = (seocnds - hours * 3600) - (minutes * 60)
    return hours, minutes, remains


alpha = calculating(234234)
hours, minutes, remains = alpha

hours, minutes, remains = calculating(34234)
print(alpha)
