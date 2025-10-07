# Serviços gRPC - stubs e services para comunicação remota)
import Proto.produto_pb2_grpc as pb2_grpc

import Proto.produto_pb2 as pb2

listaDeProdutos = []

class ProdutoService(pb2_grpc.ProdutoService):
    def AddProduto(self, request, context):
        id = len(listaDeProdutos) + 1
        listaDeProdutos.append({
            'id': id,
            'descricao': request.descricao,
            'valor': request.valor
        })
        return pb2.ProdutoResponse(**{'id': id, 'descricao' : request.descricao, 'valor': request.valor, 'msg': 'add ok'})