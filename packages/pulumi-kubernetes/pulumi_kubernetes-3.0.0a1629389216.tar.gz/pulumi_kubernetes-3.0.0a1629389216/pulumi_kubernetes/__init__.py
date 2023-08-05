# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .kustomize import *
from .provider import *
from .yaml import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_kubernetes.admissionregistration as admissionregistration
    import pulumi_kubernetes.apiextensions as apiextensions
    import pulumi_kubernetes.apiregistration as apiregistration
    import pulumi_kubernetes.apps as apps
    import pulumi_kubernetes.auditregistration as auditregistration
    import pulumi_kubernetes.authentication as authentication
    import pulumi_kubernetes.authorization as authorization
    import pulumi_kubernetes.autoscaling as autoscaling
    import pulumi_kubernetes.batch as batch
    import pulumi_kubernetes.certificates as certificates
    import pulumi_kubernetes.coordination as coordination
    import pulumi_kubernetes.core as core
    import pulumi_kubernetes.discovery as discovery
    import pulumi_kubernetes.events as events
    import pulumi_kubernetes.extensions as extensions
    import pulumi_kubernetes.flowcontrol as flowcontrol
    import pulumi_kubernetes.helm as helm
    import pulumi_kubernetes.meta as meta
    import pulumi_kubernetes.networking as networking
    import pulumi_kubernetes.node as node
    import pulumi_kubernetes.policy as policy
    import pulumi_kubernetes.rbac as rbac
    import pulumi_kubernetes.scheduling as scheduling
    import pulumi_kubernetes.settings as settings
    import pulumi_kubernetes.storage as storage
