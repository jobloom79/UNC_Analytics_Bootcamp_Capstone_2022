CREATE TABLE Borrelia_burgdorferi_sensu_stricto_Data_Source(
	
  FIPS_Code INT NOT NULL,
  State VARCHAR NOT NULL,
  County VARCHAR NOT NULL,
  Borrelia_burgdorferi_sensu_stricto_County_Status VARCHAR NOT NULL,
  Borrelia_burgdorferi_sensu_stricto_Data_Source VARCHAR NOT NULL,
  Borrelia_mayonii_County_Status VARCHAR NOT NULL, 
	Borrelia_mayonii_Data_Source VARCHAR NOT NULL
);

SELECT * FROM Borrelia_burgdorferi_sensu_stricto_Data_Source;