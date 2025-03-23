this is how I installed protocol buffer complier

```sh
sudo apt update
sudp apt install -y protobuf-compiler
```

I then had a look at the version

```sh
protoc --version
```
it was advisable to ensure I was at version 3

I then compiled my .proto file called person.proto which gave the file  person_pb2.py

```sh
protoc --python_out=. person.proto
```

To get started with python I made a virtual environment called grpc_vevn

```sh
python3 -m venv gprc_venv
. ./gprc_venv/bin/activate
```
I then installed the protobuf file
```sh
pip install protobuf
```

I then run my ex1.py file as follows
```sh
python3 ex1.py
```
and got the result
```sh
Serialized: b'\n\x06Kiprop\x10\x19\x1a\x06Coding\x1a\x07Running'
Deserialized: name: "Kiprop" age: 25 hobbies: "Coding" hobbies: "Running"
```



