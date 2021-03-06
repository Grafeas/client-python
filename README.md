# Grafeas
An API to insert and retrieve annotations on cloud artifacts.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1alpha1
- Package version: v1alpha1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import grafeas 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import grafeas
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = grafeas.GrafeasApi()
parent = 'parent_example' # str | 
body = grafeas.ApiNote() # ApiNote | 

try:
    # Creates a new `Note`.
    api_response = api_instance.create_note(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->create_note: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GrafeasApi* | [**create_note**](docs/GrafeasApi.md#create_note) | **POST** /v1alpha1/{parent}/notes | Creates a new &#x60;Note&#x60;.
*GrafeasApi* | [**create_occurrence**](docs/GrafeasApi.md#create_occurrence) | **POST** /v1alpha1/{parent}/occurrences | Creates a new &#x60;Occurrence&#x60;. Use this method to create &#x60;Occurrences&#x60; for a resource.
*GrafeasApi* | [**create_operation**](docs/GrafeasApi.md#create_operation) | **POST** /v1alpha1/{parent}/operations | Creates a new &#x60;Operation&#x60;.
*GrafeasApi* | [**get_occurrence_note**](docs/GrafeasApi.md#get_occurrence_note) | **GET** /v1alpha1/{name}/notes | Gets the &#x60;Note&#x60; attached to the given &#x60;Occurrence&#x60;.
*GrafeasApi* | [**list_note_occurrences**](docs/GrafeasApi.md#list_note_occurrences) | **GET** /v1alpha1/{name}/occurrences | Lists &#x60;Occurrences&#x60; referencing the specified &#x60;Note&#x60;. Use this method to get all occurrences referencing your &#x60;Note&#x60; across all your customer projects.
*GrafeasApi* | [**list_notes**](docs/GrafeasApi.md#list_notes) | **GET** /v1alpha1/{parent}/notes | Lists all &#x60;Notes&#x60; for a given project.
*GrafeasApi* | [**list_occurrences**](docs/GrafeasApi.md#list_occurrences) | **GET** /v1alpha1/{parent}/occurrences | Lists active &#x60;Occurrences&#x60; for a given project matching the filters.
*GrafeasApi* | [**update_note**](docs/GrafeasApi.md#update_note) | **PATCH** /v1alpha1/{name} | Updates an existing &#x60;Note&#x60;.
*GrafeasProjectsApi* | [**create_project**](docs/GrafeasProjectsApi.md#create_project) | **POST** /v1alpha1/projects | Creates a new &#x60;Project&#x60;.
*GrafeasProjectsApi* | [**delete_project**](docs/GrafeasProjectsApi.md#delete_project) | **DELETE** /v1alpha1/{name} | Deletes the given &#x60;Project&#x60; from the system.
*GrafeasProjectsApi* | [**get_project**](docs/GrafeasProjectsApi.md#get_project) | **GET** /v1alpha1/{name} | Returns the requested &#x60;Project&#x60;.
*GrafeasProjectsApi* | [**list_projects**](docs/GrafeasProjectsApi.md#list_projects) | **GET** /v1alpha1/projects | Lists &#x60;Projects&#x60;


## Documentation For Models

 - [ApiAliasContext](docs/ApiAliasContext.md)
 - [ApiAliasContextKind](docs/ApiAliasContextKind.md)
 - [ApiArtifact](docs/ApiArtifact.md)
 - [ApiBuildDetails](docs/ApiBuildDetails.md)
 - [ApiBuildProvenance](docs/ApiBuildProvenance.md)
 - [ApiBuildSignature](docs/ApiBuildSignature.md)
 - [ApiBuildType](docs/ApiBuildType.md)
 - [ApiCloudRepoSourceContext](docs/ApiCloudRepoSourceContext.md)
 - [ApiCommand](docs/ApiCommand.md)
 - [ApiCreateOperationRequest](docs/ApiCreateOperationRequest.md)
 - [ApiDeployable](docs/ApiDeployable.md)
 - [ApiDiscovery](docs/ApiDiscovery.md)
 - [ApiFileHashes](docs/ApiFileHashes.md)
 - [ApiGerritSourceContext](docs/ApiGerritSourceContext.md)
 - [ApiGitSourceContext](docs/ApiGitSourceContext.md)
 - [ApiHash](docs/ApiHash.md)
 - [ApiListNoteOccurrencesResponse](docs/ApiListNoteOccurrencesResponse.md)
 - [ApiListNotesResponse](docs/ApiListNotesResponse.md)
 - [ApiListOccurrencesResponse](docs/ApiListOccurrencesResponse.md)
 - [ApiListProjectsResponse](docs/ApiListProjectsResponse.md)
 - [ApiNote](docs/ApiNote.md)
 - [ApiNoteKind](docs/ApiNoteKind.md)
 - [ApiOccurrence](docs/ApiOccurrence.md)
 - [ApiPackageManagerLocation](docs/ApiPackageManagerLocation.md)
 - [ApiPgpSignedAttestation](docs/ApiPgpSignedAttestation.md)
 - [ApiProject](docs/ApiProject.md)
 - [ApiProjectRepoId](docs/ApiProjectRepoId.md)
 - [ApiRepoId](docs/ApiRepoId.md)
 - [ApiRepoSource](docs/ApiRepoSource.md)
 - [ApiSource](docs/ApiSource.md)
 - [ApiSourceContext](docs/ApiSourceContext.md)
 - [ApiStorageSource](docs/ApiStorageSource.md)
 - [ApiUpdateOperationRequest](docs/ApiUpdateOperationRequest.md)
 - [ApiVulnerabilityType](docs/ApiVulnerabilityType.md)
 - [AttestationAuthorityAttestationDetails](docs/AttestationAuthorityAttestationDetails.md)
 - [BuildSignatureKeyType](docs/BuildSignatureKeyType.md)
 - [DeployableDeploymentDetails](docs/DeployableDeploymentDetails.md)
 - [DeploymentDetailsPlatform](docs/DeploymentDetailsPlatform.md)
 - [DiscoveryDiscoveredDetails](docs/DiscoveryDiscoveredDetails.md)
 - [DockerImageBasis](docs/DockerImageBasis.md)
 - [DockerImageDerivedDetails](docs/DockerImageDerivedDetails.md)
 - [DockerImageFingerprint](docs/DockerImageFingerprint.md)
 - [DockerImageLayer](docs/DockerImageLayer.md)
 - [HashHashType](docs/HashHashType.md)
 - [LayerDirective](docs/LayerDirective.md)
 - [LongrunningOperation](docs/LongrunningOperation.md)
 - [NoteRelatedUrl](docs/NoteRelatedUrl.md)
 - [PackageManagerArchitecture](docs/PackageManagerArchitecture.md)
 - [PackageManagerDistribution](docs/PackageManagerDistribution.md)
 - [PackageManagerInstallationDetails](docs/PackageManagerInstallationDetails.md)
 - [PackageManagerPackage](docs/PackageManagerPackage.md)
 - [PgpSignedAttestationContentType](docs/PgpSignedAttestationContentType.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [ProtobufEmpty](docs/ProtobufEmpty.md)
 - [ProtobufFieldMask](docs/ProtobufFieldMask.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [VersionVersionKind](docs/VersionVersionKind.md)
 - [VulnerabilityTypeDetail](docs/VulnerabilityTypeDetail.md)
 - [VulnerabilityTypePackageIssue](docs/VulnerabilityTypePackageIssue.md)
 - [VulnerabilityTypeSeverity](docs/VulnerabilityTypeSeverity.md)
 - [VulnerabilityTypeVersion](docs/VulnerabilityTypeVersion.md)
 - [VulnerabilityTypeVulnerabilityDetails](docs/VulnerabilityTypeVulnerabilityDetails.md)
 - [VulnerabilityTypeVulnerabilityLocation](docs/VulnerabilityTypeVulnerabilityLocation.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



