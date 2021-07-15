DECLARE
V_DEP_NAME departments.department_name%TYPE;
V_MANG_ID departments.manager_id%TYPE;
V_DEP_ID departments.department_id%TYPE:=&ID; --TORNAND
-- A CONDIÇÃO WHERE VARIÁVEL
BEGIN

SELECT DEPARTMENT_NAME, MANAGER_ID
INTO V_DEP_NAME, V_MANG_ID
FROM departments
WHERE department_id=v_DEP_ID;

DBMS_OUTPUT.put_line(V_DEP_NAME||' - '||
                     V_MANG_ID);
-- EXCEPTION

END;