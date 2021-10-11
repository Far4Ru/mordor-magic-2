import csv
from mordor_app.serializers import EventSerializer
with open("events.csv", "rb") as source:
    rdr = csv.DictReader(source)
    for row in rdr:
        serializer = EventSerializer(**row)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
