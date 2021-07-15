DECLARE 
V_ID locations.location_id%TYPE:=&ID;
V_STREET locations.street_address%TYPE:='&STREET';
V_POST_COD locations.postal_code%TYPE:='&POSTCOD';
V_CITY locations.city%TYPE:='&CITY';
V_STATE locations.state_province%TYPE:='&STATE';
V_COUNTRY locations.country_id%TYPE:='&COUNTRY';

BEGIN
INSERT INTO 
LOCATIONS 
VALUES (V_ID, V_STREET, V_POST_COD,
        V_CITY, V_STATE,V_COUNTRY);

DBMS_OUTPUT.put_line('LOCATION INSERIDO COM SUCESSO '||' '||V_ID);

EXCEPTION WHEN OTHERS THEN
dbms_output.put_line(SQLERRM);

END;
 
 --   --   --   --    --   --   --
 
SELECT * FROM LOCATIONS
WHERE location_id=900;

DESCRIBE LOCATIONS;