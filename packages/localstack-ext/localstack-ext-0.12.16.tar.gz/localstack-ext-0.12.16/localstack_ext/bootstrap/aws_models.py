from localstack.utils.aws import aws_models
KAcri=super
KAcrh=None
KAcre=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  KAcri(LambdaLayer,self).__init__(arn)
  self.cwd=KAcrh
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.KAcre.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,KAcre,env=KAcrh):
  KAcri(RDSDatabase,self).__init__(KAcre,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,KAcre,env=KAcrh):
  KAcri(RDSCluster,self).__init__(KAcre,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,KAcre,env=KAcrh):
  KAcri(AppSyncAPI,self).__init__(KAcre,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,KAcre,env=KAcrh):
  KAcri(AmplifyApp,self).__init__(KAcre,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,KAcre,env=KAcrh):
  KAcri(ElastiCacheCluster,self).__init__(KAcre,env=env)
class TransferServer(BaseComponent):
 def __init__(self,KAcre,env=KAcrh):
  KAcri(TransferServer,self).__init__(KAcre,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,KAcre,env=KAcrh):
  KAcri(CloudFrontDistribution,self).__init__(KAcre,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,KAcre,env=KAcrh):
  KAcri(CodeCommitRepository,self).__init__(KAcre,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
