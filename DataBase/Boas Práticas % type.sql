-- BOA R�TICA PREVININDO MANUTEN��ES NAS TABELAS
-- PARA N.�O PRECISAR DAR MANUTEN��O NOS PROGRAMAS
DECLARE
V_FIRST employees.first_name%TYPE;
V_LAST  employees.last_name%TYPE;
BEGIN

SELECT FIRST_NAME, LAST_NAME
INTO V_FIRST, V_LAST
FROM employees
WHERE employee_id=100;

DBMS_OUTPUT.put_line(v_first ||' - ' ||
                     v_last);
-- EXCEPTION
END;