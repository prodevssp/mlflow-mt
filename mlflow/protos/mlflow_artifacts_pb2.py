# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlflow_artifacts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
from . import databricks_pb2 as databricks__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16mlflow_artifacts.proto\x12\x10mlflow.artifacts\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"\x1e\n\x10\x44ownloadArtifact\x1a\n\n\x08Response\"\x1c\n\x0eUploadArtifact\x1a\n\n\x08Response\"T\n\rListArtifacts\x12\x0c\n\x04path\x18\x01 \x01(\t\x1a\x35\n\x08Response\x12)\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x1a.mlflow.artifacts.FileInfo\";\n\x08\x46ileInfo\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06is_dir\x18\x02 \x01(\x08\x12\x11\n\tfile_size\x18\x03 \x01(\x03\x32\xaf\x04\n\x16MlflowArtifactsService\x12\xbd\x01\n\x10\x64ownloadArtifact\x12\".mlflow.artifacts.DownloadArtifact\x1a+.mlflow.artifacts.DownloadArtifact.Response\"X\xf2\x86\x19T\n=\n\x03GET\x12\x30/mlflow-artifacts/artifacts/<path:artifact_path>\x1a\x04\x08\x02\x10\x00\x10\x01*\x11\x44ownload Artifact\x12\xb5\x01\n\x0euploadArtifact\x12 .mlflow.artifacts.UploadArtifact\x1a).mlflow.artifacts.UploadArtifact.Response\"V\xf2\x86\x19R\n=\n\x03PUT\x12\x30/mlflow-artifacts/artifacts/<path:artifact_path>\x1a\x04\x08\x02\x10\x00\x10\x01*\x0fUpload Artifact\x12\x9c\x01\n\rlistArtifacts\x12\x1f.mlflow.artifacts.ListArtifacts\x1a(.mlflow.artifacts.ListArtifacts.Response\"@\xf2\x86\x19<\n(\n\x03GET\x12\x1b/mlflow-artifacts/artifacts\x1a\x04\x08\x02\x10\x00\x10\x01*\x0eList ArtifactsB\x1e\n\x14org.mlflow.api.proto\x90\x01\x01\xe2?\x02\x10\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mlflow_artifacts_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.mlflow.api.proto\220\001\001\342?\002\020\001'
  _MLFLOWARTIFACTSSERVICE.methods_by_name['downloadArtifact']._options = None
  _MLFLOWARTIFACTSSERVICE.methods_by_name['downloadArtifact']._serialized_options = b'\362\206\031T\n=\n\003GET\0220/mlflow-artifacts/artifacts/<path:artifact_path>\032\004\010\002\020\000\020\001*\021Download Artifact'
  _MLFLOWARTIFACTSSERVICE.methods_by_name['uploadArtifact']._options = None
  _MLFLOWARTIFACTSSERVICE.methods_by_name['uploadArtifact']._serialized_options = b'\362\206\031R\n=\n\003PUT\0220/mlflow-artifacts/artifacts/<path:artifact_path>\032\004\010\002\020\000\020\001*\017Upload Artifact'
  _MLFLOWARTIFACTSSERVICE.methods_by_name['listArtifacts']._options = None
  _MLFLOWARTIFACTSSERVICE.methods_by_name['listArtifacts']._serialized_options = b'\362\206\031<\n(\n\003GET\022\033/mlflow-artifacts/artifacts\032\004\010\002\020\000\020\001*\016List Artifacts'
  _DOWNLOADARTIFACT._serialized_start=85
  _DOWNLOADARTIFACT._serialized_end=115
  _DOWNLOADARTIFACT_RESPONSE._serialized_start=105
  _DOWNLOADARTIFACT_RESPONSE._serialized_end=115
  _UPLOADARTIFACT._serialized_start=117
  _UPLOADARTIFACT._serialized_end=145
  _UPLOADARTIFACT_RESPONSE._serialized_start=105
  _UPLOADARTIFACT_RESPONSE._serialized_end=115
  _LISTARTIFACTS._serialized_start=147
  _LISTARTIFACTS._serialized_end=231
  _LISTARTIFACTS_RESPONSE._serialized_start=178
  _LISTARTIFACTS_RESPONSE._serialized_end=231
  _FILEINFO._serialized_start=233
  _FILEINFO._serialized_end=292
  _MLFLOWARTIFACTSSERVICE._serialized_start=295
  _MLFLOWARTIFACTSSERVICE._serialized_end=854
_builder.BuildServices(DESCRIPTOR, 'mlflow_artifacts_pb2', globals())
# @@protoc_insertion_point(module_scope)
