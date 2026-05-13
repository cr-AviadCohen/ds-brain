# investigation.json

```json
{
  "DnsQueryResolvedDomainToDomain": {
    "template": {
      "overview": [
        "nonDefaultResolverEvidence",
        "recordType",
        "ttlRange",
        "sourceDomain",
        "resolvers",
        "targetDomain",
        "elementDisplayName"
      ],
      "details": [
        "nonDefaultResolverEvidence",
        "recordType",
        "ttlRange",
        "sourceDomain",
        "resolvers",
        "targetDomain",
        "elementDisplayName",
        "targetDomain.maliciousClassificationType"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "sourceDomain",
              "targetDomain",
              "resolvers",
              "Process.resolvedDnsQueriesDomainToDomain"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "sourceDomain",
              "targetDomain"
            ]
          },
          {
            "groupName": "C&C Communication",
            "features": [
              "nonDefaultResolverEvidence"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "recordType",
              "resolvers",
              "elementDisplayName",
              "ttlRange"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "sourceDomain",
              "self",
              "targetDomain"
            ]
          },
          {
            "groupName": "Target domain",
            "features": [
              "targetDomain",
              "targetDomain.maliciousClassificationType",
              "targetDomain.isInternalDomain"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "recordType",
              "ttlRange",
              "resolvers"
            ]
          },
          {
            "groupName": "Source domain",
            "features": [
              "sourceDomain",
              "sourceDomain.maliciousClassificationType",
              "sourceDomain.isInternalDomain"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "sourceDomain",
              "targetDomain"
            ]
          },
          {
            "groupName": "C&C Communication",
            "features": [
              "nonDefaultResolverEvidence"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "recordType",
              "resolvers",
              "elementDisplayName",
              "ttlRange"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "recordType",
              "resolvers",
              "ttlRange",
              "sourceDomain",
              "targetDomain",
              "nonDefaultResolverEvidence"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "recordType",
              "resolvers",
              "ttlRange",
              "sourceDomain",
              "targetDomain",
              "nonDefaultResolverEvidence"
            ]
          }
        ]
      }
    }
  },
  "ListeningConnection": {
    "template": {
      "overview": [
        "addressLocation",
        "connections",
        "knownServerRecord",
        "isIdentifiedSocket",
        "elementDisplayName"
      ],
      "details": [
        "addressLocation",
        "localAddress",
        "isUnidentifiedSocket",
        "transportProtocol",
        "ownerProcess",
        "ownerModule",
        "connections",
        "localPort",
        "ownerMachine",
        "ownerService",
        "knownServerRecord",
        "isIdentifiedSocket",
        "elementDisplayName",
        "ownerProcess.imageFile.maliciousClassificationType",
        "ownerProcess.imageFile.productType",
        "ownerProcess.imageFile.companyName",
        "ownerProcess.imageFile.productName",
        "ownerProcess.creationTime",
        "ownerProcess.endTime",
        "ownerProcess.calculatedUser",
        "ownerProcess.imageFile.isSigned",
        "ownerProcess.imageFile.signatureVerified",
        "ownerMachine.isActiveProbeConnected",
        "ownerMachine.osVersionType",
        "ownerMachine.isSuspiciousOrHasSuspiciousProcessOrFile"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "ownerProcess",
              "Connection.parent"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "addressLocation",
              "elementDisplayName",
              "localPort",
              "transportProtocol"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Connections",
            "features": [
              "connections"
            ]
          },
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "ownerProcess.calculatedUser",
              "ownerProcess",
              "self"
            ]
          },
          {
            "groupName": "Characteristics",
            "features": [
              "addressLocation"
            ]
          },
          {
            "groupName": "Process",
            "features": [
              "ownerProcess",
              "ownerProcess.calculatedName",
              "ownerProcess.calculatedUser",
              "ownerProcess.creationTime",
              "ownerProcess.endTime",
              "ownerProcess.imageFile.maliciousClassificationType"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "localAddress",
              "localPort",
              "transportProtocol",
              "endTime"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "connections",
              "localAddress",
              "ownerMachine",
              "ownerModule",
              "ownerProcess",
              "ownerService"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "knownServerRecord",
              "isUnidentifiedSocket",
              "isIdentifiedSocket"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "addressLocation",
              "elementDisplayName",
              "localPort",
              "transportProtocol"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "localPort",
              "transportProtocol",
              "ownerMachine",
              "ownerProcess",
              "ownerService",
              "connections"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "localPort",
              "transportProtocol",
              "ownerMachine",
              "ownerProcess",
              "ownerService",
              "connections"
            ]
          }
        ]
      }
    }
  },
  "Container": {
    "template": {
      "overview": [
        "elementDisplayName",
        "id",
        "creationTime",
        "status",
        "processes",
        "imageId",
        "allowPrivilegeEscalation",
        "commands"
      ],
      "detection": [
        "elementDisplayName",
        "id",
        "creationTime",
        "status",
        "processes",
        "imageId",
        "allowPrivilegeEscalation",
        "commands"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "processes"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "name",
              "id",
              "creationTime",
              "status",
              "processes",
              "imageId",
              "allowPrivilegeEscalation",
              "commands"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "name",
              "id",
              "creationTime",
              "status",
              "processes",
              "imageId",
              "allowPrivilegeEscalation",
              "commands"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Container Properties",
            "features": [
              "elementDisplayName",
              "id",
              "creationTime",
              "status",
              "imageId",
              "allowPrivilegeEscalation",
              "commands"
            ]
          },
          {
            "groupName": "Process",
            "features": [
              "processes"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "id",
              "creationTime",
              "status",
              "processes",
              "imageId",
              "allowPrivilegeEscalation"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "id",
              "creationTime",
              "status",
              "processes",
              "imageId",
              "allowPrivilegeEscalation"
            ]
          }
        ]
      }
    }
  },
  "ExecutableTaskAction": {
    "template": {
      "malop": [
        "elementDisplayName"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "fileInfo",
              "ScheduledTask.executableActions"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "executablePath",
              "executableArguments"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "executablePath",
              "executableArguments"
            ]
          },
          {
            "groupName": "File",
            "features": [
              "fileInfo",
              "fileInfo.extensionType",
              "fileInfo.correctedPath",
              "fileInfo.sha1String",
              "fileInfo.md5String",
              "fileInfo.sha256String",
              "fileInfo.productType",
              "fileInfo.companyName",
              "fileInfo.productName"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relations",
            "features": [
              "fileInfo"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "executablePath",
              "executableArguments"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "executablePath",
              "executableArguments",
              "fileInfo"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "executablePath",
              "executableArguments",
              "fileInfo"
            ]
          }
        ]
      }
    }
  },
  "Process": {
    "template": {
      "malop_communication": [
        "incomingConnections",
        "outgoingConnections",
        "ownerMachine",
        "calculatedUser"
      ],
      "overview": [
        "elementDisplayName",
        "pid",
        "ownerMachine",
        "calculatedUser",
        "parentProcess",
        "commandLine",
        "creationTime",
        "children",
        "endTime",
        "injectionMethod",
        "hostProcess",
        "hostedChildren",
        "tid",
        "loadedModules",
        "incomingConnections",
        "outgoingConnections",
        "imageFile.correctedPath",
        "imageFile.sha1String",
        "imageFile.sha256String",
        "imageFile.isSigned",
        "imageFile.signatureVerified",
        "imageFile.companyName",
        "imageFile.productName",
        "imageFile.productType",
        "imageFile.classificationLink",
        "imageFile.maliciousClassificationType",
        "imageFile.cves",
        "container"
      ],
      "detection_details": [
        "elementDisplayName",
        "pid",
        "ownerMachine",
        "calculatedUser",
        "commandLine",
        "creationTime",
        "endTime"
      ],
      "malop": [
        "elementDisplayName",
        "container",
        "pid",
        "ownerMachine",
        "calculatedUser",
        "calculatedName",
        "parentProcess",
        "commandLine",
        "decodedCommandLine",
        "creationTime",
        "children",
        "endTime",
        "injectionMethod",
        "hostProcess",
        "hostedChildren",
        "tid",
        "loadedModules",
        "incomingConnections",
        "outgoingConnections",
        "unresolvedDnsQueriesFromDomain",
        "self",
        "imageFile",
        "autorun",
        "autorun.name",
        "autorun.value",
        "imageFile.correctedPath",
        "imageFile.md5String",
        "imageFile.sha256String",
        "imageFile.sha1String",
        "imageFile.isSigned",
        "imageFile.signatureVerified",
        "imageFile.companyName",
        "imageFile.productName",
        "imageFile.productType",
        "imageFile.classificationLink",
        "imageFile.maliciousClassificationType",
        "imageFile.cves",
        "hostProcess",
        "injectionMethod",
        "loadedModules",
        "isChainOfInjections",
        "incomingConnectionsOfHostProcess",
        "outgoingConnectionsOfHostProcess",
        "isLiveProcess",
        "service",
        "service.elementDisplayName",
        "service.commandLineArguments",
        "service.description",
        "service.startType",
        "service.isActive",
        "scheduledTask",
        "scheduledTask.elementDisplayName",
        "scheduledTask.lastRunTime",
        "ransomwareAutoRemediationSuspended",
        "ransomwareAffectedFiles",
        "executionPrevented",
        "markedForPrevention",
        "blackListedFileHash",
        "connectionToBlackListAddress",
        "connectionToBlackListAddressByAddressRootCause",
        "connectionToBlackListDomain",
        "connectionToBlackListDomainByDomainRootCause",
        "connectionToMaliciousAddress",
        "connectionToMaliciousAddressByAddressRootCause",
        "connectionToMaliciousDomain",
        "connectionToMaliciousDomainByDomainRootCause",
        "credentialTheftMalop",
        "filelessMalware",
        "maliciousByAccessingAddressUsedByMalwares",
        "maliciousByAccessingAddressUsedByMalwaresByAddressRootCause",
        "maliciousByBlackListModule",
        "maliciousByCodeInjection",
        "maliciousByDgaDetection",
        "maliciousByDualExtensionByFileRootCause",
        "maliciousByDualExtension",
        "maliciousByFloatingCode",
        "maliciousByHighVolumeDataTransmittedByInjectedProcess",
        "maliciousByHighVolumeDataTransmittedByUnknownProcess",
        "maliciousByMaliciousToolModule",
        "maliciousByMalwareModule",
        "maliciousByRansomwareModule",
        "maliciousByScanningOfElevatedProcess",
        "maliciousByScanningOfInjectedProcess",
        "maliciousByScanningOfUnknownProcess",
        "maliciousByUnwantedModule",
        "maliciousExecutionOfPowerShell",
        "maliciousExecutionOfShellProcess",
        "maliciousFakeModuleLoaded",
        "maliciousFirewallHolePunching",
        "maliciousPrivilegeEscalation",
        "maliciousShadowCopyDeletion",
        "maliciousSignatureVerificationFailure",
        "maliciousToolByHashReputation",
        "maliciousUseOfPsexec",
        "malwareByHashReputation",
        "ransomwareByHashReputation",
        "rootkitProcessHide",
        "unwantedByHashReputation",
        "abusingWindowsAccessibilityFeatures",
        "maliciousUseOfOSProcess",
        "matchedActivities",
        "maliciousWebShellExecution",
        "packedProcessDecisionFeature",
        "connectionToBlackListAddress",
        "packedProcessDecisionFeature",
        "maliciousByOpeningMaliciousFile",
        "openedFiles",
        "jscriptRATMalop",
        "manInTheMiddleMalop",
        "maliciousHiddenModule",
        "shellcodeProcess",
        "covertProcessDecisionFeature",
        "maliciousTool",
        "maliciousMeterpreterAgent",
        "maliciousEmpireAgent",
        "maliciousCobaltAgent",
        "maliciousPeddleCheapAgent",
        "maliciousMimikatzAgent",
        "maliciousGenericAgent"
      ],
      "details": [
        "elementDisplayName",
        "container",
        "pid",
        "ownerMachine",
        "calculatedUser",
        "parentProcess",
        "commandLine",
        "creationTime",
        "sessionId",
        "children",
        "processRatio",
        "endTime",
        "injectionMethod",
        "hostProcess",
        "hostedChildren",
        "tid",
        "cpuTime",
        "signedDeviationsCpuUsageByName",
        "threadCount",
        "handleCount",
        "memoryUsage",
        "signedDeviationsMemoryUsageByName",
        "namedPipesCount",
        "rwxAnonymousSectionsCount",
        "rwxSectionsCount",
        "hasWindows",
        "hasVisibleWindows",
        "windowStateRatio",
        "architecture",
        "loadedModules",
        "incomingInternalConnections",
        "incomingExternalConnections",
        "outgoingInternalConnections",
        "outgoingExternalConnections",
        "unresolvedDnsQueriesFromDomain",
        "unresolvedDnsQueriesFromIp",
        "resolvedDnsQueriesDomainToIp",
        "resolvedDnsQueriesDomainToDomain",
        "resolvedDnsQueriesIpToDomain",
        "extensionRatio",
        "hashRatio",
        "autorun",
        "service",
        "imageFile",
        "imageFile.correctedPath",
        "imageFile.size",
        "imageFile.signedDeviationsSizeByExtension",
        "imageFile.createdTime",
        "imageFile.modifiedTime",
        "imageFile.md5String",
        "imageFile.sha1String",
        "imageFile.sha256String",
        "imageFile.isSigned",
        "imageFile.signatureVerified",
        "imageFile.companyName",
        "imageFile.fileDescription",
        "imageFile.fileVersion",
        "imageFile.productName",
        "imageFile.productVersion",
        "imageFile.productType",
        "imageFile.classificationLink",
        "imageFile.maliciousClassificationType",
        "imageFile.cves",
        "ownerMachine.isActiveProbeConnected",
        "ownerMachine.osVersionType",
        "ownerMachine.isSuspiciousOrHasSuspiciousProcessOrFile",
        "detectionEvents",
        "forensicArtifacts",
        "createdServices",
        "createdScheduledTasks"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links - Automatic execution",
            "features": [
              "autorun",
              "service",
              "scheduledTask"
            ]
          },
          {
            "groupName": "Links - MSRPC",
            "features": [
              "rpcRequests"
            ]
          },
          {
            "groupName": "Links - DNS",
            "features": [
              "resolvedDnsQueriesDomainToDomain",
              "resolvedDnsQueriesDomainToIp",
              "resolvedDnsQueriesIpToDomain",
              "unresolvedDnsQueriesFromDomain",
              "unresolvedDnsQueriesFromIp"
            ]
          },
          {
            "groupName": "Links - Session",
            "features": [
              "remoteSession",
              "logonSession"
            ]
          },
          {
            "groupName": "Links - Events",
            "features": [
              "fileAccessEvents",
              "registryEvents"
            ]
          },
          {
            "groupName": "Links - Injection",
            "features": [
              "hostProcess",
              "hostUser",
              "hostedChildren",
              "childrenCreatedByThread"
            ]
          },
          {
            "groupName": "Links - Machines Interaction",
            "features": [
              "allInteractions"
            ]
          },
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "calculatedUser",
              "imageFile",
              "connections",
              "parentProcess",
              "children",
              "execedBy",
              "loadedModules",
              "ipRangeScanSet",
              "hookedFunctions",
              "fileAccessEvents",
              "container",
              "contents"
            ]
          },
          {
            "groupName": "Links - LDAP queries",
            "features": [
              "ldapQueries"
            ]
          },
          {
            "groupName": "Links - Forensic Artifacts",
            "features": [
              "forensicArtifacts"
            ]
          },
          {
            "groupName": "Links - I/O Redirection",
            "features": [
              "stdinIoDevice",
              "stdoutIoDevice",
              "stderrIoDevice"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Exists in Malops",
            "features": [
              "hasMalops",
              "maliciousByAccessingAddressUsedByMalwares",
              "connectionToMaliciousDomain",
              "maliciousByDgaDetection",
              "rootkitProcessHide",
              "maliciousByHighVolumeDataTransmittedByUnknownProcess",
              "maliciousToolByHashReputation",
              "maliciousByMaliciousToolModule",
              "malwareByHashReputation",
              "maliciousByMalwareModule",
              "unwantedByHashReputation",
              "maliciousByUnwantedModule",
              "maliciousByCodeInjection",
              "maliciousByDualExtension",
              "maliciousByFloatingCode",
              "maliciousPrivilegeEscalation",
              "maliciousUseOfPsexec",
              "maliciousByScanningOfUnknownProcess",
              "maliciousExecutionOfShellProcess",
              "maliciousExecutionOfPowerShell"
            ]
          },
          {
            "groupName": "Scanning",
            "features": [
              "absoluteHighNumberOfInternalConnectionsEvidence",
              "scanningProcessSuspicion"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "hasMalops",
              "hasSuspicions",
              "commandLine",
              "decodedCommandLine",
              "detectedInjectedEvidence",
              "detectedInjectingEvidence",
              "isDownloadedFromInternet",
              "elevatingPrivilegesToChildEvidence",
              "hasExternalConnection",
              "hasListeningConnection",
              "dualExtensionNameEvidence",
              "unknownEvidence",
              "relatedToMalop",
              "imageFileUnsignedEvidence"
            ]
          },
          {
            "groupName": "Hiding and Obfuscation",
            "features": [
              "deletedParentProcessEvidence",
              "malwareModuleSuspicion",
              "dualExtensionNameEvidence",
              "screenSaverWithChildrenEvidence",
              "suspicionsScreenSaverEvidence"
            ]
          },
          {
            "groupName": "Classification - Parent Process",
            "features": [
              "parentProcessNotMatchHierarchySuspicion",
              "parentProcessNotAdminUserEvidence",
              "parentProcessFromRemovableDeviceEvidence",
              "parentPsexecEvidence"
            ]
          },
          {
            "groupName": "Suspicions",
            "features": [
              "hasSuspicions",
              "accessToMalwareAddressInfectedProcess",
              "connectingToBadReputationAddressSuspicion",
              "dgaSuspicion",
              "elevatingPrivilegesSuspicion",
              "hackingToolOfNonToolRunnerSuspicion",
              "hasSuspiciousExternalConnectionSuspicion",
              "hasSuspiciousInternalConnectionSuspicion",
              "suspiciousMailConnections",
              "highDataTransmittedSuspicion",
              "highDataVolumeTransmittedToMaliciousAddressSuspicion",
              "highNumberOfExternalConnectionsSuspicion",
              "highNumberOfInternalConnectionsSuspicion",
              "hostingInjectedThreadSuspicion",
              "maliciousInjectingCodeSuspicion",
              "knownMaliciousToolSuspicion",
              "knownMalwareSuspicion",
              "knownUnwantedSuspicion",
              "maliciousToolModuleSuspicion",
              "malwareModuleSuspicion",
              "nonDefaultResolverSuspicion",
              "parentProcessNotMatchHierarchySuspicion",
              "privilegeEscalationSuspicion",
              "maliciousInjectedCodeSuspicion",
              "shellInjectionSuspicion",
              "legitProcessInjectionSuspicion",
              "injectionToProtectedProcessSuspicion",
              "maliciousPeExecutionSuspicion",
              "scanningProcessSuspicion",
              "shellOfNonShellRunnerSuspicion",
              "suspiciousScreenSaver",
              "accessToMalwareAddressByUnknownProcess",
              "highDataVolumeTransmittedByUnknownProcess",
              "unknownUnsignedBySigningCompany",
              "unwantedModuleSuspicion",
              "maliciousUseOfPowershellSuspicion",
              "executedByPsexecSuspicion",
              "privilegeEscalationToAdminSuspicion"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "commandLine",
              "decodedCommandLine",
              "imageFileExtensionType",
              "applicablePid",
              "integrity",
              "elementDisplayName",
              "tid",
              "isAggregate",
              "openedFiles",
              "maliciousOpenedFiles",
              "isDotNetProtected",
              "container",
              "ecapabilitiesStr",
              "ruser"
            ]
          },
          {
            "groupName": "Employs Hacking Tools",
            "features": [
              "hasChildKnownHackerToolEvidence",
              "hackingToolOfNonToolRunnerEvidence",
              "hackingToolOfNonToolRunnerSuspicion",
              "hasRareChildProcessKnownHackerToolEvidence",
              "maliciousToolModuleSuspicion"
            ]
          },
          {
            "groupName": "Process Classification",
            "features": [
              "architecture",
              "commandLineContainsTempEvidence",
              "hasChildren",
              "hasClassification",
              "hasVisibleWindows",
              "hasWindows",
              "isInstaller",
              "isIdentifiedProduct",
              "hasModuleFromTempEvidence",
              "nonExecutableExtensionEvidence",
              "isNotShellRunner",
              "productType",
              "runningFromTempEvidence",
              "shellOfNonShellRunnerSuspicion",
              "shellWithElevatedPrivilegesEvidence",
              "systemUserEvidence",
              "unknownUnsignedEvidence",
              "rareProcessEvidence",
              "powershellEncodedCommandEvidence",
              "isEncodedCommandLine",
              "unexpectedAuditObjectAccessLsassEvidence",
              "unexpectedAuditObjectAccessSamKeyEvidence",
              "unexpectedAuditObjectAccessSamFileEvidence",
              "unexpectedAuditObjectAccessNtdsFileEvidence",
              "unexpectedAuditObjectAccessSamFileShadowCopyEvidence",
              "unexpectedAuditObjectAccessNtdsFileShadowCopyEvidence"
            ]
          },
          {
            "groupName": "Malicious Status",
            "features": [
              "hasMalops",
              "hasSuspicions",
              "relatedToMalop"
            ]
          },
          {
            "groupName": "Injections",
            "features": [
              "hasPeFloatingCodeEvidence",
              "hasSectionMismatchEvidence",
              "detectedInjectedEvidence",
              "detectedInjectingEvidence",
              "detectedInjectingToProtectedProcessEvidence",
              "hasInjectedChildren",
              "hostProcess",
              "hostUser",
              "hostingInjectedThreadEvidence",
              "injectedProtectedProcessEvidence",
              "maliciousInjectingCodeSuspicion",
              "injectionMethod",
              "isHostingInjectedThread",
              "maliciousInjectedCodeSuspicion",
              "maliciousPeExecutionSuspicion"
            ]
          },
          {
            "groupName": "WMI Activity",
            "features": [
              "isExectuedByWmi",
              "wmiQueryStrings",
              "wmiClientMachine",
              "wmiOperation",
              "wmiClientPid",
              "wmiIsLocal"
            ]
          },
          {
            "groupName": "Data Transfer",
            "features": [
              "hasAbsoluteHighVolumeConnectionToMaliciousAddressEvidence",
              "hasAbsoluteHighVolumeExternalOutgoingConnectionEvidence",
              "highDataTransmittedSuspicion",
              "highDataVolumeTransmittedToMaliciousAddressSuspicion",
              "highDataVolumeTransmittedByUnknownProcess"
            ]
          },
          {
            "groupName": "Execution",
            "features": [
              "markedForPrevention",
              "executionPrevented",
              "firstExecutionOfDownloadedProcessEvidence",
              "hasAutorun",
              "newProcessEvidence",
              "ransomwareAutoRemediationSuspended",
              "createdServices",
              "createdScheduledTasks"
            ]
          },
          {
            "groupName": "Domain Generation",
            "features": [
              "absoluteHighNumberOfInternalOutgoingEmbryonicConnectionsEvidence",
              "dgaSuspicion",
              "hasLowTtlDnsQueryEvidence",
              "highUnresolvedToResolvedRateEvidence",
              "manyUnresolvedRecordNotExistsEvidence"
            ]
          },
          {
            "groupName": "Classification - Process Communications",
            "features": [
              "hasExternalConnection",
              "hasExternalConnectionToWellKnownPortEvidence",
              "hasIncomingConnection",
              "hasInternalConnection",
              "hasMailConnectionForNonMailProcessEvidence",
              "hasListeningConnection",
              "hasOutgoingConnection",
              "hasUnresolvedDnsQueriesFromDomain",
              "multipleUnresolvedRecordNotExistsEvidence",
              "hasNonDefaultResolverEvidence"
            ]
          },
          {
            "groupName": "Lateral movement",
            "features": [
              "hasSuspiciousInternalConnectionEvidence",
              "highInternalOutgoingEmbryonicConnectionRateEvidence",
              "highNumberOfInternalConnectionsEvidence",
              "newProcessesAboveThresholdEvidence",
              "hasRareInternalConnectionEvidence"
            ]
          },
          {
            "groupName": "C&C Communication",
            "features": [
              "accessToMalwareAddressInfectedProcess",
              "connectingToBadReputationAddressSuspicion",
              "hasMaliciousConnectionEvidence",
              "hasSuspiciousExternalConnectionSuspicion",
              "highNumberOfExternalConnectionsSuspicion",
              "nonDefaultResolverSuspicion",
              "hasRareExternalConnectionEvidence",
              "hasRareRemoteAddressEvidence",
              "suspiciousMailConnections",
              "accessToMalwareAddressByUnknownProcess"
            ]
          },
          {
            "groupName": "MSRPC",
            "features": [
              "rpcRequests"
            ]
          },
          {
            "groupName": "Privilege escalation",
            "features": [
              "elevatingPrivilegesToChildEvidence",
              "parentProcessNotSystemUserEvidence",
              "privilegeEscalationEvidence"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "multipleSizeForHashEvidence",
              "isImageFileVerified",
              "knownMaliciousToolSuspicion",
              "knownMalwareSuspicion",
              "knownUnwantedSuspicion",
              "isMaliciousByHashEvidence",
              "imageFileMultipleCompanyNamesEvidence",
              "multipleHashForUnsignedPeInfoEvidence",
              "multipleNameForHashEvidence",
              "unknownEvidence",
              "rareHasPeMismatchEvidence",
              "unknownUnsignedBySigningCompany",
              "imageFileUnsignedEvidence",
              "imageFileUnsignedHasSignedVersionEvidence",
              "unwantedModuleSuspicion"
            ]
          },
          {
            "groupName": "LDAP queries",
            "features": [
              "ldapQueries"
            ]
          },
          {
            "groupName": "Contents",
            "features": [
              "contents"
            ]
          },
          {
            "groupName": "I/O Redirection",
            "features": [
              "stdinIoDevice",
              "stdoutIoDevice",
              "stderrIoDevice"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "User",
            "features": [
              "calculatedUser",
              "ruser"
            ]
          },
          {
            "groupName": "Container",
            "features": [
              "container",
              "container.id",
              "container.creationTime",
              "container.imageId",
              "container.status",
              "container.allowPrivilegeEscalation",
              "container.commands"
            ]
          },
          {
            "groupName": "Creation",
            "features": [
              "creatorProcess",
              "createdChildren",
              "seenCreation",
              "createdServices",
              "createdScheduledTasks"
            ]
          },
          {
            "groupName": "DNS",
            "features": [
              "resolvedDnsQueriesDomainToIp",
              "resolvedDnsQueriesDomainToDomain",
              "resolvedDnsQueriesIpToDomain",
              "unresolvedDnsQueriesFromIp",
              "unresolvedDnsQueriesFromDomain"
            ]
          },
          {
            "groupName": "Connection",
            "features": [
              "connections",
              "listeningConnections",
              "externalConnections",
              "internalConnections",
              "localConnections",
              "dynamicConfigurationConnections",
              "incomingConnections",
              "outgoingConnections",
              "suspiciousExternalConnections",
              "absoluteHighVolumeExternalConnections",
              "totalNumberOfConnections",
              "totalTransmittedBytes",
              "totalReceivedBytes"
            ]
          },
          {
            "groupName": "Functions",
            "features": [
              "hookedFunctions"
            ]
          },
          {
            "groupName": "File origin",
            "features": [
              "imageFile.isDownloadedFromInternet",
              "imageFile.downloadedFromDomain",
              "imageFile.downloadedFromIpAddress",
              "imageFile.downloadedFromUrl",
              "imageFile.downloadedFromUrlReferrer",
              "imageFile.downloadedFromEmailFrom",
              "imageFile.downloadedFromEmailMessageId",
              "imageFile.downloadedFromEmailSubject"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "applicablePid",
              "tid",
              "creationTime",
              "firstSeenTime",
              "lastSeenTime",
              "endTime",
              "commandLine",
              "decodedCommandLine",
              "iconBase64",
              "isAggregate",
              "isServiceHost",
              "isDotNetProtected",
              "lastDetectEventDetectionStatus",
              "ecapabilitiesStr",
              "ruser",
              "isProcessDebugged"
            ]
          },
          {
            "groupName": "Statistics",
            "features": [
              "newProcess",
              "processRatio",
              "hashRatio"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osType",
              "ownerMachine.osVersionType",
              "ownerMachine.deviceModel"
            ]
          },
          {
            "groupName": "Hosted Processes",
            "features": [
              "injectionMethod",
              "originInjector",
              "hostProcess",
              "creatorThread",
              "hostedChildren",
              "isInjectingProcess",
              "injectedChildren",
              "isFullProcessMemoryDump",
              "telemetryApi"
            ]
          },
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "calculatedUser",
              "parentProcess",
              "execedBy",
              "service",
              "self",
              "openedFiles",
              "children"
            ]
          },
          {
            "groupName": "WMI Activity",
            "features": [
              "isExectuedByWmi",
              "wmiQueryStrings",
              "wmiQueryObjects",
              "wmiPersistentObjects",
              "createdByWmi.wmiOperation",
              "createdByWmi.clientPid",
              "createdByWmi.isLocal",
              "createdByWmi.clientProcess",
              "createdByWmi.clientMachine"
            ]
          },
          {
            "groupName": "Execution",
            "features": [
              "parentProcess",
              "execedBy",
              "children",
              "childrenCreatedByThread",
              "failedToAccess",
              "service",
              "autorun",
              "loadedModules",
              "markedForPrevention",
              "executionPrevented",
              "ransomwareAutoRemediationSuspended",
              "ransomwareAffectedFiles",
              "totalNumOfInstances",
              "lastMinuteNumOfInstances",
              "lastSeenTimeStamp",
              "cveEventsStr",
              "keyloggerMethod"
            ]
          },
          {
            "groupName": "Events",
            "features": [
              "fileAccessEvents",
              "registryEvents"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "productType",
              "imageFile.signedInternalOrExternal",
              "imageFile.signatureVerifiedInternalOrExternal",
              "imageFile.maliciousClassificationType"
            ]
          },
          {
            "groupName": "DetectionEvents",
            "features": [
              "detectionEvents",
              "contents"
            ]
          },
          {
            "groupName": "Forensic Artifacts",
            "features": [
              "forensicArtifacts"
            ]
          },
          {
            "groupName": "MSRPC",
            "features": [
              "rpcRequests"
            ]
          },
          {
            "groupName": "Behavior",
            "features": [
              "cpuTime",
              "memoryUsage",
              "hasVisibleWindows",
              "integrity",
              "isHidden",
              "failedToAccess"
            ]
          },
          {
            "groupName": "File",
            "features": [
              "imageFile",
              "imageFile.extensionType",
              "imageFile.correctedPath",
              "imageFile.sha1String",
              "imageFile.md5String",
              "imageFile.sha256String",
              "imageFile.productType",
              "imageFile.companyName",
              "imageFile.productName",
              "imageFile.signerInternalOrExternal",
              "imageFile.avRemediationStatus",
              "imageFile.comments",
              "imageFile.cves",
              "openedFiles"
            ]
          },
          {
            "groupName": "Session",
            "features": [
              "logonSession",
              "remoteSession"
            ]
          },
          {
            "groupName": "LDAP queries",
            "features": [
              "ldapQueries"
            ]
          },
          {
            "groupName": "Protection Level",
            "features": [
              "protectionType",
              "protectionSigner"
            ]
          },
          {
            "groupName": "I/O Redirection - In",
            "features": [
              "stdinIoDevice",
              "stdinIoDevice.ioDeviceType",
              "stdinIoDevice.remoteAddress",
              "stdinIoDevice.remotePort"
            ]
          },
          {
            "groupName": "I/O Redirection - Out",
            "features": [
              "stdoutIoDevice",
              "stdoutIoDevice.ioDeviceType",
              "stdoutIoDevice.remoteAddress",
              "stdoutIoDevice.remotePort"
            ]
          },
          {
            "groupName": "I/O Redirection - Err",
            "features": [
              "stderrIoDevice",
              "stderrIoDevice.ioDeviceType",
              "stderrIoDevice.remoteAddress",
              "stderrIoDevice.remotePort"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships - DNS",
            "features": [
              "lowTtlDnsQueries",
              "nonDefaultResolverQueries",
              "resolvedDnsQueriesDomainToDomain",
              "resolvedDnsQueriesDomainToIp",
              "resolvedDnsQueriesIpToDomain",
              "suspiciousDnsQueryDomainToDomain",
              "unresolvedQueryFromSuspiciousDomain",
              "dnsQueryFromSuspiciousDomain",
              "dnsQueryToSuspiciousDomain",
              "unresolvedRecordNotExist",
              "unresolvedDnsQueriesFromDomain",
              "unresolvedDnsQueriesFromIp"
            ]
          },
          {
            "groupName": "Scanning",
            "features": [
              "absoluteHighNumberOfInternalConnectionsEvidence",
              "scanningProcessSuspicion"
            ]
          },
          {
            "groupName": "Hacking tools and advanced tools",
            "features": [
              "hasChildKnownHackerToolEvidence",
              "hackingToolOfNonToolRunnerEvidence",
              "hackingToolOfNonToolRunnerSuspicion",
              "hasRareChildProcessKnownHackerToolEvidence",
              "maliciousToolModuleSuspicion"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasMalops",
              "hasSuspicions",
              "relatedToMalop"
            ]
          },
          {
            "groupName": "Injection",
            "features": [
              "hasPeFloatingCodeEvidence",
              "hasSectionMismatchEvidence",
              "detectedInjectedEvidence",
              "detectedInjectingEvidence",
              "detectedInjectingToProtectedProcessEvidence",
              "hasInjectedChildren",
              "hostProcess",
              "hostUser",
              "hostingInjectedThreadEvidence",
              "injectedProtectedProcessEvidence",
              "maliciousInjectingCodeSuspicion",
              "injectionMethod",
              "isHostingInjectedThread",
              "maliciousInjectedCodeSuspicion",
              "maliciousPeExecutionSuspicion"
            ]
          },
          {
            "groupName": "Classification - parent",
            "features": [
              "parentProcessNotMatchHierarchySuspicion",
              "parentProcessNotAdminUserEvidence",
              "parentProcessFromRemovableDeviceEvidence"
            ]
          },
          {
            "groupName": "File origin",
            "features": [
              "imageFile.isDownloadedFromInternet",
              "imageFile.downloadedFromDomain",
              "imageFile.downloadedFromIpAddress",
              "imageFile.downloadedFromUrl",
              "imageFile.downloadedFromUrlReferrer",
              "imageFile.downloadedFromEmailFrom",
              "imageFile.downloadedFromEmailMessageId",
              "imageFile.downloadedFromEmailSubject"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "commandLine",
              "decodedCommandLine",
              "creationTime",
              "applicablePid",
              "endTime",
              "imageFileExtensionType",
              "integrity",
              "elementDisplayName",
              "tid",
              "isAggregate",
              "isDotNetProtected",
              "container",
              "ecapabilitiesStr",
              "ruser"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "creationTime",
              "endTime",
              "commandLine",
              "decodedCommandLine",
              "imageFile.maliciousClassificationType",
              "productType",
              "children",
              "parentProcess",
              "openedFiles",
              "ownerMachine",
              "calculatedUser",
              "imageFile",
              "imageFile.sha1String",
              "imageFile.md5String",
              "imageFile.sha256String",
              "imageFile.companyName",
              "imageFile.productName",
              "container"
            ]
          },
          {
            "groupName": "Relationships - modules",
            "features": [
              "maliciousToolClassificationModules",
              "malwareClassificationModules",
              "modulesNotInLoaderDbList",
              "modulesFromTemp",
              "unsignedWithSignedVersionModules",
              "unwantedClassificationModules",
              "loadedModules"
            ]
          },
          {
            "groupName": "Relationships",
            "features": [
              "autorun",
              "children",
              "childrenCreatedByThread",
              "connections",
              "elevatedPrivilegeChildren",
              "hackerToolChildren",
              "hostProcess",
              "hostUser",
              "hostedChildren",
              "imageFile",
              "injectedChildren",
              "loadedModules",
              "logonSession",
              "ownerMachine",
              "parentProcess",
              "remoteSession",
              "calculatedUser",
              "service",
              "execedBy"
            ]
          },
          {
            "groupName": "Execution",
            "features": [
              "firstExecutionOfDownloadedProcessEvidence",
              "hasAutorun",
              "newProcessEvidence",
              "markedForPrevention",
              "ransomwareAutoRemediationSuspended",
              "totalNumOfInstances",
              "lastMinuteNumOfInstances",
              "lastSeenTimeStamp",
              "wmiQueryStrings",
              "isExectuedByWmi",
              "createdServices",
              "createdScheduledTasks"
            ]
          },
          {
            "groupName": "Domain Generation",
            "features": [
              "absoluteHighNumberOfInternalOutgoingEmbryonicConnectionsEvidence",
              "dgaSuspicion",
              "hasLowTtlDnsQueryEvidence",
              "highUnresolvedToResolvedRateEvidence",
              "manyUnresolvedRecordNotExistsEvidence"
            ]
          },
          {
            "groupName": "Classification - communication",
            "features": [
              "hasExternalConnection",
              "hasExternalConnectionToWellKnownPortEvidence",
              "hasIncomingConnection",
              "hasInternalConnection",
              "hasMailConnectionForNonMailProcessEvidence",
              "hasListeningConnection",
              "hasOutgoingConnection",
              "hasUnknownSocket",
              "hasUnresolvedDnsQueriesFromDomain",
              "multipleUnresolvedRecordNotExistsEvidence",
              "hasNonDefaultResolverEvidence"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "activeServerProcessEvidence",
              "architecture",
              "commandLineContainsTempEvidence",
              "hasChildren",
              "hasClassification",
              "hasVisibleWindows",
              "hasWindows",
              "isInstaller",
              "isIdentifiedProduct",
              "isKnownServer",
              "hasModuleFromTempEvidence",
              "nonExecutableExtensionEvidence",
              "isNotShellRunner",
              "productType",
              "runningFromTempEvidence",
              "serverProcessEvidence",
              "shellOfNonShellRunnerSuspicion",
              "shellWithElevatedPrivilegesEvidence",
              "systemUserEvidence"
            ]
          },
          {
            "groupName": "Lateral movement",
            "features": [
              "hasSuspiciousInternalConnectionEvidence",
              "highInternalOutgoingEmbryonicConnectionRateEvidence",
              "highNumberOfInternalConnectionsEvidence",
              "newProcessesAboveThresholdEvidence",
              "hasRareInternalConnectionEvidence"
            ]
          },
          {
            "groupName": "Data transfer",
            "features": [
              "hasAbsoluteHighVolumeConnectionToMaliciousAddressEvidence",
              "hasAbsoluteHighVolumeExternalOutgoingConnectionEvidence",
              "highDataTransmittedSuspicion",
              "highDataVolumeTransmittedToMaliciousAddressSuspicion",
              "highDataVolumeTransmittedByUnknownProcess"
            ]
          },
          {
            "groupName": "C&C Communication",
            "features": [
              "accessToMalwareAddressInfectedProcess",
              "connectingToBadReputationAddressSuspicion",
              "hasMaliciousConnectionEvidence",
              "hasSuspiciousExternalConnectionSuspicion",
              "highNumberOfExternalConnectionsSuspicion",
              "nonDefaultResolverSuspicion",
              "hasRareExternalConnectionEvidence",
              "hasRareRemoteAddressEvidence",
              "suspiciousMailConnections",
              "accessToMalwareAddressByUnknownProcess"
            ]
          },
          {
            "groupName": "MSRPC",
            "features": [
              "rpcRequests"
            ]
          },
          {
            "groupName": "Privilege escalation",
            "features": [
              "elevatingPrivilegesToChildEvidence",
              "parentProcessNotSystemUserEvidence",
              "privilegeEscalationEvidence"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "multipleSizeForHashEvidence",
              "isImageFileVerified",
              "knownMaliciousToolSuspicion",
              "knownMalwareSuspicion",
              "knownUnwantedSuspicion",
              "isMaliciousByHashEvidence",
              "imageFileMultipleCompanyNamesEvidence",
              "multipleHashForUnsignedPeInfoEvidence",
              "multipleNameForHashEvidence",
              "unknownEvidence",
              "rareHasPeMismatchEvidence",
              "imageFile.signedInternalOrExternal",
              "unknownUnsignedBySigningCompany",
              "imageFileUnsignedEvidence",
              "imageFileUnsignedHasSignedVersionEvidence",
              "unwantedModuleSuspicion",
              "imageFile.maliciousClassificationType",
              "imageFile.signerInternalOrExternal"
            ]
          },
          {
            "groupName": "Relationships - Communication",
            "features": [
              "connectionsToMaliciousDomain",
              "connectionsToMalwareAddresses",
              "externalConnections",
              "absoluteHighVolumeMaliciousAddressConnections",
              "absoluteHighVolumeExternalConnections",
              "incomingConnections",
              "incomingConnectionsFromUnidentifiedSocket",
              "incomingExternalConnections",
              "incomingInternalConnections",
              "internalConnections",
              "listeningConnections",
              "localConnections",
              "mailConnections",
              "maliciousReputationConnections",
              "outgoingConnections",
              "outgoingExternalConnections",
              "outgoingInternalConnections",
              "suspiciousExternalConnections",
              "suspiciousInternalConnections",
              "wellKnownPortConnections",
              "connections"
            ]
          },
          {
            "groupName": "Hiding and obfuscation",
            "features": [
              "deletedParentProcessEvidence",
              "malwareModuleSuspicion",
              "dualExtensionNameEvidence",
              "hiddenFileExtensionEvidence",
              "rightToLeftFileExtensionEvidence",
              "screenSaverWithChildrenEvidence",
              "suspicionsScreenSaverEvidence"
            ]
          },
          {
            "groupName": "LDAP queries",
            "features": [
              "ldapQueries"
            ]
          },
          {
            "groupName": "Forensic Artifacts",
            "features": [
              "forensicArtifacts"
            ]
          },
          {
            "groupName": "I/O Redirection",
            "features": [
              "stdinIoDevice",
              "stdoutIoDevice",
              "stderrIoDevice"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "creationTime",
              "endTime",
              "commandLine",
              "isImageFileSignedAndVerified",
              "imageFile.maliciousClassificationType",
              "productType",
              "children",
              "parentProcess",
              "ownerMachine",
              "calculatedUser",
              "imageFile",
              "imageFile.sha1String",
              "imageFile.md5String",
              "imageFile.companyName",
              "imageFile.productName",
              "container",
              "stdinDeviceInfo",
              "stdoutDeviceInfo",
              "stderrDeviceInfo"
            ]
          }
        ]
      }
    }
  },
  "MalopProcess": {
    "template": {
      "overview": [
        "rootCauseElementTypes",
        "rootCauseElementHashes",
        "rootCauseElementCompanyProduct",
        "rootCauseElementNames",
        "primaryRootCauseElements",
        "creationTime",
        "affectedMachines",
        "affectedUsers",
        "detectionType",
        "malopActivityTypes",
        "decisionFeature",
        "malopStartTime",
        "malopLastUpdateTime",
        "elementDisplayName",
        "isBlocked",
        "hasRansomwareSuspendedProcesses",
        "allRansomwareProcessesSuspended",
        "iconBase64"
      ],
      "detection": [
        "rootCauseElementNames",
        "rootCauseElementTypes",
        "rootCauseElements",
        "rootCauseElementCompanyProduct",
        "primaryRootCauseElements",
        "creationTime",
        "affectedMachines",
        "affectedUsers",
        "containers",
        "decisionFeatureSet",
        "detectionType",
        "decisionFeature",
        "malopLastUpdateTime",
        "isBlocked",
        "hasActiveProcesses",
        "hasRansomwareSuspendedProcesses",
        "allRansomwareProcessesSuspended",
        "iconBase64",
        "group"
      ],
      "malop": [
        "rootCauseElementTypes",
        "rootCauseElementHashes",
        "rootCauseElementCompanyProduct",
        "rootCauseElementNames",
        "rootCauseElements",
        "primaryRootCauseElements",
        "creationTime",
        "affectedMachines",
        "affectedUsers",
        "suspects",
        "detectionType",
        "malopActivityTypes",
        "decisionFeature",
        "decisionFeatureSet",
        "malopStartTime",
        "malopLastUpdateTime",
        "totalNumberOfOutgoingConnections",
        "totalNumberOfIncomingConnections",
        "totalTransmittedBytes",
        "totalReceivedBytes",
        "filesToRemediate",
        "isBlocked",
        "hasRansomwareSuspendedProcesses",
        "allRansomwareProcessesSuspended",
        "iconBase64"
      ],
      "details": [
        "rootCauseElementTypes",
        "rootCauseElementHashes",
        "rootCauseElementCompanyProduct",
        "rootCauseElementNames",
        "primaryRootCauseElements",
        "creationTime",
        "affectedMachines",
        "detectionType",
        "malopActivityTypes",
        "decisionFeature",
        "malopStartTime",
        "malopLastUpdateTime",
        "elementDisplayName"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "affectedMachines",
              "affectedUsers",
              "suspects"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "malopActivityTypes",
              "decisionFeature",
              "rootCauseElementHashes",
              "rootCauseElementNames",
              "rootCauseElementTypes",
              "rootCauseElementCompanyProduct",
              "detectionType"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "malopActivityTypes",
              "totalNumberOfIncomingConnections",
              "totalNumberOfOutgoingConnections",
              "totalReceivedBytes",
              "totalTransmittedBytes",
              "suspectsProcesses",
              "suspectsHostProcesses",
              "suspectsInjectingProcesses"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "self"
            ]
          },
          {
            "groupName": "User",
            "features": [
              "affectedUsers"
            ]
          },
          {
            "groupName": "Characteristics",
            "features": [
              "malopStartTime",
              "malopLastUpdateTime"
            ]
          },
          {
            "groupName": "Root cause",
            "features": [
              "rootCauseElementTypes",
              "rootCauseElements",
              "rootCauseElementNames",
              "rootCauseElementHashes",
              "rootCauseElementCompanyProduct"
            ]
          },
          {
            "groupName": "Processes",
            "features": [
              "suspects",
              "newSuspects"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "creationTime",
              "decisionFeature",
              "detectionType",
              "malopActivityTypes"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "affectedMachines"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "affectedMachines",
              "affectedUsers",
              "suspects",
              "newSuspects"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "decisionFeature",
              "detectionType",
              "rootCauseElementHashes",
              "rootCauseElementCompanyProduct"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "detectionType",
              "malopActivityTypes",
              "affectedMachines",
              "affectedUsers",
              "suspects",
              "totalNumberOfIncomingConnections",
              "totalNumberOfOutgoingConnections",
              "totalReceivedBytes",
              "totalTransmittedBytes",
              "rootCauseElementNames"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "malopStartTime",
              "malopActivityTypes",
              "malopLastUpdateTime",
              "totalNumberOfIncomingConnections",
              "totalNumberOfOutgoingConnections",
              "totalTransmittedBytes",
              "totalReceivedBytes",
              "creationTime"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "detectionType",
              "malopActivityTypes",
              "affectedMachines",
              "affectedUsers",
              "suspects",
              "totalNumberOfIncomingConnections",
              "totalNumberOfOutgoingConnections",
              "totalReceivedBytes",
              "totalTransmittedBytes"
            ]
          }
        ]
      }
    }
  },
  "FileAccessEvent": {
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerProcess",
              "ownerMachine",
              "ownerUser",
              "fileInfo"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "ownerProcess",
              "fileEventType",
              "fileEventStatus",
              "path",
              "newPath",
              "isHidden"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "ownerUser",
              "ownerProcess",
              "self",
              "fileInfo"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "ownerProcess",
              "fileInfo",
              "fileEventType",
              "fileEventStatus",
              "firstAccessTime",
              "path",
              "newPath",
              "isHidden",
              "isAlternateDataStream",
              "eventCounter",
              "lastAccessTime"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "ownerProcess",
              "ownerMachine",
              "fileInfo",
              "path",
              "fileEventType",
              "fileEventStatus",
              "firstAccessTime",
              "newPath",
              "isHidden",
              "lastAccessTime",
              "eventCounter"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "ownerProcess",
              "firstAccessTime",
              "fileEventType",
              "fileEventStatus",
              "path",
              "newPath",
              "lastAccessTime",
              "eventCounter"
            ]
          }
        ]
      }
    }
  },
  "DomainName": {
    "template": {
      "overview": [
        "isInternalSecondLevelDomain",
        "everResolvedDomain",
        "everResolvedSecondLevelDomain",
        "maliciousClassificationType",
        "name",
        "isInternalDomain",
        "elementDisplayName"
      ],
      "malop": [
        "elementDisplayName",
        "maliciousClassificationType"
      ],
      "details": [
        "isInternalSecondLevelDomain",
        "everResolvedDomain",
        "everResolvedSecondLevelDomain",
        "maliciousClassificationType",
        "name",
        "isInternalDomain",
        "elementDisplayName"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "DnsQueryResolvedDomainToIp.sourceDomain",
              "DnsQueryResolvedDomainToDomain.sourceDomain",
              "DnsQueryResolvedDomainToDomain.targetDomain",
              "DnsQueryResolvedIpToDomain.targetDomain",
              "DnsQueryUnresolvedFromDomain.sourceDomain"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Malicious activity",
            "features": [
              "hasSuspicions",
              "maliciousClassificationType"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "elementDisplayName",
              "maliciousClassificationType",
              "isInternalDomain",
              "everResolvedDomain",
              "everResolvedSecondLevelDomain"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "classificationLink",
              "isInternalDomain",
              "isInternalSecondLevelDomain",
              "everResolvedDomain",
              "everResolvedSecondLevelDomain",
              "classificationComment"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "self"
            ]
          },
          {
            "groupName": "Characteristics",
            "features": [
              "isInternalDomain",
              "isInternalSecondLevelDomain",
              "everResolvedDomain",
              "everResolvedSecondLevelDomain",
              "isReverseLookup"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "name",
              "topLevelDomain",
              "secondLevelDomain"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "maliciousClassificationType",
              "relatedToMalop",
              "isTorrentDomain"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Malicious activity",
            "features": [
              "hasSuspicions",
              "maliciousClassificationType",
              "isSuspiciousDomainEvidence"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "isInternalDomain",
              "isInternalSecondLevelDomain",
              "maliciousClassificationType",
              "everResolvedDomain",
              "everResolvedSecondLevelDomain",
              "classificationComment"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "classificationLink",
              "isInternalDomain",
              "isInternalSecondLevelDomain",
              "everResolvedDomain",
              "everResolvedSecondLevelDomain",
              "classificationComment",
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "isInternalDomain",
              "everResolvedDomain",
              "everResolvedSecondLevelDomain",
              "maliciousClassificationType",
              "elementDisplayName"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "maliciousClassificationType",
              "isInternalDomain",
              "everResolvedDomain",
              "everResolvedSecondLevelDomain"
            ]
          }
        ]
      }
    }
  },
  "QuarantineFile": {
    "template": {
      "overview": [
        "ownerMachine",
        "file",
        "quarantineFile",
        "creationTime",
        "md5String",
        "sha1String"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "file",
              "quarantineFile",
              "ownerMachine"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "File info",
            "features": [
              "md5String",
              "sha1String"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "md5String",
              "sha1String",
              "hasSuspicions",
              "hasMalops",
              "quarantineFileStatus"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "hasSuspicions",
              "hasMalops"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "file",
              "self",
              "quarantineFile"
            ]
          },
          {
            "groupName": "File info",
            "features": [
              "elementDisplayName",
              "md5String",
              "sha1String"
            ]
          },
          {
            "groupName": "Quarantine",
            "features": [
              "creationTime",
              "quarantineFileStatus",
              "requester"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "file",
              "quarantineFile"
            ]
          },
          {
            "groupName": "File info",
            "features": [
              "md5String",
              "sha1String",
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Quarantine",
            "features": [
              "creationTime",
              "quarantineFileStatus"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "ownerMachine",
              "file",
              "quarantineFile",
              "creationTime",
              "md5String",
              "sha1String"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "ownerMachine",
              "file",
              "quarantineFile",
              "creationTime",
              "md5String",
              "sha1String"
            ]
          }
        ]
      }
    }
  },
  "NetworkInterface": {
    "template": {
      "overview": [
        "name",
        "id",
        "macAddressFormat",
        "networkStatistics",
        "elementDisplayName"
      ],
      "details": [
        "name",
        "id",
        "macAddressFormat",
        "networkStatistics",
        "elementDisplayName"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ipAddress",
              "ownerMachine",
              "dhcpServer",
              "dnsServer",
              "gateway",
              "proxies",
              "localNetworks"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "macAddressFormat",
              "id",
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "name",
              "id",
              "description",
              "macAddressFormat",
              "flags",
              "dhcpServer",
              "dnsServer",
              "gateway",
              "proxies"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "dhcpServer",
              "dnsServer",
              "gateway",
              "ipAddress",
              "ownerMachine",
              "proxies"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "macAddressFormat",
              "id",
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "ipAddress",
              "ownerMachine",
              "gateway",
              "dnsServer",
              "dhcpServer",
              "macAddressFormat"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "ipAddress",
              "ownerMachine",
              "gateway",
              "dnsServer",
              "dhcpServer",
              "macAddressFormat"
            ]
          }
        ]
      }
    }
  },
  "Msrpc": {
    "template": {
      "overview": [
        "creationTimestamp",
        "endPoint",
        "eventCounter",
        "eventSoruce",
        "interfaceUUID",
        "interfaceName",
        "lastSeenTimeStamp",
        "networkAddress",
        "opNum",
        "options",
        "process",
        "protocolName",
        "statusName",
        "impersonationLevelName",
        "authLevelName",
        "authServiceName"
      ],
      "details": [
        "elementDisplayName",
        "creationTimestamp",
        "endPoint",
        "eventCounter",
        "eventSoruce",
        "interfaceUUID",
        "interfaceName",
        "lastSeenTimeStamp",
        "networkAddress",
        "opNum",
        "options",
        "process",
        "protocolName",
        "statusName",
        "impersonationLevelName",
        "authServiceName",
        "authLevelName"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "process"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "process",
              "interfaceUUID",
              "interfaceName",
              "opNum",
              "operationName",
              "eventSoruce",
              "networkAddress"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "statusName",
              "protocolName",
              "endPoint",
              "options",
              "eventCounter",
              "lastSeenTimeStamp",
              "authLevelName",
              "impersonationLevelName",
              "authServiceName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "process",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "interfaceUUID",
              "interfaceName",
              "opNum",
              "operationName",
              "creationTimestamp",
              "endPoint",
              "eventCounter",
              "eventSoruce",
              "lastSeenTimeStamp",
              "networkAddress",
              "options",
              "protocolName",
              "statusName",
              "authLevelName",
              "authServiceName",
              "impersonationLevelName"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "process",
              "creationTimestamp",
              "interfaceUUID",
              "interfaceName",
              "opNum",
              "operationName",
              "eventSoruce",
              "networkAddress",
              "statusName",
              "protocolName",
              "lastSeenTimeStamp",
              "authLevelName",
              "authServiceName",
              "impersonationLevelName"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "interfaceUUID",
              "interfaceName",
              "opNum",
              "operationName",
              "process",
              "eventSoruce",
              "creationTimestamp",
              "statusName",
              "protocolName",
              "endPoint",
              "options",
              "authLevelName",
              "authServiceName",
              "networkAddress"
            ]
          }
        ]
      }
    }
  },
  "IpRangeScan": {
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerProcess"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerProcess.ownerMachine",
              "ownerProcess.calculatedUser",
              "ownerProcess",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "ownerProcess",
              "range",
              "count",
              "range.version"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "ownerProcess",
              "range",
              "count"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "ownerProcess",
              "range",
              "count"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "ownerProcess",
              "range",
              "count"
            ]
          }
        ]
      }
    }
  },
  "EmailAddress": {
    "template": {
      "detection": [
        "email",
        "users"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "userEmailAddresses"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "email",
              "users"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "email",
              "users"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "self"
            ]
          },
          {
            "groupName": "Relationships",
            "features": [
              "userEmailAddresses"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "email"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "userEmailAddresses"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "email",
              "users"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "email",
              "users"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "users",
              "email"
            ]
          }
        ]
      }
    }
  },
  "MountPoint": {
    "template": {
      "overview": [
        "name",
        "mediaType",
        "deviceName",
        "volumeName",
        "isRemovableDevice",
        "elementDisplayName"
      ],
      "details": [
        "name",
        "mediaType",
        "deviceName",
        "volumeName",
        "isRemovableDevice",
        "elementDisplayName"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "files",
              "ownerMachine"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "deviceName",
              "mediaType",
              "elementDisplayName",
              "isRemovableDevice",
              "volumeName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self"
            ]
          },
          {
            "groupName": "Characteristics",
            "features": [
              "isRemovableDevice"
            ]
          },
          {
            "groupName": "Files",
            "features": [
              "files"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "name",
              "mediaType",
              "mountedFrom",
              "deviceName",
              "volumeName",
              "creationTime",
              "endTime"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "files",
              "ownerMachine"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "deviceName",
              "mediaType",
              "elementDisplayName",
              "isRemovableDevice",
              "volumeName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "deviceName",
              "mediaType",
              "volumeName",
              "ownerMachine",
              "files"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "deviceName",
              "mediaType",
              "volumeName",
              "ownerMachine",
              "files"
            ]
          }
        ]
      }
    }
  },
  "DnsQueryUnresolvedFromDomain": {
    "template": {
      "overview": [
        "externalDomainNotExists",
        "everResolvedDomain",
        "everResolvedSecondLevelDomain",
        "recordType",
        "sourceDomain",
        "errorCode",
        "resolvers",
        "isInternalDomain",
        "elementDisplayName"
      ],
      "details": [
        "externalDomainNotExists",
        "everResolvedDomain",
        "everResolvedSecondLevelDomain",
        "recordType",
        "sourceDomain",
        "errorCode",
        "resolvers",
        "isInternalDomain",
        "elementDisplayName",
        "sourceDomain.maliciousClassificationType"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "sourceDomain",
              "resolvers",
              "Process.unresolvedDnsQueriesFromDomain"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Classification",
            "features": [
              "confirmedUnresolvedDomainEvidence",
              "isInternalDomain"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "errorCode",
              "recordType",
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "sourceDomain",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "recordType",
              "resolvers",
              "errorCode"
            ]
          },
          {
            "groupName": "Source domain",
            "features": [
              "sourceDomain",
              "sourceDomain.maliciousClassificationType",
              "isInternalDomain",
              "sourceDomain.everResolvedDomain",
              "sourceDomain.everResolvedSecondLevelDomain",
              "confirmedUnresolvedDomainEvidence"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "sourceDomain",
              "resolvers"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "confirmedUnresolvedDomainEvidence",
              "isInternalDomain",
              "sourceDomain.everResolvedDomain",
              "sourceDomain.everResolvedSecondLevelDomain"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "errorCode",
              "recordType",
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "errorCode",
              "recordType",
              "confirmedUnresolvedDomainEvidence",
              "isInternalDomain",
              "sourceDomain.everResolvedDomain",
              "sourceDomain.everResolvedSecondLevelDomain",
              "sourceDomain",
              "resolvers"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "errorCode",
              "recordType",
              "confirmedUnresolvedDomainEvidence",
              "isInternalDomain",
              "sourceDomain.everResolvedDomain",
              "sourceDomain.everResolvedSecondLevelDomain",
              "sourceDomain",
              "resolvers"
            ]
          }
        ]
      }
    }
  },
  "DnsQueryResolvedIpToDomain": {
    "template": {
      "overview": [
        "nonDefaultResolverEvidence",
        "recordType",
        "sourceIpAddress",
        "ttlRange",
        "resolvers",
        "targetDomain",
        "elementDisplayName"
      ],
      "details": [
        "nonDefaultResolverEvidence",
        "recordType",
        "sourceIpAddress",
        "ttlRange",
        "resolvers",
        "targetDomain",
        "elementDisplayName",
        "sourceIpAddress.countryNameOrNotExternalType",
        "sourceIpAddress.ownerMachine",
        "targetDomain.maliciousClassificationType"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "targetDomain",
              "sourceIpAddress",
              "resolvers",
              "Process.resolvedDnsQueriesIpToDomain"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "C&C Communication",
            "features": [
              "nonDefaultResolverEvidence"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "recordType",
              "elementDisplayName",
              "ttlRange"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "sourceIpAddress",
              "self",
              "targetDomain"
            ]
          },
          {
            "groupName": "Source IP address",
            "features": [
              "sourceIpAddress",
              "sourceIpAddress.countryNameOrNotExternalType",
              "sourceIpAddress.ownerMachine"
            ]
          },
          {
            "groupName": "Target domain",
            "features": [
              "targetDomain",
              "targetDomain.maliciousClassificationType",
              "targetDomain.isInternalDomain"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "recordType",
              "ttlRange",
              "resolvers"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "targetDomain",
              "sourceIpAddress",
              "resolvers"
            ]
          },
          {
            "groupName": "C&C Communication",
            "features": [
              "nonDefaultResolverEvidence"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "recordType",
              "elementDisplayName",
              "ttlRange"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "recordType",
              "elementDisplayName",
              "ttlRange",
              "nonDefaultResolverEvidence",
              "targetDomain",
              "sourceIpAddress",
              "resolvers"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "recordType",
              "elementDisplayName",
              "ttlRange",
              "nonDefaultResolverEvidence",
              "targetDomain",
              "sourceIpAddress",
              "resolvers"
            ]
          }
        ]
      }
    }
  },
  "FunctionDetails": {
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "exportingFile"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "exportingFile",
              "self",
              "hookingModule"
            ]
          },
          {
            "groupName": "Hooking Module",
            "features": [
              "hookingModule.elementDisplayName",
              "hookingModule.file.path",
              "hookingModule.address",
              "hookingModule.file.sha1String",
              "hookingModule.file.md5String",
              "hookingModule.file.sha256String",
              "hookingModule.file.isSigned",
              "hookingModule.file.productType",
              "hookingModule.file.signatureVerified"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "hookingModule",
              "type",
              "hookOffset",
              "hookedModule"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "exportingFile.ownerMachine",
              "exportingFile.ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "functionName",
              "exportingFile",
              "hookingModule"
            ]
          }
        ]
      }
    }
  },
  "NetworkMachine": {
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "machine"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "self",
              "machine"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "hostName",
              "domainFqdn"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "machine"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "machine"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "machine"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "machine"
            ]
          }
        ]
      }
    }
  },
  "FileHash": {
    "template": {
      "overview": [
        "sha1HexString",
        "iconMd5HexString",
        "maliciousClassificationType"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": []
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "sha1HexString",
              "iconMd5HexString",
              "maliciousClassificationType"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Execution",
            "features": []
          },
          {
            "groupName": "Reputation",
            "features": [
              "maliciousClassificationType"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "sha1HexString",
              "iconMd5HexString"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "iconMd5HexString",
              "maliciousClassificationType"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "sha1HexString",
              "iconMd5HexString"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "sha1HexString",
              "iconMd5HexString",
              "maliciousClassificationType"
            ]
          }
        ]
      }
    }
  },
  "LocalNetwork": {
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "NetworkInterface.localNetworks"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Hardware Properties",
            "features": [
              "networkInterfaces"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "searchDomain",
              "networkInterfaces"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "searchDomain",
              "dnsServer",
              "dhcpServer",
              "gatewayIp",
              "wifiSsid"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "networkInterfaces",
              "self"
            ]
          },
          {
            "groupName": "Hardware Properties",
            "features": [
              "networkInterfaces"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "ipRange.subnet",
              "ipRange.mask",
              "searchDomain",
              "wifiSsid",
              "dnsServer",
              "dhcpServer",
              "gatewayIp"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Hardware Properties",
            "features": [
              "networkInterfaces"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "ipRange.subnet",
              "ipRange.mask",
              "searchDomain",
              "networkInterfaces"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "ipRange.subnet",
              "ipRange.mask",
              "searchDomain",
              "dnsServer",
              "dhcpServer",
              "wifiSsid",
              "gatewayIp"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "ipRange.subnet",
              "ipRange.mask",
              "searchDomain",
              "wifiSsid",
              "dnsServer",
              "dhcpServer",
              "gatewayIp"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "ipRange.subnet",
              "ipRange.mask",
              "searchDomain",
              "wifiSsid",
              "dnsServer",
              "dhcpServer",
              "gatewayIp"
            ]
          }
        ]
      }
    }
  },
  "Module": {
    "template": {
      "overview": [
        "isFloating",
        "ownerMachine",
        "moduleName",
        "maliciousClassification",
        "hasAutorun",
        "file.correctedPath",
        "file.sha1String",
        "file.sha256String",
        "file.isSigned",
        "file.signatureVerified",
        "file.companyName",
        "file.productName",
        "file.productType",
        "file.classificationLink",
        "file.maliciousClassificationType",
        "elementDisplayName"
      ],
      "malop": [
        "elementDisplayName",
        "file",
        "file.classificationLink",
        "file.companyName",
        "file.productName",
        "file.productType",
        "file.maliciousClassificationType"
      ],
      "details": [
        "isFloating",
        "ownerMachine",
        "moduleName",
        "maliciousClassification",
        "hasAutorun",
        "file.correctedPath",
        "file.sha1String",
        "file.sha256String",
        "file.isSigned",
        "file.signatureVerified",
        "file.companyName",
        "file.productName",
        "file.productType",
        "file.classificationLink",
        "file.maliciousClassificationType",
        "elementDisplayName"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "file",
              "ownerMachine",
              "Process.loadedModules"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Execution",
            "features": [
              "markedForPrevention",
              "isBlocked"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "elementDisplayName",
              "hasMalops",
              "hasSuspicions",
              "hasAutorun",
              "isFloating",
              "notInLoaderDbEvidence",
              "maliciousClassification"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "hasAutorun",
              "isFloating",
              "notInLoaderDbEvidence"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasMalops",
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "fileUnsignedHasSignedVersionEvidence"
            ]
          },
          {
            "groupName": "Suspicions",
            "features": [
              "moduleReputationSuspicion"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "address",
              "exeHeaderProtection",
              "exeAllocatedProtection"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "file",
              "self"
            ]
          },
          {
            "groupName": "Execution",
            "features": [
              "markedForPrevention",
              "isBlocked",
              "executionPreventedEvidence",
              "executionPreventedSuspicion"
            ]
          },
          {
            "groupName": "Characteristics",
            "features": [
              "isFloating",
              "hasAutorun"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "address",
              "sizeOfImage",
              "exeHeaderProtection",
              "exeAllocatedProtection",
              "exeHeaderMalformed"
            ]
          },
          {
            "groupName": "File",
            "features": [
              "file",
              "file.correctedPath",
              "file.sha1String",
              "file.md5String",
              "file.sha256String",
              "file.maliciousClassificationType",
              "file.productType",
              "file.companyName",
              "file.productName",
              "file.isSigned",
              "file.signatureVerified"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "file",
              "ownerMachine"
            ]
          },
          {
            "groupName": "Execution",
            "features": [
              "markedForPrevention",
              "isBlocked"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "hasAutorun",
              "isFloating",
              "notInLoaderDbEvidence"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasMalops",
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "fileUnsignedHasSignedVersionEvidence"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "address"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "file",
              "ownerMachine",
              "hasAutorun",
              "isFloating",
              "notInLoaderDbEvidence",
              "maliciousClassification"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "file",
              "ownerMachine",
              "hasAutorun",
              "isFloating",
              "notInLoaderDbEvidence",
              "maliciousClassification"
            ]
          }
        ]
      }
    }
  },
  "File": {
    "template": {
      "overview": [
        "md5String",
        "sha256String",
        "companyName",
        "maliciousClassificationType",
        "isSigned",
        "isDownloadedFromInternet",
        "productName",
        "productType",
        "ownerMachine",
        "size",
        "productVersion",
        "createdTime",
        "endTime",
        "sha1String",
        "isSuspicious",
        "correctedPath",
        "extensionType",
        "modifiedTime",
        "signatureVerifiedInternalOrExternal",
        "elementDisplayName",
        "cves",
        "behaviourIdString"
      ],
      "detection_details": [
        "ownerMachine",
        "sha1String",
        "correctedPath",
        "modifiedTime",
        "createdTime",
        "elementDisplayName",
        "fileIsQuarantined",
        "companyName",
        "productName",
        "behaviourIdString"
      ],
      "malop": [
        "elementDisplayName",
        "classificationLink",
        "companyName",
        "productName",
        "productType",
        "maliciousClassificationType",
        "cves"
      ],
      "details": [
        "md5String",
        "sha256String",
        "companyName",
        "maliciousClassificationType",
        "isSigned",
        "isDownloadedFromInternet",
        "productName",
        "productType",
        "ownerMachine",
        "size",
        "productVersion",
        "createdTime",
        "endTime",
        "sha1String",
        "isSuspicious",
        "correctedPath",
        "extensionType",
        "modifiedTime",
        "signatureVerifiedInternalOrExternal",
        "elementDisplayName",
        "ownerMachine.isActiveProbeConnected",
        "ownerMachine.osVersionType",
        "ownerMachine.isSuspiciousOrHasSuspiciousProcessOrFile",
        "cves",
        "wmiPersistentObjects",
        "behaviourIdString"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links - Execution",
            "features": [
              "autorun",
              "ExecutableTaskAction.fileInfo"
            ]
          },
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "Process.imageFile",
              "Module.file",
              "Driver.file",
              "Service.binaryFile",
              "HostsFile.file",
              "mount",
              "fileAccessEvents",
              "FileHash.contents"
            ]
          },
          {
            "groupName": "Links - Quarantine",
            "features": [
              "quarantineVersion",
              "originalVersion",
              "fileIsQuarantined",
              "fileIsQuarantinedVersion"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "File Reputation",
            "features": [
              "multipleCompanyNamesEvidence",
              "multipleHashForUnsignedPeInfoEvidence",
              "signatureVerifiedInternalOrExternal",
              "unsignedHasSignedVersionEvidence",
              "signerInternalOrExternal",
              "signedInternalOrExternal"
            ]
          },
          {
            "groupName": "File Origin",
            "features": [
              "isDownloadedFromInternet",
              "downloadedFromDomain",
              "downloadedFromIpAddress",
              "downloadedFromUrl",
              "downloadedFromUrlReferrer",
              "downloadedFromEmailFrom",
              "downloadedFromEmailMessageId",
              "downloadedFromEmailSubject"
            ]
          },
          {
            "groupName": "Extended Properties",
            "features": [
              "comments",
              "fileVersion",
              "legalCopyright",
              "legalTrademarks",
              "privateBuild",
              "specialBuild"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "elementDisplayName",
              "extensionType",
              "signedInternalOrExternal",
              "signatureVerifiedInternalOrExternal",
              "sha1String",
              "hasMalops",
              "hasSuspicions",
              "isDownloadedFromInternet",
              "maliciousClassificationType",
              "dualExtensionEvidence"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "classificationLink",
              "isPEFile",
              "executedByProcessEvidence",
              "hasAutorun",
              "hasClassification",
              "isInstallerProperties",
              "isFromRemovableDevice",
              "productType",
              "secondExtensionType",
              "temporaryFolderEvidence",
              "classificationComment"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "companyName",
              "extensionType",
              "fileDescription",
              "elementDisplayName",
              "internalName",
              "md5String",
              "sha256String",
              "originalFileName",
              "correctedPath",
              "productName",
              "productVersion",
              "sha1String",
              "size",
              "applicationIdentifier",
              "cves",
              "fileHash.contents"
            ]
          },
          {
            "groupName": "Malicious Activity - Hiding and obfuscation",
            "features": [
              "dualExtensionEvidence",
              "hiddenFileExtensionEvidence",
              "rightToLeftFileExtensionEvidence"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "hasMalops",
              "hasSuspicions",
              "fileReputationSuspicion",
              "fileVersionSuspicion",
              "suspiciousScreenSaver",
              "classificationBlocking",
              "maliciousClassificationType",
              "hackingToolClassificationEvidence",
              "reportedAsMaliciousByAVSuspicion",
              "fileHash.contents"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "File events",
            "features": [
              "fileAccessEvents"
            ]
          },
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self"
            ]
          },
          {
            "groupName": "Execution",
            "features": [
              "classificationBlocking"
            ]
          },
          {
            "groupName": "Anti-Malware",
            "features": [
              "avRemediationStatus",
              "classificationDetectionName",
              "avScanTime"
            ]
          },
          {
            "groupName": "Quarantine",
            "features": [
              "quarantineVersion",
              "originalVersion"
            ]
          },
          {
            "groupName": "DetectionEvents",
            "features": [
              "detectionEvents",
              "fileHash.contents"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "relatedToMalop",
              "isSuspicious",
              "maliciousClassificationType"
            ]
          },
          {
            "groupName": "File origin",
            "features": [
              "isDownloadedFromInternet",
              "downloadedFromDomain",
              "downloadedFromIpAddress",
              "downloadedFromUrl",
              "downloadedFromUrlReferrer",
              "downloadedFromEmailFrom",
              "downloadedFromEmailMessageId",
              "downloadedFromEmailSubject"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "applicationIdentifier",
              "correctedPath",
              "canonizedPath",
              "originalFileName",
              "internalName",
              "mount",
              "mountedAs",
              "createdTime",
              "modifiedTime",
              "md5String",
              "sha1String",
              "sha256String",
              "fileEntropy",
              "productType",
              "companyName",
              "productName",
              "fileVersion",
              "productVersion",
              "signerInternalOrExternal",
              "signedInternalOrExternal",
              "signatureVerifiedInternalOrExternal",
              "signedByMicrosoft",
              "extensionType",
              "size",
              "legalCopyright",
              "legalTrademarks",
              "comments",
              "privateBuild",
              "specialBuild",
              "lastDetectEventDetectionStatus",
              "cves",
              "behaviourIdString"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          },
          {
            "groupName": "WMI Persistent",
            "features": [
              "wmiPersistentObjects"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "autorun",
              "autoruns",
              "fileHash",
              "ownerMachine",
              "mount"
            ]
          },
          {
            "groupName": "Extended Properties",
            "features": [
              "comments",
              "fileVersion",
              "legalCopyright",
              "legalTrademarks",
              "privateBuild",
              "specialBuild"
            ]
          },
          {
            "groupName": "Malicious Activity - Hiding and Obfuscation",
            "features": [
              "dualExtensionEvidence",
              "hiddenFileExtensionEvidence",
              "rightToLeftFileExtensionEvidence"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "classificationLink",
              "classificationComment",
              "isPEFile",
              "executedByProcessEvidence",
              "hasAutorun",
              "isInstallerProperties",
              "isFromRemovableDevice",
              "productType",
              "secondExtensionType",
              "temporaryFolderEvidence",
              "signedInternalOrExternal",
              "signatureVerifiedInternalOrExternal",
              "multipleCompanyNamesEvidence",
              "multipleHashForUnsignedPeInfoEvidence",
              "unsignedHasSignedVersionEvidence",
              "classificationBlocking"
            ]
          },
          {
            "groupName": "File origin",
            "features": [
              "isDownloadedFromInternet",
              "downloadedFromDomain",
              "downloadedFromIpAddress",
              "downloadedFromUrl",
              "downloadedFromUrlReferrer",
              "downloadedFromEmailFrom",
              "downloadedFromEmailMessageId",
              "downloadedFromEmailSubject"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "applicationIdentifier",
              "companyName",
              "createdTime",
              "extensionType",
              "fileDescription",
              "internalName",
              "md5String",
              "sha256String",
              "fileEntropy",
              "modifiedTime",
              "originalFileName",
              "correctedPath",
              "productName",
              "productVersion",
              "sha1String",
              "size",
              "comments",
              "fileVersion",
              "cves",
              "behaviourIdString"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "maliciousClassificationType",
              "elementDisplayName",
              "ownerMachine",
              "avRemediationStatus",
              "signerInternalOrExternal",
              "signedInternalOrExternal",
              "signatureVerifiedInternalOrExternal",
              "sha1String",
              "createdTime",
              "modifiedTime",
              "size",
              "correctedPath",
              "productName"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "hasMalops",
              "hasSuspicions",
              "maliciousClassificationType",
              "hackingToolClassificationEvidence"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "ownerMachine",
              "avRemediationStatus",
              "isSigned",
              "signatureVerifiedInternalOrExternal",
              "sha1String",
              "maliciousClassificationType",
              "createdTime",
              "modifiedTime",
              "size",
              "correctedPath",
              "productName",
              "productVersion",
              "companyName",
              "internalName"
            ]
          }
        ]
      }
    }
  },
  "DnsQueryUnresolvedFromIp": {
    "template": {
      "overview": [
        "recordType",
        "sourceIpAddress",
        "errorCode",
        "resolvers",
        "elementDisplayName"
      ],
      "details": [
        "recordType",
        "sourceIpAddress",
        "errorCode",
        "resolvers",
        "elementDisplayName",
        "sourceIpAddress.countryNameOrNotExternalType",
        "sourceIpAddress.ownerMachine"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "sourceIpAddress",
              "resolvers",
              "Process.unresolvedDnsQueriesFromIp"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "errorCode",
              "recordType",
              "resolvers",
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "sourceIpAddress",
              "self"
            ]
          },
          {
            "groupName": "Source IP address",
            "features": [
              "sourceIpAddress",
              "sourceIpAddress.countryNameOrNotExternalType",
              "sourceIpAddress.ownerMachine"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "recordType",
              "resolvers",
              "errorCode"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "sourceIpAddress"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "errorCode",
              "recordType",
              "resolvers",
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "errorCode",
              "recordType",
              "resolvers",
              "sourceIpAddress"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "errorCode",
              "recordType",
              "resolvers",
              "sourceIpAddress"
            ]
          }
        ]
      }
    }
  },
  "RegistryEvent": {
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "registryProcess",
              "registryEntry",
              "ownerMachine"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "registryProcess",
              "self"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "data",
              "registryDataType",
              "registryOperationType",
              "registryProcess",
              "timestamp",
              "firstTime",
              "detectionTimesNumber",
              "isCLSID"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "registryProcess",
              "self",
              "registryEntry"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "registryProcess",
              "elementDisplayName",
              "data",
              "registryDataType",
              "registryOperationType",
              "firstTime",
              "timestamp",
              "detectionTimesNumber",
              "isCLSID"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "registryProcess",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "data",
              "registryDataType",
              "registryOperationType",
              "registryProcess",
              "timestamp",
              "registryEntry",
              "firstTime",
              "detectionTimesNumber"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "registryProcess",
              "registryEntry",
              "data",
              "operationType",
              "ownerMachine"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "registryPath",
              "registryDataType",
              "registryOperationType",
              "registryEntryType"
            ]
          }
        ]
      }
    }
  },
  "User": {
    "template": {
      "overview": [
        "isSuspicious",
        "numberOfMachines",
        "privileges",
        "passwordAgeDays",
        "username",
        "isLocalSystem",
        "comment",
        "domain",
        "elementDisplayName",
        "emailAddress"
      ],
      "detection": [
        "elementDisplayName",
        "isAdmin",
        "isLocalSystem",
        "isDomainUser"
      ],
      "detection_details": [
        "elementDisplayName",
        "isAdmin",
        "isLocalSystem",
        "isDomainUser",
        "adSid",
        "adDisplayName",
        "adLogonName",
        "adDepartment",
        "adSamAccountName",
        "adMemberOf",
        "adCompany",
        "adAssociatedDomain",
        "adMail",
        "adOU",
        "adPrimaryGroupID",
        "adCountry"
      ],
      "malop": [
        "elementDisplayName",
        "self",
        "ownerOrganization.name",
        "domain",
        "processes",
        "passwordAgeDays",
        "privileges",
        "emailAddress"
      ],
      "details": [
        "isSuspicious",
        "hasPowerTool",
        "numberOfMachines",
        "privileges",
        "passwordAgeDays",
        "username",
        "maliciousProcesses",
        "isLocalSystem",
        "processes",
        "suspiciousProcesses",
        "hasSuspiciousProcess",
        "hasRareProcessWithExternalConnections",
        "maliciousTools",
        "comment",
        "domain",
        "elementDisplayName",
        "emailAddress"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "processes",
              "LogonSession.user",
              "RemoteSession.user",
              "ownerMachine",
              "emailAddress"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "User Activity",
            "features": [
              "runningPowerToolEvidence",
              "hasRareProcessWithExternalConnections",
              "runningRareProcessWithExternalConnectionsEvidence",
              "highNumberOfDownloadedProcessesEvidence",
              "newAdminToolForUserEvidence"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "domain",
              "elementDisplayName",
              "hasSuspicions",
              "isLocalSystem"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "domain",
              "emailAddress",
              "numberOfMachines",
              "privileges",
              "comment",
              "passwordAgeDays",
              "isLocalSystem",
              "isAdmin",
              "highNumberOfMachinesEvidence",
              "sid"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "hasSuspicions",
              "runningMaliciousProcessEvidence",
              "trespassingUserBySuspiciousActivitySuspicion"
            ]
          },
          {
            "groupName": "Active Directory",
            "features": [
              "adAssociatedDomain",
              "adCanonicalName",
              "adCompany",
              "adCountry",
              "adCreated",
              "adDepartment",
              "adDisplayName",
              "adLogonName",
              "adMail",
              "adMemberOf",
              "adOU",
              "adPrimaryGroupID",
              "adSamAccountName",
              "adTitle"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self"
            ]
          },
          {
            "groupName": "Relationships",
            "features": [
              "processes",
              "maliciousProcesses",
              "maliciousTools",
              "suspiciousProcesses",
              "loginActions"
            ]
          },
          {
            "groupName": "Processes",
            "features": [
              "processes",
              "newProcessesCount",
              "downloadedProcessesCount"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "username",
              "sid",
              "domain",
              "emailAddress",
              "privileges",
              "passwordAgeDays",
              "isLocalSystem",
              "isAdmin",
              "comment",
              "ownerOrganization.name",
              "fullname"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "maliciousProcesses",
              "suspiciousProcesses",
              "maliciousTools",
              "runningRareProcessWithExternalConnectionsEvidence",
              "rareProcessesWithExternalConnections"
            ]
          },
          {
            "groupName": "Active Directory",
            "features": [
              "adDisplayName",
              "adLogonName",
              "adDepartment",
              "adCompany",
              "adOU",
              "adTitle",
              "adMail",
              "adCreated",
              "adCanonicalName",
              "adSamAccountName",
              "adMemberOf",
              "adCountry",
              "adAssociatedDomain",
              "adPrimaryGroupID"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "User Activity",
            "features": [
              "runningPowerToolEvidence",
              "highNumberOfDownloadedProcessesEvidence",
              "highNumberOfMachinesEvidence",
              "newAdminToolForUserEvidence",
              "hasPowerTool"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "username",
              "domain",
              "emailAddress",
              "numberOfMachines",
              "passwordAgeDays",
              "privileges",
              "isLocalSystem",
              "isAdmin",
              "comment",
              "sid"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "domain",
              "ownerOrganization.name",
              "ownerMachine",
              "isLocalSystem",
              "isAdmin",
              "highNumberOfMachinesEvidence"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "hasMaliciousProcess",
              "hasSuspicions",
              "hasSuspiciousProcess",
              "runningMaliciousProcessEvidence",
              "hasRareProcessWithExternalConnections"
            ]
          },
          {
            "groupName": "Active Directory",
            "features": [
              "adAssociatedDomain",
              "adCanonicalName",
              "adCompany",
              "adCreated",
              "adCountry",
              "adDepartment",
              "adDisplayName",
              "adLogonName",
              "adMail",
              "adMemberOf",
              "adOU",
              "adPrimaryGroupID",
              "adSamAccountName",
              "adTitle"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "domain",
              "ownerMachine",
              "ownerOrganization.name",
              "isLocalSystem",
              "emailAddress"
            ]
          }
        ]
      }
    }
  },
  "Driver": {
    "template": {
      "overview": [
        "endTime",
        "name",
        "knownMaliciousDriver",
        "creationTime",
        "ownerMachine",
        "newDriverEvidence",
        "file",
        "rareDriverEvidence",
        "service",
        "elementDisplayName",
        "author",
        "description"
      ],
      "details": [
        "endTime",
        "name",
        "knownMaliciousDriver",
        "creationTime",
        "ownerMachine",
        "newDriverEvidence",
        "file",
        "rareDriverEvidence",
        "service",
        "elementDisplayName",
        "file.maliciousClassificationType",
        "file.productType",
        "file.companyName",
        "file.productName",
        "file.isSigned",
        "file.signatureVerified",
        "ownerMachine.isActiveProbeConnected",
        "ownerMachine.osVersionType",
        "ownerMachine.isSuspiciousOrHasSuspiciousProcessOrFile",
        "author",
        "description"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "file",
              "ownerMachine",
              "service"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Classification",
            "features": [
              "newDriverEvidence"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Suspicions",
            "features": [
              "knownMaliciousDriver"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "author",
              "description"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "file",
              "self"
            ]
          },
          {
            "groupName": "Service",
            "features": [
              "service"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "name",
              "creationTime",
              "endTime",
              "author",
              "description"
            ]
          },
          {
            "groupName": "File",
            "features": [
              "file",
              "file.correctedPath",
              "file.sha1String",
              "file.md5String",
              "file.sha256String",
              "file.maliciousClassificationType",
              "file.productType",
              "file.companyName",
              "file.productName",
              "file.isSigned",
              "file.signatureVerified"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "file",
              "ownerMachine",
              "service"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "newDriverEvidence"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "creationTime",
              "elementDisplayName",
              "endTime",
              "author",
              "description"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "creationTime",
              "file",
              "ownerMachine",
              "service"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "creationTime",
              "file",
              "ownerMachine",
              "service",
              "author",
              "description"
            ]
          }
        ]
      }
    }
  },
  "Machine": {
    "template": {
      "overview": [
        "elementDisplayName",
        "osVersionType",
        "platformArchitecture",
        "isActiveProbeConnected",
        "users",
        "isSuspiciousOrHasSuspiciousProcessOrFile",
        "processes",
        "maliciousProcesses",
        "suspiciousProcesses",
        "isLaptop",
        "uptime",
        "elementDisplayName",
        "isIsolated",
        "lastSeenTimeStamp",
        "timeStampSinceLastConnectionTime"
      ],
      "detection": [
        "elementDisplayName",
        "osType",
        "isActiveProbeConnected",
        "lastSeenTimeStamp",
        "timeStampSinceLastConnectionTime",
        "isIsolated"
      ],
      "detection_details": [
        "elementDisplayName",
        "osType",
        "isActiveProbeConnected",
        "lastSeenTimeStamp",
        "timeStampSinceLastConnectionTime",
        "isIsolated",
        "pylumId",
        "adOU",
        "adOrganization",
        "adDisplayName",
        "adDNSHostName",
        "adDepartment",
        "adCompany",
        "adLocation",
        "adMachineRole"
      ],
      "malop": [
        "elementDisplayName",
        "osVersionType",
        "platformArchitecture",
        "isActiveProbeConnected",
        "lastSeenTimeStamp",
        "timeStampSinceLastConnectionTime",
        "users",
        "processes",
        "self",
        "isIsolated"
      ],
      "details": [
        "computerName",
        "freeDiskSpace",
        "networkInterfaces",
        "isActiveProbeConnected",
        "isSuspiciousOrHasSuspiciousProcessOrFile",
        "timezoneUTCOffsetMinutes",
        "hasRemovableDevice",
        "cpuCount",
        "totalMemory",
        "removableDevices",
        "autoruns",
        "registryEntries",
        "services",
        "maliciousProcesses",
        "osVersionType",
        "isLaptop",
        "drivers",
        "totalDiskSpace",
        "freeMemory",
        "suspiciousProcesses",
        "processes",
        "mbrHashString",
        "maliciousTools",
        "platformArchitecture",
        "users",
        "uptime",
        "mountPoints",
        "elementDisplayName",
        "isIsolated",
        "lastSeenTimeStamp",
        "timeStampSinceLastConnectionTime"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "users",
              "logonSessions",
              "processes",
              "services",
              "drivers",
              "hostsFile",
              "mountPoints",
              "networkInterfaces",
              "removableDevices",
              "localNetworks",
              "clientInteractions",
              "serverInteractions"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Device Properties",
            "features": [
              "cpuCount",
              "totalDiskSpace",
              "totalMemory",
              "freeDiskSpace",
              "freeMemory",
              "isLaptop",
              "deviceModel"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "elementDisplayName",
              "osType",
              "osVersionType",
              "platformArchitecture",
              "hasMalops",
              "hasSuspicions",
              "isSuspiciousOrHasSuspiciousProcessOrFile"
            ]
          },
          {
            "groupName": "Machine Activity",
            "features": [
              "isIsolated",
              "isActiveProbeConnected",
              "uptime",
              "timeStampSinceLastConnectionTime"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "hasRemovableDevice",
              "elementDisplayName",
              "timezoneUTCOffsetMinutes",
              "mbrHashString",
              "osType",
              "osVersionType",
              "platformArchitecture",
              "domainFqdn"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "hasMalops",
              "maliciousProcesses",
              "hasSuspicions",
              "isSuspiciousOrHasSuspiciousProcessOrFile"
            ]
          },
          {
            "groupName": "Active Directory",
            "features": [
              "adCanonicalName",
              "adCompany",
              "adDNSHostName",
              "adDepartment",
              "adDescription",
              "adDisplayName",
              "adLocation",
              "adMachineRole",
              "adOU",
              "adOrganization",
              "adSid"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Sensor Properties",
            "features": [
              "isActiveProbeConnected",
              "lastSeenTimeStamp",
              "isIsolated",
              "uptime",
              "timeStampSinceLastConnectionTime",
              "timezoneUTCOffsetMinutes",
              "logonFileMissingTimestamp"
            ]
          },
          {
            "groupName": "Device Properties",
            "features": [
              "mountPoints",
              "platformArchitecture",
              "isLaptop",
              "hasRemovableDevice",
              "removableDevices",
              "cpuCount",
              "totalDiskSpace",
              "freeDiskSpace",
              "totalMemory",
              "freeMemory",
              "mbrHashString"
            ]
          },
          {
            "groupName": "Hierarchy",
            "features": [
              "self",
              "mountPoints"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "maliciousProcesses",
              "suspiciousProcesses",
              "maliciousTools"
            ]
          },
          {
            "groupName": "Suspicious Activity",
            "features": [
              "suspiciousProcesses",
              "logonFileMissingTimestamp"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "osType",
              "osVersionType",
              "domainFqdn",
              "deviceModel",
              "lastSeenTimeStamp",
              "uptime",
              "timezoneUTCOffsetMinutes",
              "pylumId",
              "networkInterfaces",
              "deviceModel"
            ]
          },
          {
            "groupName": "Active Directory",
            "features": [
              "adDisplayName",
              "adSid",
              "adCanonicalName",
              "adCompany",
              "adDNSHostName",
              "adDepartment",
              "adDescription",
              "adLocation",
              "adMachineRole",
              "adOrganization",
              "adOU"
            ]
          },
          {
            "groupName": "Collected Data",
            "features": [
              "users",
              "processes",
              "services",
              "drivers",
              "autoruns",
              "logonSessions"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "processes",
              "services",
              "mountPoints",
              "maliciousProcesses",
              "suspiciousProcesses"
            ]
          },
          {
            "groupName": "Machine Activity",
            "features": [
              "isIsolated",
              "isActiveProbeConnected",
              "lastSeenTimeStamp",
              "timeStampSinceLastConnectionTime",
              "uptime"
            ]
          },
          {
            "groupName": "Device Properites",
            "features": [
              "freeDiskSpace",
              "totalDiskSpace",
              "freeMemory",
              "totalMemory",
              "deviceModel",
              "cpuCount",
              "isLaptop"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "hasRemovableDevice",
              "timezoneUTCOffsetMinutes",
              "mbrHashString",
              "osVersionType",
              "osType",
              "platformArchitecture",
              "domainFqdn",
              "ownerOrganization",
              "pylumId"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "osVersionType",
              "platformArchitecture",
              "uptime",
              "isActiveProbeConnected",
              "lastSeenTimeStamp",
              "timeStampSinceLastConnectionTime",
              "mountPoints",
              "processes",
              "services",
              "logonSessions",
              "domainFqdn",
              "timezoneUTCOffsetMinutes"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "hasMalops",
              "hasSuspicions",
              "isSuspiciousOrHasSuspiciousProcessOrFile",
              "maliciousTools"
            ]
          },
          {
            "groupName": "Active Directory",
            "features": [
              "adSid",
              "adOU",
              "adOrganization",
              "adCanonicalName",
              "adCompany",
              "adDNSHostName",
              "adDepartment",
              "adDisplayName",
              "adLocation",
              "adMachineRole",
              "adDescription"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "osVersionType",
              "platformArchitecture",
              "uptime",
              "isActiveProbeConnected",
              "lastSeenTimeStamp",
              "timeStampSinceLastConnectionTime",
              "activeUsers",
              "mountPoints",
              "processes",
              "services"
            ]
          }
        ]
      }
    }
  },
  "MachinesInteraction": {
    "template": {
      "overview": [
        "interactionType",
        "interactionProtocol",
        "user",
        "elementDisplayName",
        "attackerTimestamp",
        "victimTimestamp",
        "clientProcess",
        "serverProcess",
        "clientUser",
        "serverUser",
        "clientMachine",
        "serverMachine",
        "clientMachineIp",
        "serverMachineIp",
        "clientMachinePort",
        "serverMachinePort",
        "minTime",
        "maxTime"
      ],
      "malop": [
        "interactionType",
        "interactionProtocol",
        "user",
        "elementDisplayName",
        "attackerTimestamp",
        "victimTimestamp",
        "clientProcess",
        "serverProcess",
        "clientUser",
        "serverUser",
        "clientMachine",
        "serverMachine",
        "clientMachineIp",
        "serverMachineIp",
        "clientMachinePort",
        "serverMachinePort",
        "minTime",
        "maxTime"
      ],
      "details": [
        "interactionType",
        "interactionProtocol",
        "user",
        "elementDisplayName",
        "attackerTimestamp",
        "victimTimestamp",
        "clientProcess",
        "serverProcess",
        "clientUser",
        "serverUser",
        "clientMachine",
        "serverMachine",
        "clientMachineIp",
        "serverMachineIp",
        "clientMachinePort",
        "serverMachinePort",
        "minTime",
        "maxTime",
        ""
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "user",
              "clientProcess",
              "serverProcess",
              "clientUser",
              "serverUser",
              "clientMachine",
              "serverMachine"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "interactionProtocol",
              "interactionRole",
              "clientMachinePort",
              "serverMachinePort"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "self"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "elementDisplayName",
              "clientProcess",
              "serverProcess",
              "clientMachineIp",
              "serverMachineIp",
              "clientMachinePort",
              "serverMachinePort"
            ]
          },
          {
            "groupName": "Links",
            "features": [
              "clientUser",
              "serverUser",
              "clientMachine",
              "serverMachine"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "interactionType",
              "interactionProtocol",
              "user",
              "elementDisplayName",
              "attackerTimestamp",
              "victimTimestamp"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "interactionType",
              "clientMachineIp",
              "serverMachineIp",
              "clientMachinePort",
              "serverMachinePort"
            ]
          },
          {
            "groupName": "Links",
            "features": [
              "clientMachine",
              "serverMachine"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "interactionProtocol",
              "attackerTimestamp",
              "victimTimestamp",
              "clientUser",
              "clientProcess",
              "serverUser",
              "serverProcess",
              "user"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "interactionType",
              "minTime",
              "maxTime",
              "interactionProtocol",
              "elementDisplayName",
              "attackerTimestamp",
              "victimTimestamp"
            ]
          }
        ]
      }
    }
  },
  "Proxy": {
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ipAddress",
              "host",
              "NetworkInterface.proxies"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "discoveryType",
              "elementDisplayName",
              "hasMalops",
              "hasSuspicions",
              "pacUrl",
              "port"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "discoveryType",
              "host",
              "ipAddress",
              "pacUrl",
              "port"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "host",
              "ipAddress"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "discoveryType",
              "pacUrl",
              "port"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "discoveryType",
              "host",
              "ipAddress",
              "pacUrl",
              "port"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "discoveryType",
              "host",
              "ipAddress",
              "pacUrl",
              "port"
            ]
          }
        ]
      }
    }
  },
  "AutomaticExecution": {
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Execution",
            "features": [
              "ownerMachine",
              "registry",
              "service",
              "scheduledTask"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "type"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "type"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self",
              "service",
              "registry",
              "scheduledTask"
            ]
          },
          {
            "groupName": "Execution",
            "features": [
              "service",
              "registry",
              "scheduledTask"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "type"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relations",
            "features": [
              "registry",
              "service",
              "scheduledTask"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "type"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "type",
              "registry",
              "service",
              "scheduledTask"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "type",
              "registry",
              "scheduledTask",
              "service"
            ]
          }
        ]
      }
    }
  },
  "WmiPersistentObject": {
    "template": {
      "overview": [
        "elementDisplayName",
        "filterName",
        "filterQuery",
        "consumerName",
        "consumerAction",
        "consumerFilePath",
        "consumerImageFile",
        "persistenceType",
        "scriptEngine",
        "clientNetworkMachine",
        "clientMachine",
        "clientIp",
        "clientPid"
      ],
      "details": [
        "elementDisplayName",
        "filterName",
        "filterQuery",
        "consumerName",
        "consumerAction",
        "consumerFilePath",
        "consumerImageFile",
        "persistenceType",
        "scriptEngine",
        "creatingProc",
        "clientNetworkMachine",
        "clientMachine",
        "clientIp",
        "clientPid"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "creatingProc",
              "clientMachine",
              "consumerImageFile"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "filterName",
              "filterQuery",
              "consumerName",
              "consumerAction"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "consumerFilePath",
              "consumerImageFile",
              "persistenceType",
              "scriptEngine"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "creatingProc",
              "clientPid",
              "filterName",
              "filterQuery",
              "consumerName",
              "consumerAction",
              "consumerFilePath",
              "consumerImageFile",
              "persistenceType",
              "scriptEngine",
              "clientMachine",
              "clientNetworkMachine",
              "clientIp"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "creatingProc",
              "clientPid",
              "filterName",
              "filterQuery",
              "consumerName",
              "consumerAction"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "consumerFilePath",
              "consumerImageFile",
              "persistenceType",
              "scriptEngine"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "filterName",
              "filterQuery",
              "consumerName",
              "consumerAction"
            ]
          }
        ]
      }
    }
  },
  "WmiQueryObject": {
    "template": {
      "overview": [
        "elementDisplayName",
        "queryTime",
        "query",
        "queryType",
        "clientNetworkMachine",
        "clientMachine",
        "clientIp",
        "clientPid"
      ],
      "details": [
        "elementDisplayName",
        "queryTime",
        "query",
        "queryType",
        "creatingProc",
        "clientNetworkMachine",
        "clientMachine",
        "clientIp",
        "clientPid"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "creatingProc",
              "clientMachine"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "queryTime",
              "query",
              "queryType"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "creatingProc",
              "clientPid",
              "queryTime",
              "query",
              "queryType",
              "clientMachine",
              "clientNetworkMachine",
              "clientIp"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "creatingProc",
              "clientPid",
              "queryTime",
              "query",
              "queryType"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "queryTime",
              "query",
              "queryType"
            ]
          }
        ]
      }
    }
  },
  "DetectionEvents": {
    "template": {
      "detection": [
        "detectionTime",
        "decisionStatus",
        "file",
        "detectionEngine",
        "detectionTime",
        "detectionValue"
      ],
      "detection_details": [
        "detectionEngine",
        "firstSeen",
        "detectionTime",
        "counter",
        "ownerMachine",
        "decisionStatus",
        "connection",
        "process",
        "file",
        "logonSession",
        "wasEverDetectedInScan",
        "wasEverDetectedByAccess",
        "payload",
        "self",
        "collaborationActivity",
        "emailMessage",
        "SIEMAuxData"
      ],
      "details": [
        "elementDisplayName",
        "detectionEngine",
        "decisionStatus",
        "detectionValueType",
        "counter"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "process",
              "user",
              "file"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "ownerMachine",
              "user",
              "process",
              "self"
            ]
          },
          {
            "groupName": "Process",
            "features": [
              "process",
              "process.calculatedName",
              "process.calculatedUser",
              "process.creationTime",
              "process.endTime",
              "process.imageFile.maliciousClassificationType"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "detectionValueType",
              "detectionValue",
              "detectionEngine",
              "scriptEngine",
              "decisionStatus"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "user",
              "process",
              "self"
            ]
          },
          {
            "groupName": "Xdr",
            "features": [
              "collaborationActivity",
              "emailMessage",
              "cloudAccessEvent"
            ]
          },
          {
            "groupName": "Process",
            "features": [
              "process",
              "process.calculatedName",
              "process.calculatedUser",
              "process.creationTime",
              "process.endTime",
              "process.commandLine",
              "process.imageFile.maliciousClassificationType"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "firstSeen",
              "detectionEngine",
              "rootCause",
              "decisionStatus",
              "scriptEngine",
              "detectionValue",
              "detectionValueType",
              "elementDisplayName",
              "msrpcRemoteIpAddress",
              "msrpcEventType",
              "counter"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Process",
            "features": [
              "process",
              "process.calculatedName",
              "process.calculatedUser",
              "process.creationTime",
              "process.endTime",
              "process.imageFile.maliciousClassificationType"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "detectionValueType",
              "detectionValue",
              "detectionEngine",
              "counter"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "detectionEngine",
              "decisionStatus",
              "detectionValue",
              "firstSeen",
              "process",
              "user",
              "ownerMachine",
              "counter"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "detectionEngine",
              "decisionStatus",
              "detectionValue",
              "firstSeen",
              "process",
              "user",
              "ownerMachine",
              "counter"
            ]
          }
        ]
      }
    }
  },
  "MalopDetectionEvents": {
    "template": {
      "overview": [
        "malopLastUpdateTime",
        "malopActivityTypes",
        "affectedMachines",
        "detectionType",
        "decisionFeature",
        "decisionStatuses",
        "iconBase64",
        "rootCauseElementTypes",
        "rootCauseElementNames",
        "rootCauseElementCompanyProduct",
        "creationTime",
        "malopLastActivityTime",
        "elementDisplayName"
      ],
      "detection": [
        "creationTime",
        "affectedMachines",
        "affectedUsers",
        "malopActivityTypes",
        "decisionFeatureSet",
        "decisionFeature",
        "detectionEngines",
        "detectionType",
        "malopLastUpdateTime",
        "elementDisplayName",
        "rootCauseElementNames",
        "rootCauseElementTypes",
        "rootCauseElementHashes",
        "primaryRootCauseElements",
        "rootCauseElements",
        "isBlocked",
        "hasActiveProcesses",
        "iconBase64",
        "detectionValueTypes",
        "detectionValues",
        "decisionStatuses",
        "malopLastActivityTime",
        "filesToRemediate",
        "group"
      ],
      "detection_details": [
        "creationTime",
        "affectedMachines",
        "affectedUsers",
        "malopActivityTypes",
        "decisionFeatureSet",
        "decisionFeature",
        "detectionEngines",
        "malopLastUpdateTime",
        "elementDisplayName",
        "rootCauseElementNames",
        "rootCauseElementTypes",
        "rootCauseElementHashes",
        "rootCauseElements",
        "primaryRootCauseElements",
        "scriptDetectionTypes",
        "isBlocked",
        "hasActiveProcesses",
        "iconBase64",
        "signers",
        "fileClassificationTypes",
        "filePaths",
        "commandLines",
        "decodedCommandLines",
        "detectionValues",
        "detectionValueTypes",
        "detectionType",
        "decisionStatuses",
        "processesToRemediate",
        "activeProcessesCount",
        "malopLastActivityTime",
        "hasAnyScanEvent",
        "filesToRemediate",
        "exploitDetectionTypes"
      ],
      "malop": [
        "malopLastUpdateTime",
        "malopActivityTypes",
        "affectedMachines",
        "detectionType",
        "decisionFeature",
        "iconBase64",
        "rootCauseElementTypes",
        "rootCauseElementNames",
        "rootCauseElementCompanyProduct",
        "creationTime",
        "malopLastActivityTime",
        "elementDisplayName"
      ]
    }
  },
  "Connection": {
    "template": {
      "overview": [
        "elementDisplayName",
        "remoteAddress",
        "ownerMachine",
        "ownerProcess",
        "localPort",
        "remotePort",
        "isIncoming",
        "isExternalConnection",
        "state",
        "transportProtocol",
        "portType",
        "portDescription",
        "receivedBytesCount",
        "transmittedBytesCount",
        "calculatedCreationTime",
        "endTime",
        "ownerProcess.user"
      ],
      "detection_details": [
        "direction",
        "serverAddress",
        "serverPort",
        "portType",
        "aggregatedReceivedBytesCount",
        "aggregatedTransmittedBytesCount",
        "remoteAddressCountryName",
        "remoteAddress",
        "hasSuspicions",
        "ownerMachine",
        "ownerProcess",
        "dnsQuery",
        "calculatedCreationTime",
        "endTime",
        "elementDisplayName"
      ],
      "malop": [
        "elementDisplayName",
        "self",
        "remoteAddress",
        "ownerMachine",
        "ownerProcess",
        "localPort",
        "remotePort",
        "isIncoming",
        "isExternalConnection",
        "state",
        "transportProtocol",
        "portType",
        "portDescription",
        "receivedBytesCount",
        "transmittedBytesCount",
        "creationTime",
        "endTime",
        "remoteAddressCountryName",
        "ownerProcess.user",
        "isLiveProcess"
      ],
      "details": [
        "isWellKnownPort",
        "transmittedBytesCount",
        "calculatedCreationTime",
        "ownerProcess",
        "remoteDnsEntry",
        "portType",
        "transportProtocol",
        "remoteAddress",
        "remoteAddressCountryName",
        "localAddress",
        "ownerMachine",
        "relatedToMalop",
        "serverAddress",
        "domainName",
        "isProcessMalware",
        "remoteMachine",
        "endTime",
        "isSuspicious",
        "direction",
        "isProcessLegit",
        "dnsQuery",
        "remoteAddressInternalExternalLocal",
        "state",
        "parent",
        "elementDisplayName",
        "ownerProcess.imageFile.maliciousClassificationType",
        "ownerProcess.imageFile.productType",
        "ownerProcess.imageFile.companyName",
        "ownerProcess.imageFile.productName",
        "ownerProcess.creationTime",
        "ownerProcess.endTime",
        "ownerProcess.calculatedUser",
        "ownerProcess.imageFile.isSigned",
        "ownerProcess.imageFile.signatureVerified",
        "ownerMachine.isActiveProbeConnected",
        "ownerMachine.osVersionType",
        "ownerMachine.isSuspiciousOrHasSuspiciousProcessOrFile"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "localAddress",
              "remoteAddress",
              "ownerMachine",
              "ownerProcess",
              "dnsQuery",
              "ListeningConnection.connections",
              "Process.connections",
              "urlDomains"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "elementDisplayName",
              "direction",
              "serverAddress",
              "serverPort",
              "portType",
              "hasMalops",
              "hasSuspicions",
              "isExternalConnection",
              "isSuspicious",
              "isProcessLegit",
              "isProcessMalware",
              "remoteAddressCountryName"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "isExternalConnection",
              "isIncoming",
              "remoteAddressInternalExternalLocal",
              "connectionToTorAddressEvidence",
              "isWellKnownPort",
              "isProcessLegit"
            ]
          },
          {
            "groupName": "Malicious Activity - C&C Communication",
            "features": [
              "rareAddressInternalExternalLocalByProcessEvidence",
              "rareDirectionByProcessEvidence",
              "rarePortAddressByProcessEvidence",
              "rarePortByProcessEvidence",
              "rarePortTypeByProcessEvidence",
              "rareCountryByProcessEvidence",
              "lowAddressByMachineEvidence",
              "lowAddressByProcessEvidence",
              "lowAddressOnMachineByProcessRatioEvidence"
            ]
          },
          {
            "groupName": "Malicious Classification",
            "features": [
              "hasMalops",
              "hasSuspicions",
              "accessedByMalwareEvidence",
              "relatedToMalop",
              "maliciousAddressEvidence",
              "isProcessMalware",
              "isProcessMaliciousByHashEvidence",
              "rareAddressOnMachineEvidence",
              "rareAddressByProcessEvidence",
              "rareCountryByMachineEvidence",
              "isSuspicious"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "localAddress",
              "remoteAddress",
              "direction",
              "domainName",
              "localPort",
              "outgoingWithListeningConnectionEvidence",
              "portDescription",
              "portType",
              "remoteAddressCountryName",
              "remotePort",
              "serverAddress",
              "serverPort",
              "state",
              "dnsQuery",
              "aggregatedReceivedBytesCount",
              "aggregatedTransmittedBytesCount",
              "transportProtocol"
            ]
          },
          {
            "groupName": "Malicious Activity - Connections",
            "features": [
              "connectionToAddressUsedByMalwareSuspicion",
              "maliciousConnectionSuspicion",
              "externalConnectionOfMaliciousProcessByHashSuspicion",
              "absoluteHighDataVolumeTransmittedToMaliciousAddressSuspicion",
              "internalConnectionOfMaliciousProcessByHashSuspicion",
              "absoluteHighTransmittedBytesEvidence"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "maliciousClassificationTypeRemoteAddress",
              "maliciousClassificationTypeLocalAddress",
              "accessedByMalwaresOnlyRemote",
              "accessedByMalwaresOnlyLocal",
              "classificationCommentLocalAddress",
              "classificationCommentRemoteAddress"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "ownerProcess.calculatedUser",
              "ownerProcess",
              "localAddress",
              "self",
              "remoteAddress"
            ]
          },
          {
            "groupName": "Listening connection",
            "features": [
              "parent"
            ]
          },
          {
            "groupName": "DNS query",
            "features": [
              "dnsQuery",
              "urlDomains"
            ]
          },
          {
            "groupName": "Data transfer",
            "features": [
              "aggregatedTransmittedBytesCount",
              "aggregatedReceivedBytesCount"
            ]
          },
          {
            "groupName": "Process",
            "features": [
              "ownerProcess",
              "ownerProcess.calculatedName",
              "ownerProcess.calculatedUser",
              "ownerProcess.creationTime",
              "ownerProcess.endTime",
              "ownerProcess.imageFile.maliciousClassificationType"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "isProcessMalware",
              "isProcessLegit",
              "maliciousClassificationTypeRemoteAddress"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "localAddress",
              "remoteAddress",
              "remoteAddressInternalExternalLocal",
              "remoteMachine",
              "remoteAddressCountryName",
              "domainName",
              "transportProtocol",
              "direction",
              "state",
              "portType",
              "isWellKnownPort",
              "calculatedCreationTime",
              "endTime",
              "lastDetectEventDetectionStatus",
              "ipConnections"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "parent",
              "dnsQuery",
              "localAddress",
              "ownerMachine",
              "ownerProcess",
              "remoteAddress",
              "remoteDnsEntry",
              "remoteMachine",
              "urlDomains"
            ]
          },
          {
            "groupName": "Malicious Activity - C&C Communications",
            "features": [
              "rareAddressInternalExternalLocalByProcessEvidence",
              "rareDirectionByProcessEvidence",
              "rarePortAddressByProcessEvidence",
              "rarePortByProcessEvidence",
              "rarePortTypeByProcessEvidence",
              "rareCountryByProcessEvidence",
              "lowAddressByMachineEvidence",
              "lowAddressByProcessEvidence",
              "lowAddressOnMachineByProcessRatioEvidence"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "isExternalConnection",
              "isIncoming",
              "remoteAddressInternalExternalLocal",
              "transportProtocol",
              "outgoingWithListeningConnectionEvidence"
            ]
          },
          {
            "groupName": "Malicious Activity - Data transfer",
            "features": [
              "absoluteHighTransmittedBytesEvidence"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "calculatedCreationTime",
              "direction",
              "domainName",
              "endTime",
              "localPort",
              "portDescription",
              "portType",
              "remoteAddressCountryName",
              "remotePort",
              "serverAddress",
              "serverPort",
              "state",
              "aggregatedReceivedBytesCount",
              "aggregatedTransmittedBytesCount"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "direction",
              "ownerMachine",
              "ownerProcess",
              "serverPort",
              "serverAddress",
              "portType",
              "aggregatedReceivedBytesCount",
              "aggregatedTransmittedBytesCount",
              "remoteAddressCountryName",
              "dnsQuery",
              "accessedByMalwareEvidence"
            ]
          },
          {
            "groupName": "Malicious Activity",
            "features": [
              "hasMalops",
              "hasSuspicions",
              "accessedByMalwareEvidence",
              "relatedToMalop",
              "isWellKnownPort",
              "maliciousAddressEvidence",
              "isProcessLegit",
              "isProcessMalware",
              "isProcessMaliciousByHashEvidence",
              "rareAddressOnMachineEvidence",
              "rareAddressByProcessEvidence",
              "rareCountryByMachineEvidence",
              "isSuspicious"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "maliciousClassificationTypeRemoteAddress",
              "maliciousClassificationTypeLocalAddress",
              "accessedByMalwaresOnlyRemote",
              "accessedByMalwaresOnlyLocal",
              "classificationCommentLocalAddress",
              "classificationCommentRemoteAddress"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "direction",
              "serverAddress",
              "serverPort",
              "portType",
              "aggregatedReceivedBytesCount",
              "aggregatedTransmittedBytesCount",
              "remoteAddressCountryName",
              "accessedByMalwareEvidence",
              "ownerMachine",
              "ownerProcess",
              "dnsQuery",
              "maliciousClassificationTypeRemoteAddress",
              "maliciousClassificationTypeLocalAddress"
            ]
          }
        ]
      }
    }
  },
  "Service": {
    "template": {
      "overview": [
        "commandLineArguments",
        "parentProcess",
        "name",
        "startType",
        "binaryFile",
        "isActive",
        "description",
        "createdBy",
        "binaryFile.correctedPath",
        "binaryFile.sha1String",
        "binaryFile.isSigned",
        "binaryFile.signatureVerified",
        "binaryFile.companyName",
        "binaryFile.productName",
        "binaryFile.productType",
        "binaryFile.classificationLink",
        "binaryFile.maliciousClassificationType",
        "elementDisplayName"
      ],
      "details": [
        "commandLineArguments",
        "parentProcess",
        "name",
        "startType",
        "binaryFile",
        "isActive",
        "description",
        "createdBy",
        "binaryFile.correctedPath",
        "binaryFile.sha1String",
        "binaryFile.isSigned",
        "binaryFile.signatureVerified",
        "binaryFile.companyName",
        "binaryFile.productName",
        "binaryFile.productType",
        "binaryFile.classificationLink",
        "binaryFile.maliciousClassificationType",
        "elementDisplayName",
        "parentProcess.imageFile.maliciousClassificationType",
        "parentProcess.creationTime",
        "parentProcess.endTime",
        "parentProcess.calculatedUser",
        "ownerMachine.isActiveProbeConnected",
        "ownerMachine.osVersionType",
        "ownerMachine.isSuspiciousOrHasSuspiciousProcessOrFile"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "binaryFile",
              "process",
              "ownerMachine",
              "driver"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "description",
              "commandLineArguments",
              "isActive",
              "startType",
              "hasSuspicions",
              "rareServiceEvidence",
              "unitFilePath",
              "serviceSubState",
              "isAutoRestartService"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "newServiceEvidence",
              "rareServiceEvidence",
              "serviceType"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "commandLineArguments",
              "description",
              "name",
              "isActive",
              "elementDisplayName",
              "startType",
              "serviceStartName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "binaryFile",
              "self"
            ]
          },
          {
            "groupName": "Driver",
            "features": [
              "driver"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "hasSuspicions",
              "hasMalops"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "name",
              "description",
              "startType",
              "isActive",
              "isSystemProcess",
              "commandLineArguments",
              "serviceStartName",
              "unitFilePath",
              "serviceState",
              "serviceSubState",
              "isAutoRestartService",
              "serviceType",
              "createdBy"
            ]
          },
          {
            "groupName": "File",
            "features": [
              "binaryFile",
              "binaryFile.correctedPath",
              "binaryFile.sha1String",
              "binaryFile.md5String",
              "binaryFile.sha256String",
              "binaryFile.maliciousClassificationType",
              "binaryFile.productType",
              "binaryFile.companyName",
              "binaryFile.productName",
              "binaryFile.signedInternalOrExternal",
              "binaryFile.signatureVerified"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "binaryFile",
              "driver",
              "ownerMachine",
              "process",
              "createdBy"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "newServiceEvidence",
              "rareServiceEvidence",
              "serviceType"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "commandLineArguments",
              "description",
              "endTime",
              "isActive",
              "elementDisplayName",
              "startType",
              "unitFilePath",
              "serviceState",
              "serviceSubState",
              "isAutoRestartService"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "name",
              "description",
              "commandLineArguments",
              "binaryFile",
              "isActive",
              "startType",
              "ownerMachine",
              "process",
              "serviceStartName"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "name",
              "description",
              "commandLineArguments",
              "binaryFile",
              "isActive",
              "startType",
              "ownerMachine",
              "process",
              "parentProcess"
            ]
          }
        ]
      }
    }
  },
  "ScheduledTask": {
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "processes",
              "author",
              "lastUpdatedBy",
              "ownerMachine",
              "files"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "state",
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "state",
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "author",
              "self",
              "processes"
            ]
          },
          {
            "groupName": "Execution",
            "features": [
              "processes",
              "lastRunTime"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "enabled",
              "state",
              "author",
              "lastUpdatedBy",
              "createdBy"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relations",
            "features": [
              "processes",
              "author",
              "lastUpdatedBy",
              "createdBy"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "state",
              "lastRunTime"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "state",
              "lastRunTime",
              "processes",
              "author",
              "lastUpdatedBy"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "state",
              "lastRunTime",
              "processes",
              "executableActions",
              "author",
              "lastUpdatedBy"
            ]
          }
        ]
      }
    }
  },
  "RegistryEntry": {
    "template": {
      "overview": [
        "value",
        "key",
        "elementDisplayName"
      ],
      "details": [
        "value",
        "key",
        "elementDisplayName"
      ]
    },
    "investigation": {
      "GridColumns": {
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "key",
              "value",
              "ownerMachine",
              "endTime"
            ]
          }
        ]
      }
    }
  },
  "Autorun": {
    "template": {
      "overview": [
        "rareAutorunFileNameByOsEvidence",
        "endTime",
        "isPointingToTemp",
        "registryEntry",
        "autorunJavascriptValueSuspicion",
        "ownerMachine",
        "value",
        "dependInFile",
        "file",
        "elementDisplayName"
      ],
      "details": [
        "rareAutorunFileNameByOsEvidence",
        "endTime",
        "isPointingToTemp",
        "registryEntry",
        "autorunJavascriptValueSuspicion",
        "ownerMachine",
        "value",
        "dependInFile",
        "file",
        "elementDisplayName",
        "ownerMachine.isActiveProbeConnected",
        "ownerMachine.osVersionType",
        "ownerMachine.isSuspiciousOrHasSuspiciousProcessOrFile",
        "file.maliciousClassificationType",
        "file.productType",
        "file.companyName",
        "file.productName",
        "file.isSigned",
        "file.signatureVerified"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "dependInFile",
              "registryEvents"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Classification",
            "features": [
              "isPointingToTemp"
            ]
          },
          {
            "groupName": "Suspicions",
            "features": [
              "autorunJavascriptValueSuspicion"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "dependInFile",
              "ownerMachine",
              "elementDisplayName",
              "value"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Target file",
            "features": [
              "file",
              "file.maliciousClassificationType",
              "file.productType",
              "file.companyName",
              "file.productName",
              "file.isSigned",
              "file.signatureVerified"
            ]
          },
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self",
              "file"
            ]
          },
          {
            "groupName": "Registry events",
            "features": [
              "registryEvents"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "value",
              "isCLSID"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Classification",
            "features": [
              "isPointingToTemp"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "dependInFile",
              "elementDisplayName",
              "endTime",
              "ownerMachine",
              "value",
              "registryEntry"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "value",
              "dependInFile",
              "ownerMachine",
              "isPointingToTemp"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "name",
              "value",
              "dependInFile",
              "ownerMachine",
              "isPointingToTemp",
              "sourceType"
            ]
          },
          {
            "presetName": "BuiltIn1",
            "columnNames": [
              "name",
              "value"
            ]
          },
          {
            "presetName": "BuiltIn2",
            "columnNames": [
              "dependInFile",
              "ownerMachine",
              "isPointingToTemp",
              "sourceType"
            ]
          }
        ]
      }
    }
  },
  "HostsFile": {
    "template": {
      "overview": [
        "file",
        "ownerMachine",
        "elementDisplayName"
      ],
      "details": [
        "file",
        "ownerMachine",
        "elementDisplayName",
        "ownerMachine.isActiveProbeConnected",
        "ownerMachine.osVersionType",
        "ownerMachine.isSuspiciousOrHasSuspiciousProcessOrFile"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "file"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self",
              "file"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "File",
            "features": [
              "file"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "domainToIp",
              "domainToDomain",
              "file",
              "ownerMachine"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "file",
              "ownerMachine"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "file",
              "ownerMachine"
            ]
          }
        ]
      }
    }
  },
  "DnsQueryResolvedDomainToIp": {
    "template": {
      "overview": [
        "targetIpAddress",
        "lowMaxTtlEvidence",
        "nonDefaultResolverEvidence",
        "recordType",
        "ttlRange",
        "sourceDomain",
        "resolvers",
        "elementDisplayName"
      ],
      "details": [
        "targetIpAddress",
        "lowMaxTtlEvidence",
        "nonDefaultResolverEvidence",
        "recordType",
        "ttlRange",
        "sourceDomain",
        "resolvers",
        "elementDisplayName",
        "targetIpAddress.countryNameOrNotExternalType",
        "targetIpAddress.ownerMachine"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "sourceDomain",
              "targetIpAddress",
              "resolvers",
              "Connection.dnsQuery",
              "Process.resolvedDnsQueriesDomainToIp"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "lowMaxTtlEvidence",
              "nonDefaultResolverEvidence",
              "recordType",
              "elementDisplayName",
              "ttlRange"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Target IP address",
            "features": [
              "targetIpAddress",
              "targetIpAddress.countryNameOrNotExternalType",
              "targetIpAddress.ownerMachine"
            ]
          },
          {
            "groupName": "Hierarchy",
            "features": [
              "sourceDomain",
              "self",
              "targetIpAddress"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "sourceDomain.maliciousClassificationType"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "recordType",
              "ttlRange",
              "resolvers"
            ]
          },
          {
            "groupName": "Source domain",
            "features": [
              "sourceDomain",
              "sourceDomain.isInternalDomain"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "resolvers",
              "sourceDomain",
              "targetIpAddress"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "lowMaxTtlEvidence",
              "nonDefaultResolverEvidence",
              "recordType",
              "elementDisplayName",
              "ttlRange"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "lowMaxTtlEvidence",
              "nonDefaultResolverEvidence",
              "recordType",
              "ttlRange",
              "resolvers",
              "sourceDomain",
              "targetIpAddress"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "lowMaxTtlEvidence",
              "nonDefaultResolverEvidence",
              "recordType",
              "ttlRange",
              "resolvers",
              "sourceDomain",
              "targetIpAddress"
            ]
          }
        ]
      }
    }
  },
  "RemoteSession": {
    "template": {
      "malop": [
        "server",
        "user",
        "user.privileges",
        "authenticationProtocol",
        "resourceType",
        "firstSeenTime",
        "clientLogonSession",
        "clientLogonSession.user",
        "clientLogonSession.ownerMachine",
        "elementDisplayName",
        "self"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "clientMachine",
              "serverMachine",
              "user",
              "client",
              "clientLogonSession",
              "processes",
              "server",
              "serverLogonSession"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "clientMachine",
              "user",
              "clientLogonSession",
              "self",
              "server",
              "serverMachine"
            ]
          },
          {
            "groupName": "User",
            "features": [
              "user"
            ]
          },
          {
            "groupName": "Server",
            "features": [
              "server",
              "serverMachine",
              "serverLogonSession"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "isPassTheTicket"
            ]
          },
          {
            "groupName": "Processes",
            "features": [
              "processes"
            ]
          },
          {
            "groupName": "Client",
            "features": [
              "client",
              "clientMachine",
              "clientLogonSession"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "firstSeenTime",
              "resourceType",
              "authenticationProtocol"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "client",
              "clientLogonSession",
              "clientMachine",
              "processes",
              "server",
              "serverLogonSession",
              "serverMachine",
              "user"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "hasSuspicions",
              "client",
              "clientLogonSession",
              "clientMachine",
              "processes",
              "server",
              "serverLogonSession",
              "serverMachine"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "hasSuspicions",
              "client",
              "clientLogonSession",
              "clientMachine",
              "processes",
              "server",
              "serverLogonSession",
              "serverMachine"
            ]
          }
        ]
      }
    }
  },
  "MalopLogonSession": {
    "template": {
      "overview": [
        "rootCauseElementTypes",
        "rootCauseElementNames",
        "rootCauseElementDomains",
        "creationTime",
        "affectedMachines",
        "affectedUsers",
        "detectionType",
        "malopActivityTypes",
        "decisionFeature",
        "malopStartTime",
        "malopLastUpdateTime",
        "elementDisplayName"
      ],
      "detection": [
        "rootCauseElementTypes",
        "rootCauseElementNames",
        "rootCauseElementDomains",
        "rootCauseElements",
        "creationTime",
        "affectedMachines",
        "affectedUsers",
        "detectionType",
        "malopActivityTypes",
        "decisionFeatureSet",
        "malopLastUpdateTime",
        "elementDisplayName",
        "group"
      ],
      "malop": [
        "rootCauseElementTypes",
        "rootCauseElementNames",
        "rootCauseElementDomains",
        "rootCauseElements",
        "creationTime",
        "affectedMachines",
        "affectedUsers",
        "detectionType",
        "malopActivityTypes",
        "decisionFeature",
        "malopStartTime",
        "malopLastUpdateTime",
        "elementDisplayName"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "affectedMachines",
              "affectedUsers",
              "suspects"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "self"
            ]
          },
          {
            "groupName": "User",
            "features": [
              "rootCauseElements",
              "affectedUsers"
            ]
          },
          {
            "groupName": "Characteristics",
            "features": [
              "malopStartTime",
              "malopLastUpdateTime"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "creationTime",
              "endTime",
              "decisionFeature",
              "detectionType",
              "primaryMalopType",
              "malopActivityTypes"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "affectedMachines"
            ]
          },
          {
            "groupName": "Logon session",
            "features": [
              "suspects"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "affectedMachines",
              "affectedUsers",
              "newSuspects",
              "suspectsFeatureCollection",
              "suspects"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "affectedMachines",
              "affectedUsers",
              "rootCauseElements",
              "suspects"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "affectedMachines",
              "affectedUsers",
              "suspects"
            ]
          }
        ]
      }
    }
  },
  "IpAddress": {
    "template": {
      "overview": [
        "isGateway",
        "addressReputation",
        "countryCode",
        "accessedByMalwaresOnly",
        "region",
        "version",
        "countryNameOrNotExternalType",
        "dhcpServerOfInterfaces",
        "elementDisplayName",
        "longitude",
        "ownerMachine",
        "isDhcpServer",
        "latitude",
        "ipReputationSource",
        "city",
        "gatewayOfInterfaces",
        "elementDisplayName"
      ],
      "malop": [
        "elementDisplayName",
        "maliciousClassificationType"
      ],
      "details": [
        "isGateway",
        "addressReputation",
        "countryCode",
        "accessedByMalwaresOnly",
        "region",
        "version",
        "countryNameOrNotExternalType",
        "dhcpServerOfInterfaces",
        "elementDisplayName",
        "longitude",
        "ownerMachine",
        "isDhcpServer",
        "latitude",
        "ipReputationSource",
        "city",
        "gatewayOfInterfaces",
        "elementDisplayName",
        "ownerMachine.isActiveProbeConnected",
        "ownerMachine.osVersionType",
        "ownerMachine.isSuspiciousOrHasSuspiciousProcessOrFile"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links - DNS",
            "features": [
              "DnsQueryResolvedDomainToIp.targetIpAddress",
              "DnsQueryResolvedIpToDomain.sourceIpAddress",
              "DnsQueryUnresolvedFromIp.sourceIpAddress"
            ]
          },
          {
            "groupName": "Links",
            "features": [
              "Connection.localAddress",
              "Connection.remoteAddress",
              "ownerMachine",
              "dhcpServerOfInterfaces",
              "gatewayOfInterfaces"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Geolocation",
            "features": [
              "city",
              "countryCode",
              "countryNameOrNotExternalType",
              "latitude",
              "longitude",
              "region"
            ]
          },
          {
            "groupName": "Recommended",
            "features": [
              "elementDisplayName",
              "hasSuspicions",
              "countryNameOrNotExternalType",
              "accessedByMalwaresOnly"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "maliciousClassificationType",
              "isGateway",
              "isDhcpServer",
              "classificationComment"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "ipReputationSource",
              "accessedByMalwaresOnly",
              "maliciousClassificationType"
            ]
          },
          {
            "groupName": "Suspicions",
            "features": [
              "ipAddressReputationSuspicion"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "version"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "self"
            ]
          },
          {
            "groupName": "Geolocation",
            "features": [
              "countryNameOrNotExternalType",
              "countryCode",
              "city",
              "region",
              "longitude",
              "latitude"
            ]
          },
          {
            "groupName": "Characteristics",
            "features": [
              "isGateway",
              "gatewayOfInterfaces",
              "isDhcpServer",
              "dhcpServerOfInterfaces"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "addressReputation",
              "ipReputationSource",
              "accessedByMalwaresOnly",
              "maliciousClassificationType"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "address",
              "version"
            ]
          },
          {
            "groupName": "Machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "ownerMachine",
              "dhcpServerOfInterfaces",
              "gatewayOfInterfaces"
            ]
          },
          {
            "groupName": "Geolocation",
            "features": [
              "city",
              "countryCode",
              "countryNameOrNotExternalType",
              "latitude",
              "longitude",
              "region"
            ]
          },
          {
            "groupName": "Classification",
            "features": [
              "isGateway",
              "isDhcpServer",
              "classificationComment"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "ipReputationSource",
              "accessedByMalwaresOnly",
              "maliciousClassificationType"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "version"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "addressReputation",
              "accessedByMalwaresOnly",
              "ownerMachine",
              "countryNameOrNotExternalType",
              "region",
              "city"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "maliciousClassificationType",
              "accessedByMalwaresOnly",
              "ownerMachine",
              "countryNameOrNotExternalType",
              "region",
              "city"
            ]
          }
        ]
      }
    }
  },
  "LogonSession": {
    "template": {
      "malop": [
        "remoteMachine",
        "ownerMachine",
        "user",
        "self",
        "processes",
        "creationTime",
        "endTime",
        "elementDisplayName",
        "passTheHashMalop",
        "passTheTicketMalop"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "user",
              "processes",
              "remoteMachine",
              "sourceIp"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Malops",
            "features": [
              "passTheHashMalop"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions",
              "passTheHashSuspicion"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "logonType",
              "logonApplication"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "user",
              "remoteMachine",
              "ownerMachine",
              "self",
              "processes"
            ]
          },
          {
            "groupName": "User",
            "features": [
              "user",
              "user.privileges",
              "user.domain",
              "user.isLocalSystem",
              "user.isAdmin"
            ]
          },
          {
            "groupName": "Local machine",
            "features": [
              "ownerMachine",
              "ownerMachine.isActiveProbeConnected",
              "ownerMachine.osVersionType"
            ]
          },
          {
            "groupName": "Remote machine",
            "features": [
              "remoteMachine",
              "remoteNetworkMachine",
              "sourceIp",
              "remoteMachine.isActiveProbeConnected",
              "remoteMachine.osVersionType"
            ]
          },
          {
            "groupName": "Reputation",
            "features": [
              "hasSuspicions",
              "hasMalops"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "creationTime",
              "lastSeenTime",
              "logonType",
              "logonApplication",
              "endTime"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Relationships",
            "features": [
              "ownerMachine",
              "remoteMachine",
              "user",
              "processes",
              "sourceIp"
            ]
          },
          {
            "groupName": "Detected activity",
            "features": [
              "hasSuspicions"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "creationTime",
              "lastSeenTime",
              "logonType",
              "logonApplication"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "processes",
              "ownerMachine",
              "user",
              "remoteMachine",
              "logonType",
              "creationTime",
              "lastSeenTime"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "processes",
              "ownerMachine",
              "user",
              "remoteMachine",
              "logonType",
              "creationTime"
            ]
          }
        ]
      }
    }
  },
  "LdapQuery": {
    "template": {
      "overview": [
        "creationTimestamp",
        "aggEventCounter",
        "lastSeenTimeStamp",
        "process",
        "attributeList",
        "distinguishedName",
        "scopeOfSearch",
        "elementDisplayName"
      ],
      "details": [
        "elementDisplayName",
        "creationTimestamp",
        "aggEventCounter",
        "lastSeenTimeStamp",
        "process",
        "attributeList",
        "distinguishedName",
        "scopeOfSearch"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "ownerMachine",
              "process"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "process"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "aggEventCounter",
              "lastSeenTimeStamp",
              "attributeList",
              "distinguishedName",
              "scopeOfSearch"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "ownerMachine",
              "process",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "creationTimestamp",
              "aggEventCounter",
              "lastSeenTimeStamp",
              "attributeList",
              "distinguishedName",
              "scopeOfSearch"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "process",
              "creationTimestamp",
              "lastSeenTimeStamp",
              "attributeList",
              "distinguishedName",
              "aggEventCounter",
              "scopeOfSearch"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "process",
              "creationTimestamp",
              "attributeList",
              "distinguishedName",
              "scopeOfSearch"
            ]
          }
        ]
      }
    }
  },
  "ForensicArtifacts": {
    "template": {
      "overview": [
        "process",
        "self",
        "executableFileName",
        "executableFullPath",
        "firstRuntime",
        "lastRuntime",
        "numberOfRuns",
        "sourceFullPath",
        "type",
        "collectorMetadata",
        "collectionTime"
      ],
      "details": [
        "elementDisplayName",
        "executableFileName",
        "executableFullPath",
        "firstRuntime",
        "lastRuntime",
        "numberOfRuns",
        "sourceFullPath",
        "type",
        "collectorMetadata",
        "collectionTime"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "process"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "process",
              "elementDisplayName",
              "executableFileName",
              "executableFullPath",
              "firstRuntime",
              "lastRuntime",
              "numberOfRuns",
              "sourceFullPath",
              "type",
              "collectorMetadata",
              "collectionTime"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "executableFileName",
              "executableFullPath",
              "firstRuntime",
              "lastRuntime",
              "numberOfRuns",
              "sourceFullPath",
              "type",
              "collectorMetadata",
              "collectionTime"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "process",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "executableFileName",
              "executableFullPath",
              "firstRuntime",
              "lastRuntime",
              "numberOfRuns"
            ]
          },
          {
            "groupName": "Details",
            "features": [
              "sourceFullPath",
              "type",
              "collectorMetadata",
              "collectionTime"
            ]
          },
          {
            "groupName": "Process",
            "features": [
              "process"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "executableFileName",
              "executableFullPath",
              "firstRuntime",
              "lastRuntime",
              "numberOfRuns",
              "sourceFullPath",
              "type",
              "collectorMetadata",
              "collectionTime"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "executableFileName",
              "executableFullPath",
              "firstRuntime",
              "lastRuntime",
              "numberOfRuns",
              "sourceFullPath",
              "type",
              "collectorMetadata",
              "collectionTime",
              "process"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "executableFileName",
              "executableFullPath",
              "firstRuntime",
              "lastRuntime",
              "numberOfRuns",
              "sourceFullPath",
              "type",
              "collectorMetadata",
              "collectionTime",
              "process"
            ]
          }
        ]
      }
    }
  },
  "Pattern": {
    "template": {
      "overview": [
        "elementDisplayName",
        "name"
      ],
      "detection": [
        "elementDisplayName",
        "name"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "contents"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "contents"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "name"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "contents",
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "name"
            ]
          },
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "name"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "name"
            ]
          }
        ]
      }
    }
  },
  "Content": {
    "template": {
      "overview": [
        "elementDisplayName",
        "size",
        "source",
        "patterns",
        "sha256HexString",
        "payload"
      ],
      "detection": [
        "elementDisplayName",
        "size",
        "source",
        "patterns",
        "sha256HexString",
        "payload"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": [
              "patterns",
              "process",
              "files"
            ]
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "process",
              "self",
              "size"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "source",
              "patterns",
              "sha256HexString"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "process",
              "self",
              "patterns"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "size",
              "source",
              "patterns",
              "sha256HexString",
              "payload"
            ]
          },
          {
            "groupName": "Process",
            "features": [
              "process"
            ]
          },
          {
            "groupName": "File",
            "features": [
              "files"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "sha256HexString",
              "size",
              "source",
              "payload"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "sha256HexString",
              "size",
              "source",
              "payload"
            ]
          }
        ]
      }
    }
  },
  "IODeviceInfo": {
    "template": {
      "overview": [
        "elementDisplayName",
        "ioDeviceType",
        "remoteAddress",
        "remotePort"
      ],
      "detection": [
        "elementDisplayName",
        "ioDeviceType",
        "remoteAddress",
        "remotePort"
      ]
    },
    "investigation": {
      "VisualQuery": {
        "configurationModel": [
          {
            "groupName": "Links",
            "features": []
          }
        ]
      },
      "GridFilters": {
        "configurationModel": [
          {
            "groupName": "Recommended",
            "features": [
              "self",
              "elementDisplayName",
              "ioDeviceType",
              "remoteAddress",
              "remotePort"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName"
            ]
          }
        ]
      },
      "ElementDetails": {
        "configurationModel": [
          {
            "groupName": "Hierarchy",
            "features": [
              "self"
            ]
          },
          {
            "groupName": "Properties",
            "features": [
              "elementDisplayName",
              "ioDeviceType",
              "remoteAddress",
              "remotePort"
            ]
          }
        ]
      },
      "GridColumns": {
        "configurationModel": [
          {
            "groupName": "Default",
            "features": [
              "elementDisplayName",
              "ioDeviceType",
              "remoteAddress",
              "remotePort"
            ]
          }
        ],
        "presets": [
          {
            "presetName": "Default",
            "columnNames": [
              "elementDisplayName",
              "ioDeviceType",
              "remoteAddress",
              "remotePort"
            ]
          }
        ]
      }
    }
  }
}
```
