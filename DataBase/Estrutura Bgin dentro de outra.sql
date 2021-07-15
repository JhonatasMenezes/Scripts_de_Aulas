DECLARE
  V_EMAIL employees.email%TYPE; 
  V_EMP_ID employees.employee_id%TYPE:=&ID;

  V_DPT departments.department_name%TYPE;
  V_DPT_ID departments.department_id%TYPE;
BEGIN

SELECT EMAIL, DEPARTMENT_ID
INTO V_EMAIL, V_DPT_ID
FROM EMPLOYEES
WHERE EMPLOYEE_ID = V_EMP_ID;

dbms_output.put_line(V_EMAIL);

    BEGIN
    SELECT DEPARTMENT_NAME
    INTO V_DPT
    FROM DEPARTMENTS
    WHERE department_id = v_dpt_id;
    
    dbms_output.put_line(V_DPT);
    EXCEPTION WHEN OTHERS THEN
    dbms_output.put_line(SQLERRM||' - '|| 'SEGUNDO');
    END;
    
EXCEPTION WHEN OTHERS THEN
dbms_output.put_line(SQLERRM||' - '|| 'PRIMEIRO');

    
END;