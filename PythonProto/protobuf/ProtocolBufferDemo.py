from protobuf import Person_pb2

people = Person_pb2.People()
f = open("../../protobufBinary/People", "rb")
people.ParseFromString(f.read())

print(people)
