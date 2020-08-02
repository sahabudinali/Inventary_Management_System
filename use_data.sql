BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "use_data" (
	"ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Refrences"	TEXT,
	"Parts_Name"	TEXT,
	"MinArea"	NUMERIC,
	"MaxArea"	NUMERIC,
	"NumberOfHoles"	NUMERIC,
	"MinDiameter"	NUMERIC,
	"MaxDiameter"	NUMERIC,
	"Count"	NUMERIC
);
INSERT INTO "use_data" ("ID","Refrences","Parts_Name","MinArea","MaxArea","NumberOfHoles","MinDiameter","MaxDiameter","Count") VALUES (1,'W482','Washer',2898,2984,1,204.5,207.6,3),
 (2,'M142','Mount',3421,4587,1,201.2,223,4),
 (3,'B737','Bolt',2442,3254,4,45,56,4),
 (4,'W987','Washer',2442,3421,5,45.25,56.88,3),
 (5,'C345','Mount',7865,8654,3,345.23,450.2,7),
 (6,'A893','Bolt',3454,4442,1,435.2,435.5,5),
 (7,'B223','Washer',3443,4321,3,345.23,542,7),
 (8,'D343','Bolt',3421,4522,6,45,54,5),
 (9,'F232','Washer',1244,4323,7,65,456,5),
 (10,'B334','Mount',5845,6743,8,453,225,9),
 (11,'C244','Bolt',4584,5643,0,76,89,4),
 (12,'B977','Washer',5656,7657,7,54.2,62.5,5),
 (13,'E234','Mount',3455,5463,0,86,93,5),
 (14,'A764','Washer',3455,6545,5,43,64,5),
 (15,'V433','Mount',4645,6545,3,54,85,3);
COMMIT;
