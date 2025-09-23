import grpc
import Proto.user_pb2_grpc as pb2_grpc
import Proto.user_pb2 as pb2


def client():
   with grpc.insecure_channel('localhost:50051') as channel:
      #operações de cliente
      stubUser = pb2_grpc.UserServiceStub(channel)

      print('Dados de usuário')
      responseUser1 = stubUser.AddUser(pb2.UserRequest(id = 0, name='John', email = "ze@123"))
      responseUser2 = stubUser.AddUser(pb2.UserRequest(id = 0, name='ze', email = "ze@123"))

      responseUser3 = stubUser.GetUser(pb2.UserIdRequest(id = 9))

      responseUser4 = stubUser.UpdateUser(pb2.UserRequest(id = 2, name='angela', email = "angela@123"))

      responseUser5 = stubUser.GetUser(pb2.UserIdRequest(id = 2))

      responseUser6 = stubUser.DeleteUser(pb2.UserIdRequest(id = 1))

      print(f"{responseUser1.msg}: {responseUser1.id} -  {responseUser1.name} -  {responseUser1.email}")
      print(f"{responseUser2.msg}: {responseUser2.id} -  {responseUser2.name} -  {responseUser2.email}")
      print(f"{responseUser3.msg}: {responseUser3.id} -  {responseUser3.name} -  {responseUser3.email}")
      print(f"{responseUser4.msg}: {responseUser4.id} -  {responseUser4.name} -  {responseUser4.email}")
      print(f"{responseUser5.msg}: {responseUser5.id} -  {responseUser5.name} -  {responseUser5.email}")
      print(f"{responseUser6.msg}: {responseUser6.id} -  {responseUser6.name} -  {responseUser6.email}")  
      
if __name__ == '__main__':
    client()