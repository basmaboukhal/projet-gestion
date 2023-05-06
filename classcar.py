class car:
  def __init__(self,idcar,Marque,Price,carburant,disponibility,nombredePlace,transmition ):
        self.__idcar=idcar;
        self.__Marque=Marque;
        self.__Price=Price;
        self.__carburant=carburant;
        self.__disponibility=disponibility;
        self.__nombredePlace=nombredePlace;
        self.__transmition=transmition;

  def getIdcar(self):
      return  self.__idcar 
  
  def getMarque(self):
    return self.__Marque
  
  def getPrice(self):
      return self.__Price
  
  def getCarburant(self):
      return self.__carburant;
  def getdiponibility(self):
      return self.__disponibility
  
  def getnombredePlace(self):
       return self.__nombredePlace;
  def gettransmision(self):
      return self.__transmition