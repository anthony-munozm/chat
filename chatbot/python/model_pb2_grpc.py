# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import model_pb2 as model__pb2


class NodeStub(object):
  """This is the single method that needs to be implemented by a gRPC client.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.MessageLoop = channel.stream_stream(
        '/pbx.Node/MessageLoop',
        request_serializer=model__pb2.ClientMsg.SerializeToString,
        response_deserializer=model__pb2.ServerMsg.FromString,
        )


class NodeServicer(object):
  """This is the single method that needs to be implemented by a gRPC client.
  """

  def MessageLoop(self, request_iterator, context):
    """Client sends a stream of ClientMsg, server responds with a stream of ServerMsg
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NodeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'MessageLoop': grpc.stream_stream_rpc_method_handler(
          servicer.MessageLoop,
          request_deserializer=model__pb2.ClientMsg.FromString,
          response_serializer=model__pb2.ServerMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pbx.Node', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class PluginStub(object):
  """Plugin interface.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FireHose = channel.unary_unary(
        '/pbx.Plugin/FireHose',
        request_serializer=model__pb2.ClientReq.SerializeToString,
        response_deserializer=model__pb2.ServerResp.FromString,
        )
    self.Find = channel.unary_unary(
        '/pbx.Plugin/Find',
        request_serializer=model__pb2.SearchQuery.SerializeToString,
        response_deserializer=model__pb2.SearchFound.FromString,
        )
    self.Account = channel.unary_unary(
        '/pbx.Plugin/Account',
        request_serializer=model__pb2.AccountEvent.SerializeToString,
        response_deserializer=model__pb2.Unused.FromString,
        )
    self.Topic = channel.unary_unary(
        '/pbx.Plugin/Topic',
        request_serializer=model__pb2.TopicEvent.SerializeToString,
        response_deserializer=model__pb2.Unused.FromString,
        )
    self.Subscription = channel.unary_unary(
        '/pbx.Plugin/Subscription',
        request_serializer=model__pb2.SubscriptionEvent.SerializeToString,
        response_deserializer=model__pb2.Unused.FromString,
        )
    self.Message = channel.unary_unary(
        '/pbx.Plugin/Message',
        request_serializer=model__pb2.MessageEvent.SerializeToString,
        response_deserializer=model__pb2.Unused.FromString,
        )


class PluginServicer(object):
  """Plugin interface.
  """

  def FireHose(self, request, context):
    """This plugin method is called by Tinode server for every message received from the clients. The
    method returns a ServerCtrl message. Non-zero ServerCtrl.code indicates that no further
    processing is needed. The Tinode server will generate a {ctrl} message from the returned ServerCtrl
    and forward it to the client session.
    ServerCtrl.code equals to 0 instructs the server to continue with default processing of the client message.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Find(self, request, context):
    """An alteranative user and topic discovery mechanism.
    A search request issued on a 'fnd' topic. This method is called to generate an alternative result set.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Account(self, request, context):
    """The following methods are for the Tinode server to report individual events.

    Account created, updated or deleted
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Topic(self, request, context):
    """Topic created, updated [or deleted -- not supported yet]
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Subscription(self, request, context):
    """Subscription created, updated or deleted
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Message(self, request, context):
    """Message published or deleted
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PluginServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FireHose': grpc.unary_unary_rpc_method_handler(
          servicer.FireHose,
          request_deserializer=model__pb2.ClientReq.FromString,
          response_serializer=model__pb2.ServerResp.SerializeToString,
      ),
      'Find': grpc.unary_unary_rpc_method_handler(
          servicer.Find,
          request_deserializer=model__pb2.SearchQuery.FromString,
          response_serializer=model__pb2.SearchFound.SerializeToString,
      ),
      'Account': grpc.unary_unary_rpc_method_handler(
          servicer.Account,
          request_deserializer=model__pb2.AccountEvent.FromString,
          response_serializer=model__pb2.Unused.SerializeToString,
      ),
      'Topic': grpc.unary_unary_rpc_method_handler(
          servicer.Topic,
          request_deserializer=model__pb2.TopicEvent.FromString,
          response_serializer=model__pb2.Unused.SerializeToString,
      ),
      'Subscription': grpc.unary_unary_rpc_method_handler(
          servicer.Subscription,
          request_deserializer=model__pb2.SubscriptionEvent.FromString,
          response_serializer=model__pb2.Unused.SerializeToString,
      ),
      'Message': grpc.unary_unary_rpc_method_handler(
          servicer.Message,
          request_deserializer=model__pb2.MessageEvent.FromString,
          response_serializer=model__pb2.Unused.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pbx.Plugin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
