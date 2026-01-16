from abc import ABC, abstractmethod

class FoodPackage (ABC): 
  @abstractmethod
  def pack(self)  -> str:
    pass
  @abstractmethod
  def material(self) -> str:
    pass
  def describe(self):
    return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
  def pack(self) -> str:
    return "Wrapping"

  def material(self) -> str:
    return "Paper"

class Bottle(FoodPackage):  
  def pack(self) -> str:
    return "Bottle"
  
  def material(self) -> str:
    return "Plastic"
      
class Glass(FoodPackage):  
  def pack(self) -> str:
    return "Glass"
  
  def material(self) -> str:
    return "Cardboard"

class Box(FoodPackage):  
  def pack(self) -> str:
    return "Box"
  
  def material(self) -> str:
    return "Cardboard"