DECLARE 
V_ID departments.department_id%TYPE:=&ID;
V_NOME departments.department_name%TYPE:='&NOME';
V_MANAGER departments.manager_id%TYPE:=&MAN;
V_LOCATION departments.location_id%TYPE:=&LOC;

BEGIN
INSERT INTO DEPARTMENTS
VALUES (V_ID,V_NOME,
             V_MANAGER, V_LOCATION);

DBMS_OUTPUT.put_line('DEPTO INSERIDO COM SUCESSO '||' '||V_ID
);

EXCEPTION WHEN OTHERS THEN
dbms_output.put_line(SQLERRM);

END;

SELECT * FROM DEPARTMENTS
WHERE department_id=990;