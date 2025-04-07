# # FastAPI se import kar rahe hain, taaki hum API bana sakein
# from fastapi import FastAPI
# from pydantic import BaseModel

# # FastAPI ka ek instance bana rahe hain
# app = FastAPI()



# names = ["kiran", "muskan", "kanwal", "mehak"]







# # Yeh ek GET request ka endpoint define kar raha hai jo root ("/") pe chalega
# @app.get("/")

#  # Ek function define kiya jo execute hoga jab yeh endpoint hit hoga
# def get_function():
#      # Yeh function ek JSON response return karega
#     #  return {"message": "Hello, FastAPI!"}
#     return names
 
 
# class Data(BaseModel):
#      name: str
#     #  age: int
     
# @app.post("/data")
# def post_function(data: Data):
#     # return{
#     #     "name": f"My name is {data.name}",
#     #      "age": f"my age is {data.age}"
#     #      }
    
#     names.append(data.name)
#     return names
     
# # @app.delete("/{item_id}")
# # def delete_data(item_id:int):
#     # Yeh endpoint jo data.name parameter pe chalega
#     # Delete operation karenge data.name se koi match karega
#     # return {"message": f"Item with id Deleted {item_id} successfully"}
 
# @app.delete("/{name}")
# def delete_data(name:str):
#     names.remove(name)
#     return names

# # @app.put("/{item_id}")
# # def update_data(item_id, data:Data):
#     # Yeh endpoint jo data.name parameter pe chalega
#     # Update operation karenge data.name se koi match karega
#     # return {"message": f"Item with id {item_id} updated with name: {data.name}, age: {data.age} successfully"}
    
    
# @app.put("/{name}")
# def update_data(name, data:Data):
#     for i, n in enumerate(names):
#         if n == name:
#          names[i] = data.name
#     return names


# FastAPI import
from fastapi import FastAPI
from pydantic import BaseModel

# App create
app = FastAPI()

# Dummy data
names = ["kiran", "muskan", "kanwal", "mehak"]

# GET endpoint
@app.get("/")
def get_function():
    return names

# POST endpoint
class Data(BaseModel):
    name: str

@app.post("/data")
def post_function(data: Data):
    names.append(data.name)
    return names

# DELETE endpoint
@app.delete("/{name}")
def delete_data(name: str):
    names.remove(name)
    return names

# PUT endpoint
@app.put("/{name}")
def update_data(name: str, data: Data):
    for i, n in enumerate(names):
        if n == name:
            names[i] = data.name
    return names
