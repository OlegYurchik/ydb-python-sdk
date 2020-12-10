# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos import ydb_import_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__import__pb2


class ImportServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ImportFromS3 = channel.unary_unary(
        '/Ydb.Import.V1.ImportService/ImportFromS3',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__import__pb2.ImportFromS3Request.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__import__pb2.ImportFromS3Response.FromString,
        )
    self.ImportData = channel.unary_unary(
        '/Ydb.Import.V1.ImportService/ImportData',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__import__pb2.ImportDataRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__import__pb2.ImportDataResponse.FromString,
        )


class ImportServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ImportFromS3(self, request, context):
    """Imports data from S3.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImportData(self, request, context):
    """Writes data to a table.
    Method accepts serialized data in the selected format and writes it non-transactionally.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ImportServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ImportFromS3': grpc.unary_unary_rpc_method_handler(
          servicer.ImportFromS3,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__import__pb2.ImportFromS3Request.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__import__pb2.ImportFromS3Response.SerializeToString,
      ),
      'ImportData': grpc.unary_unary_rpc_method_handler(
          servicer.ImportData,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__import__pb2.ImportDataRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__import__pb2.ImportDataResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Ydb.Import.V1.ImportService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