else:
    admissionregistration = _utilities.lazy_import('pulumi_kubernetes.admissionregistration')
    apiextensions = _utilities.lazy_import('pulumi_kubernetes.apiextensions')
    apiregistration = _utilities.lazy_import('pulumi_kubernetes.apiregistration')
    apps = _utilities.lazy_import('pulumi_kubernetes.apps')
    auditregistration = _utilities.lazy_import('pulumi_kubernetes.auditregistration')
    authentication = _utilities.lazy_import('pulumi_kubernetes.authentication')
    authorization = _utilities.lazy_import('pulumi_kubernetes.authorization')
    autoscaling = _utilities.lazy_import('pulumi_kubernetes.autoscaling')
    batch = _utilities.lazy_import('pulumi_kubernetes.batch')
    certificates = _utilities.lazy_import('pulumi_kubernetes.certificates')
    coordination = _utilities.lazy_import('pulumi_kubernetes.coordination')
    core = _utilities.lazy_import('pulumi_kubernetes.core')
    discovery = _utilities.lazy_import('pulumi_kubernetes.discovery')
    events = _utilities.lazy_import('pulumi_kubernetes.events')
    extensions = _utilities.lazy_import('pulumi_kubernetes.extensions')
    flowcontrol = _utilities.lazy_import('pulumi_kubernetes.flowcontrol')
    helm = _utilities.lazy_import('pulumi_kubernetes.helm')
    meta = _utilities.lazy_import('pulumi_kubernetes.meta')
    networking = _utilities.lazy_import('pulumi_kubernetes.networking')
    node = _utilities.lazy_import('pulumi_kubernetes.node')
    policy = _utilities.lazy_import('pulumi_kubernetes.policy')
    rbac = _utilities.lazy_import('pulumi_kubernetes.rbac')
    scheduling = _utilities.lazy_import('pulumi_kubernetes.scheduling')
    settings = _utilities.lazy_import('pulumi_kubernetes.settings')
    storage = _utilities.lazy_import('pulumi_kubernetes.storage')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "kubernetes",
  "mod": "admissionregistration.k8s.io/v1",
  "fqn": "pulumi_kubernetes.admissionregistration.v1",
  "classes": {
   "kubernetes:admissionregistration.k8s.io/v1:MutatingWebhookConfiguration": "MutatingWebhookConfiguration",
   "kubernetes:admissionregistration.k8s.io/v1:MutatingWebhookConfigurationList": "MutatingWebhookConfigurationList",
   "kubernetes:admissionregistration.k8s.io/v1:ValidatingWebhookConfiguration": "ValidatingWebhookConfiguration",
   "kubernetes:admissionregistration.k8s.io/v1:ValidatingWebhookConfigurationList": "ValidatingWebhookConfigurationList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "admissionregistration.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.admissionregistration.v1beta1",
  "classes": {
   "kubernetes:admissionregistration.k8s.io/v1beta1:MutatingWebhookConfiguration": "MutatingWebhookConfiguration",
   "kubernetes:admissionregistration.k8s.io/v1beta1:MutatingWebhookConfigurationList": "MutatingWebhookConfigurationList",
   "kubernetes:admissionregistration.k8s.io/v1beta1:ValidatingWebhookConfiguration": "ValidatingWebhookConfiguration",
   "kubernetes:admissionregistration.k8s.io/v1beta1:ValidatingWebhookConfigurationList": "ValidatingWebhookConfigurationList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apiextensions.k8s.io/v1",
  "fqn": "pulumi_kubernetes.apiextensions.v1",
  "classes": {
   "kubernetes:apiextensions.k8s.io/v1:CustomResourceDefinition": "CustomResourceDefinition",
   "kubernetes:apiextensions.k8s.io/v1:CustomResourceDefinitionList": "CustomResourceDefinitionList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apiextensions.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.apiextensions.v1beta1",
  "classes": {
   "kubernetes:apiextensions.k8s.io/v1beta1:CustomResourceDefinition": "CustomResourceDefinition",
   "kubernetes:apiextensions.k8s.io/v1beta1:CustomResourceDefinitionList": "CustomResourceDefinitionList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apiregistration.k8s.io/v1",
  "fqn": "pulumi_kubernetes.apiregistration.v1",
  "classes": {
   "kubernetes:apiregistration.k8s.io/v1:APIService": "APIService",
   "kubernetes:apiregistration.k8s.io/v1:APIServiceList": "APIServiceList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apiregistration.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.apiregistration.v1beta1",
  "classes": {
   "kubernetes:apiregistration.k8s.io/v1beta1:APIService": "APIService",
   "kubernetes:apiregistration.k8s.io/v1beta1:APIServiceList": "APIServiceList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apps/v1",
  "fqn": "pulumi_kubernetes.apps.v1",
  "classes": {
   "kubernetes:apps/v1:ControllerRevision": "ControllerRevision",
   "kubernetes:apps/v1:ControllerRevisionList": "ControllerRevisionList",
   "kubernetes:apps/v1:DaemonSet": "DaemonSet",
   "kubernetes:apps/v1:DaemonSetList": "DaemonSetList",
   "kubernetes:apps/v1:Deployment": "Deployment",
   "kubernetes:apps/v1:DeploymentList": "DeploymentList",
   "kubernetes:apps/v1:ReplicaSet": "ReplicaSet",
   "kubernetes:apps/v1:ReplicaSetList": "ReplicaSetList",
   "kubernetes:apps/v1:StatefulSet": "StatefulSet",
   "kubernetes:apps/v1:StatefulSetList": "StatefulSetList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apps/v1beta1",
  "fqn": "pulumi_kubernetes.apps.v1beta1",
  "classes": {
   "kubernetes:apps/v1beta1:ControllerRevision": "ControllerRevision",
   "kubernetes:apps/v1beta1:ControllerRevisionList": "ControllerRevisionList",
   "kubernetes:apps/v1beta1:Deployment": "Deployment",
   "kubernetes:apps/v1beta1:DeploymentList": "DeploymentList",
   "kubernetes:apps/v1beta1:StatefulSet": "StatefulSet",
   "kubernetes:apps/v1beta1:StatefulSetList": "StatefulSetList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apps/v1beta2",
  "fqn": "pulumi_kubernetes.apps.v1beta2",
  "classes": {
   "kubernetes:apps/v1beta2:ControllerRevision": "ControllerRevision",
   "kubernetes:apps/v1beta2:ControllerRevisionList": "ControllerRevisionList",
   "kubernetes:apps/v1beta2:DaemonSet": "DaemonSet",
   "kubernetes:apps/v1beta2:DaemonSetList": "DaemonSetList",
   "kubernetes:apps/v1beta2:Deployment": "Deployment",
   "kubernetes:apps/v1beta2:DeploymentList": "DeploymentList",
   "kubernetes:apps/v1beta2:ReplicaSet": "ReplicaSet",
   "kubernetes:apps/v1beta2:ReplicaSetList": "ReplicaSetList",
   "kubernetes:apps/v1beta2:StatefulSet": "StatefulSet",
   "kubernetes:apps/v1beta2:StatefulSetList": "StatefulSetList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "auditregistration.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.auditregistration.v1alpha1",
  "classes": {
   "kubernetes:auditregistration.k8s.io/v1alpha1:AuditSink": "AuditSink",
   "kubernetes:auditregistration.k8s.io/v1alpha1:AuditSinkList": "AuditSinkList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "authentication.k8s.io/v1",
  "fqn": "pulumi_kubernetes.authentication.v1",
  "classes": {
   "kubernetes:authentication.k8s.io/v1:TokenRequest": "TokenRequest",
   "kubernetes:authentication.k8s.io/v1:TokenReview": "TokenReview"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "authentication.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.authentication.v1beta1",
  "classes": {
   "kubernetes:authentication.k8s.io/v1beta1:TokenReview": "TokenReview"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "authorization.k8s.io/v1",
  "fqn": "pulumi_kubernetes.authorization.v1",
  "classes": {
   "kubernetes:authorization.k8s.io/v1:LocalSubjectAccessReview": "LocalSubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1:SelfSubjectAccessReview": "SelfSubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1:SelfSubjectRulesReview": "SelfSubjectRulesReview",
   "kubernetes:authorization.k8s.io/v1:SubjectAccessReview": "SubjectAccessReview"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "authorization.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.authorization.v1beta1",
  "classes": {
   "kubernetes:authorization.k8s.io/v1beta1:LocalSubjectAccessReview": "LocalSubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1beta1:SelfSubjectAccessReview": "SelfSubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1beta1:SelfSubjectRulesReview": "SelfSubjectRulesReview",
   "kubernetes:authorization.k8s.io/v1beta1:SubjectAccessReview": "SubjectAccessReview"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "autoscaling/v1",
  "fqn": "pulumi_kubernetes.autoscaling.v1",
  "classes": {
   "kubernetes:autoscaling/v1:HorizontalPodAutoscaler": "HorizontalPodAutoscaler",
   "kubernetes:autoscaling/v1:HorizontalPodAutoscalerList": "HorizontalPodAutoscalerList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "autoscaling/v2beta1",
  "fqn": "pulumi_kubernetes.autoscaling.v2beta1",
  "classes": {
   "kubernetes:autoscaling/v2beta1:HorizontalPodAutoscaler": "HorizontalPodAutoscaler",
   "kubernetes:autoscaling/v2beta1:HorizontalPodAutoscalerList": "HorizontalPodAutoscalerList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "autoscaling/v2beta2",
  "fqn": "pulumi_kubernetes.autoscaling.v2beta2",
  "classes": {
   "kubernetes:autoscaling/v2beta2:HorizontalPodAutoscaler": "HorizontalPodAutoscaler",
   "kubernetes:autoscaling/v2beta2:HorizontalPodAutoscalerList": "HorizontalPodAutoscalerList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "batch/v1",
  "fqn": "pulumi_kubernetes.batch.v1",
  "classes": {
   "kubernetes:batch/v1:CronJob": "CronJob",
   "kubernetes:batch/v1:CronJobList": "CronJobList",
   "kubernetes:batch/v1:Job": "Job",
   "kubernetes:batch/v1:JobList": "JobList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "batch/v1beta1",
  "fqn": "pulumi_kubernetes.batch.v1beta1",
  "classes": {
   "kubernetes:batch/v1beta1:CronJob": "CronJob",
   "kubernetes:batch/v1beta1:CronJobList": "CronJobList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "batch/v2alpha1",
  "fqn": "pulumi_kubernetes.batch.v2alpha1",
  "classes": {
   "kubernetes:batch/v2alpha1:CronJob": "CronJob",
   "kubernetes:batch/v2alpha1:CronJobList": "CronJobList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "certificates.k8s.io/v1",
  "fqn": "pulumi_kubernetes.certificates.v1",
  "classes": {
   "kubernetes:certificates.k8s.io/v1:CertificateSigningRequest": "CertificateSigningRequest",
   "kubernetes:certificates.k8s.io/v1:CertificateSigningRequestList": "CertificateSigningRequestList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "certificates.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.certificates.v1beta1",
  "classes": {
   "kubernetes:certificates.k8s.io/v1beta1:CertificateSigningRequest": "CertificateSigningRequest",
   "kubernetes:certificates.k8s.io/v1beta1:CertificateSigningRequestList": "CertificateSigningRequestList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "coordination.k8s.io/v1",
  "fqn": "pulumi_kubernetes.coordination.v1",
  "classes": {
   "kubernetes:coordination.k8s.io/v1:Lease": "Lease",
   "kubernetes:coordination.k8s.io/v1:LeaseList": "LeaseList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "coordination.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.coordination.v1beta1",
  "classes": {
   "kubernetes:coordination.k8s.io/v1beta1:Lease": "Lease",
   "kubernetes:coordination.k8s.io/v1beta1:LeaseList": "LeaseList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "core/v1",
  "fqn": "pulumi_kubernetes.core.v1",
  "classes": {
   "kubernetes:core/v1:Binding": "Binding",
   "kubernetes:core/v1:ConfigMap": "ConfigMap",
   "kubernetes:core/v1:ConfigMapList": "ConfigMapList",
   "kubernetes:core/v1:Endpoints": "Endpoints",
   "kubernetes:core/v1:EndpointsList": "EndpointsList",
   "kubernetes:core/v1:Event": "Event",
   "kubernetes:core/v1:EventList": "EventList",
   "kubernetes:core/v1:LimitRange": "LimitRange",
   "kubernetes:core/v1:LimitRangeList": "LimitRangeList",
   "kubernetes:core/v1:Namespace": "Namespace",
   "kubernetes:core/v1:NamespaceList": "NamespaceList",
   "kubernetes:core/v1:Node": "Node",
   "kubernetes:core/v1:NodeList": "NodeList",
   "kubernetes:core/v1:PersistentVolume": "PersistentVolume",
   "kubernetes:core/v1:PersistentVolumeClaim": "PersistentVolumeClaim",
   "kubernetes:core/v1:PersistentVolumeClaimList": "PersistentVolumeClaimList",
   "kubernetes:core/v1:PersistentVolumeList": "PersistentVolumeList",
   "kubernetes:core/v1:Pod": "Pod",
   "kubernetes:core/v1:PodList": "PodList",
   "kubernetes:core/v1:PodTemplate": "PodTemplate",
   "kubernetes:core/v1:PodTemplateList": "PodTemplateList",
   "kubernetes:core/v1:ReplicationController": "ReplicationController",
   "kubernetes:core/v1:ReplicationControllerList": "ReplicationControllerList",
   "kubernetes:core/v1:ResourceQuota": "ResourceQuota",
   "kubernetes:core/v1:ResourceQuotaList": "ResourceQuotaList",
   "kubernetes:core/v1:Secret": "Secret",
   "kubernetes:core/v1:SecretList": "SecretList",
   "kubernetes:core/v1:Service": "Service",
   "kubernetes:core/v1:ServiceAccount": "ServiceAccount",
   "kubernetes:core/v1:ServiceAccountList": "ServiceAccountList",
   "kubernetes:core/v1:ServiceList": "ServiceList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "discovery.k8s.io/v1",
  "fqn": "pulumi_kubernetes.discovery.v1",
  "classes": {
   "kubernetes:discovery.k8s.io/v1:EndpointSlice": "EndpointSlice",
   "kubernetes:discovery.k8s.io/v1:EndpointSliceList": "EndpointSliceList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "discovery.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.discovery.v1beta1",
  "classes": {
   "kubernetes:discovery.k8s.io/v1beta1:EndpointSlice": "EndpointSlice",
   "kubernetes:discovery.k8s.io/v1beta1:EndpointSliceList": "EndpointSliceList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "events.k8s.io/v1",
  "fqn": "pulumi_kubernetes.events.v1",
  "classes": {
   "kubernetes:events.k8s.io/v1:Event": "Event",
   "kubernetes:events.k8s.io/v1:EventList": "EventList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "events.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.events.v1beta1",
  "classes": {
   "kubernetes:events.k8s.io/v1beta1:Event": "Event",
   "kubernetes:events.k8s.io/v1beta1:EventList": "EventList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "extensions/v1beta1",
  "fqn": "pulumi_kubernetes.extensions.v1beta1",
  "classes": {
   "kubernetes:extensions/v1beta1:DaemonSet": "DaemonSet",
   "kubernetes:extensions/v1beta1:DaemonSetList": "DaemonSetList",
   "kubernetes:extensions/v1beta1:Deployment": "Deployment",
   "kubernetes:extensions/v1beta1:DeploymentList": "DeploymentList",
   "kubernetes:extensions/v1beta1:Ingress": "Ingress",
   "kubernetes:extensions/v1beta1:IngressList": "IngressList",
   "kubernetes:extensions/v1beta1:NetworkPolicy": "NetworkPolicy",
   "kubernetes:extensions/v1beta1:NetworkPolicyList": "NetworkPolicyList",
   "kubernetes:extensions/v1beta1:PodSecurityPolicy": "PodSecurityPolicy",
   "kubernetes:extensions/v1beta1:PodSecurityPolicyList": "PodSecurityPolicyList",
   "kubernetes:extensions/v1beta1:ReplicaSet": "ReplicaSet",
   "kubernetes:extensions/v1beta1:ReplicaSetList": "ReplicaSetList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "flowcontrol.apiserver.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.flowcontrol.v1alpha1",
  "classes": {
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:FlowSchema": "FlowSchema",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:FlowSchemaList": "FlowSchemaList",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:PriorityLevelConfiguration": "PriorityLevelConfiguration",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:PriorityLevelConfigurationList": "PriorityLevelConfigurationList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "flowcontrol.apiserver.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.flowcontrol.v1beta1",
  "classes": {
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:FlowSchema": "FlowSchema",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:FlowSchemaList": "FlowSchemaList",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:PriorityLevelConfiguration": "PriorityLevelConfiguration",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:PriorityLevelConfigurationList": "PriorityLevelConfigurationList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "meta/v1",
  "fqn": "pulumi_kubernetes.meta.v1",
  "classes": {
   "kubernetes:meta/v1:Status": "Status"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "networking.k8s.io/v1",
  "fqn": "pulumi_kubernetes.networking.v1",
  "classes": {
   "kubernetes:networking.k8s.io/v1:Ingress": "Ingress",
   "kubernetes:networking.k8s.io/v1:IngressClass": "IngressClass",
   "kubernetes:networking.k8s.io/v1:IngressClassList": "IngressClassList",
   "kubernetes:networking.k8s.io/v1:IngressList": "IngressList",
   "kubernetes:networking.k8s.io/v1:NetworkPolicy": "NetworkPolicy",
   "kubernetes:networking.k8s.io/v1:NetworkPolicyList": "NetworkPolicyList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "networking.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.networking.v1beta1",
  "classes": {
   "kubernetes:networking.k8s.io/v1beta1:Ingress": "Ingress",
   "kubernetes:networking.k8s.io/v1beta1:IngressClass": "IngressClass",
   "kubernetes:networking.k8s.io/v1beta1:IngressClassList": "IngressClassList",
   "kubernetes:networking.k8s.io/v1beta1:IngressList": "IngressList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "node.k8s.io/v1",
  "fqn": "pulumi_kubernetes.node.v1",
  "classes": {
   "kubernetes:node.k8s.io/v1:RuntimeClass": "RuntimeClass",
   "kubernetes:node.k8s.io/v1:RuntimeClassList": "RuntimeClassList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "node.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.node.v1alpha1",
  "classes": {
   "kubernetes:node.k8s.io/v1alpha1:RuntimeClass": "RuntimeClass",
   "kubernetes:node.k8s.io/v1alpha1:RuntimeClassList": "RuntimeClassList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "node.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.node.v1beta1",
  "classes": {
   "kubernetes:node.k8s.io/v1beta1:RuntimeClass": "RuntimeClass",
   "kubernetes:node.k8s.io/v1beta1:RuntimeClassList": "RuntimeClassList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "policy/v1",
  "fqn": "pulumi_kubernetes.policy.v1",
  "classes": {
   "kubernetes:policy/v1:PodDisruptionBudget": "PodDisruptionBudget",
   "kubernetes:policy/v1:PodDisruptionBudgetList": "PodDisruptionBudgetList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "policy/v1beta1",
  "fqn": "pulumi_kubernetes.policy.v1beta1",
  "classes": {
   "kubernetes:policy/v1beta1:PodDisruptionBudget": "PodDisruptionBudget",
   "kubernetes:policy/v1beta1:PodDisruptionBudgetList": "PodDisruptionBudgetList",
   "kubernetes:policy/v1beta1:PodSecurityPolicy": "PodSecurityPolicy",
   "kubernetes:policy/v1beta1:PodSecurityPolicyList": "PodSecurityPolicyList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "rbac.authorization.k8s.io/v1",
  "fqn": "pulumi_kubernetes.rbac.v1",
  "classes": {
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRole": "ClusterRole",
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding": "ClusterRoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBindingList": "ClusterRoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleList": "ClusterRoleList",
   "kubernetes:rbac.authorization.k8s.io/v1:Role": "Role",
   "kubernetes:rbac.authorization.k8s.io/v1:RoleBinding": "RoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1:RoleBindingList": "RoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1:RoleList": "RoleList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "rbac.authorization.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.rbac.v1alpha1",
  "classes": {
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRole": "ClusterRole",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRoleBinding": "ClusterRoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRoleBindingList": "ClusterRoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRoleList": "ClusterRoleList",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:Role": "Role",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:RoleBinding": "RoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:RoleBindingList": "RoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:RoleList": "RoleList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "rbac.authorization.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.rbac.v1beta1",
  "classes": {
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRole": "ClusterRole",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleBinding": "ClusterRoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleBindingList": "ClusterRoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleList": "ClusterRoleList",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:Role": "Role",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:RoleBinding": "RoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:RoleBindingList": "RoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:RoleList": "RoleList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "scheduling.k8s.io/v1",
  "fqn": "pulumi_kubernetes.scheduling.v1",
  "classes": {
   "kubernetes:scheduling.k8s.io/v1:PriorityClass": "PriorityClass",
   "kubernetes:scheduling.k8s.io/v1:PriorityClassList": "PriorityClassList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "scheduling.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.scheduling.v1alpha1",
  "classes": {
   "kubernetes:scheduling.k8s.io/v1alpha1:PriorityClass": "PriorityClass",
   "kubernetes:scheduling.k8s.io/v1alpha1:PriorityClassList": "PriorityClassList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "scheduling.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.scheduling.v1beta1",
  "classes": {
   "kubernetes:scheduling.k8s.io/v1beta1:PriorityClass": "PriorityClass",
   "kubernetes:scheduling.k8s.io/v1beta1:PriorityClassList": "PriorityClassList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "settings.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.settings.v1alpha1",
  "classes": {
   "kubernetes:settings.k8s.io/v1alpha1:PodPreset": "PodPreset",
   "kubernetes:settings.k8s.io/v1alpha1:PodPresetList": "PodPresetList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "storage.k8s.io/v1",
  "fqn": "pulumi_kubernetes.storage.v1",
  "classes": {
   "kubernetes:storage.k8s.io/v1:CSIDriver": "CSIDriver",
   "kubernetes:storage.k8s.io/v1:CSIDriverList": "CSIDriverList",
   "kubernetes:storage.k8s.io/v1:CSINode": "CSINode",
   "kubernetes:storage.k8s.io/v1:CSINodeList": "CSINodeList",
   "kubernetes:storage.k8s.io/v1:StorageClass": "StorageClass",
   "kubernetes:storage.k8s.io/v1:StorageClassList": "StorageClassList",
   "kubernetes:storage.k8s.io/v1:VolumeAttachment": "VolumeAttachment",
   "kubernetes:storage.k8s.io/v1:VolumeAttachmentList": "VolumeAttachmentList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "storage.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.storage.v1alpha1",
  "classes": {
   "kubernetes:storage.k8s.io/v1alpha1:CSIStorageCapacity": "CSIStorageCapacity",
   "kubernetes:storage.k8s.io/v1alpha1:CSIStorageCapacityList": "CSIStorageCapacityList",
   "kubernetes:storage.k8s.io/v1alpha1:VolumeAttachment": "VolumeAttachment",
   "kubernetes:storage.k8s.io/v1alpha1:VolumeAttachmentList": "VolumeAttachmentList"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "storage.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.storage.v1beta1",
  "classes": {
   "kubernetes:storage.k8s.io/v1beta1:CSIDriver": "CSIDriver",
   "kubernetes:storage.k8s.io/v1beta1:CSIDriverList": "CSIDriverList",
   "kubernetes:storage.k8s.io/v1beta1:CSINode": "CSINode",
   "kubernetes:storage.k8s.io/v1beta1:CSINodeList": "CSINodeList",
   "kubernetes:storage.k8s.io/v1beta1:CSIStorageCapacity": "CSIStorageCapacity",
   "kubernetes:storage.k8s.io/v1beta1:CSIStorageCapacityList": "CSIStorageCapacityList",
   "kubernetes:storage.k8s.io/v1beta1:StorageClass": "StorageClass",
   "kubernetes:storage.k8s.io/v1beta1:StorageClassList": "StorageClassList",
   "kubernetes:storage.k8s.io/v1beta1:VolumeAttachment": "VolumeAttachment",
   "kubernetes:storage.k8s.io/v1beta1:VolumeAttachmentList": "VolumeAttachmentList"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "kubernetes",
  "token": "pulumi:providers:kubernetes",
  "fqn": "pulumi_kubernetes",
  "class": "Provider"
 }
]
"""
)
