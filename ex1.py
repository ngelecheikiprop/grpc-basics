from person_pb2 import Person

person = Person()
person.name = "kiprop"
person.id = 31
person.hobbies.extend(["coding", "running"])

serialized_data = person.SerializeToString()
print("Serialized:", serialized_data)

new_person = Person()
new_person.ParseFromString(serialized_data)
print("deserialized", new_person)
