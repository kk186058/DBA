WITH RECURSIVE All_databases
(Depth
,DatabaseNameI
,DatabaseId
,OwnerId

,PasswordModTime
,ProtectionType
,JournalFlag
,PermSpace
,SpoolSpace
,StartupString
,CommentString
,AccountName
,CreatorName
,DatabaseName
,JournalId
,Version
,OwnerName
,NumFallBackTables
,NumLogProtTables
,DefaultDataBase
,LogonRules
,AccLogRules
,AccLogUsrRules
,DefaultCollation
,RowType
,PasswordChgDate
,LockedDate
,LockedTime
,LockedCount
,UnResolvedRICount
,TimeZoneHour
,TimeZoneMinute
,DefaultDateForm
,CreateUID
,CreateTimeStamp
,LastAlterUID
,LastAlterTimeStamp
,TempSpace
,LastAccessTimeStamp
,AccessCount
,DefaultCharType
,RoleName
,ProfileName
,UDFLibRevision
,AppCat1Revision
,AppCat2Revision
,AppCat3Revision
,AppCat4Revision
,JarLibRevision
,TimeZoneString
,CalendarName
,ExportDefinitionName
,ExportWidthRuleSet
,NetCompression
,NetConfidentiality
,NetPolicyLevel
,ZoneID
,DBA
,DefaultMapNo
,MapOverride
,GPLLibRevision
,NewFlag

,SoftLimitPercent
,PermSkewLimit
,SpoolSkewLimit
,TempSkewLimit
,SpaceMapNo
,ExtraField1
,ExtraField2
,ExtraField3
,ExtraField4
,ExtraField5
,ExtraNVP
) AS
(
SELECT 
0 AS depth
,DatabaseNameI
,DatabaseId
,OwnerId

,PasswordModTime
,ProtectionType
,JournalFlag
,Cast(Cast(permspace AS BIGINT) AS VARCHAR(1000))
,Cast(Cast(spoolspace AS BIGINT) AS VARCHAR(1000))
,StartupString
,CommentString
,AccountName
,CreatorName
,DatabaseName
,JournalId
,Version
,OwnerName
,NumFallBackTables
,NumLogProtTables
,DefaultDataBase
,LogonRules
,AccLogRules
,AccLogUsrRules
,DefaultCollation
,RowType
,PasswordChgDate
,LockedDate
,LockedTime
,LockedCount
,UnResolvedRICount
,TimeZoneHour
,TimeZoneMinute
,DefaultDateForm
,CreateUID
,CreateTimeStamp
,LastAlterUID
,LastAlterTimeStamp
,Cast(Cast(db.tempspace AS BIGINT) AS VARCHAR(1000))
,LastAccessTimeStamp
,AccessCount
,DefaultCharType
,RoleName
,ProfileName
,UDFLibRevision
,AppCat1Revision
,AppCat2Revision
,AppCat3Revision
,AppCat4Revision
,JarLibRevision
,TimeZoneString
,CalendarName
,ExportDefinitionName
,ExportWidthRuleSet
,NetCompression
,NetConfidentiality
,NetPolicyLevel
,ZoneID
,DBA
,DefaultMapNo
,MapOverride
,GPLLibRevision
,NewFlag

,SoftLimitPercent
,PermSkewLimit
,SpoolSkewLimit
,TempSkewLimit
,SpaceMapNo
,ExtraField1
,ExtraField2
,ExtraField3
,ExtraField4
,ExtraField5
,ExtraNVP

FROM dbc.dbase db

WHERE db.DatabaseNameI = '${DATABASE}'
UNION ALL
SELECT  
  depth+1
, db.DatabaseNameI
, db.DatabaseId
, db.OwnerId

, db.PasswordModTime
, db.ProtectionType
, db.JournalFlag
, Cast(Cast(db.permspace AS BIGINT) AS VARCHAR(1000))
, Cast(Cast(db.spoolspace AS BIGINT) AS VARCHAR(1000))
, db.StartupString
, db.CommentString
, db.AccountName
, db.CreatorName
, db.DatabaseName
, db.JournalId
, db.Version
, db.OwnerName
, db.NumFallBackTables
, db.NumLogProtTables
, db.DefaultDataBase
, db.LogonRules
, db.AccLogRules
, db.AccLogUsrRules
, db.DefaultCollation
, db.RowType
, db.PasswordChgDate
, db.LockedDate
, db.LockedTime
, db.LockedCount
, db.UnResolvedRICount
, db.TimeZoneHour
, db.TimeZoneMinute
, db.DefaultDateForm
, db.CreateUID
, db.CreateTimeStamp
, db.LastAlterUID
, db.LastAlterTimeStamp
, Cast(Cast(db.tempspace AS BIGINT) AS VARCHAR(1000))
, db.LastAccessTimeStamp
, db.AccessCount
, db.DefaultCharType
, db.RoleName
, db.ProfileName
, db.UDFLibRevision
, db.AppCat1Revision
, db.AppCat2Revision
, db.AppCat3Revision
, db.AppCat4Revision
, db.JarLibRevision
, db.TimeZoneString
, db.CalendarName
, db.ExportDefinitionName
, db.ExportWidthRuleSet
, db.NetCompression
, db.NetConfidentiality
, db.NetPolicyLevel
, db.ZoneID
, db.DBA
, db.DefaultMapNo
, db.MapOverride
, db.GPLLibRevision
, db.NewFlag

, db.SoftLimitPercent
, db.PermSkewLimit
, db.SpoolSkewLimit
, db.TempSkewLimit
, db.SpaceMapNo
, db.ExtraField1
, db.ExtraField2
, db.ExtraField3
, db.ExtraField4
, db.ExtraField5
, db.ExtraNVP

		
FROM All_databases INNER JOIN  dbc.dbase db
ON   All_databases.DatabaseNameI = db .ownername
AND  All_databases.Depth < 15

)
SELECT DISTINCT * FROM All_databases
order by depth, DatabaseNameI
;



