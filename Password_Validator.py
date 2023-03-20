def validate(username,password):
    if username =="ABC" and password =="Abc@123":
        print (" is a valid password")
    else:
        print(" is not a valid password")
validate("ABC", "Abc@123")
validate(password="Abc@123", username="ABC")
