CREATE OR REPLACE FUNCTION FCT_VALID_DEPTO
(P_DEPTO IN departments.department_id%TYPE) RETURN NUMBER
IS
V_RESULT NUMBER;

BEGIN

SELECT COUNT (1)
INTO V_RESULT
FROM departments
WHERE department_id = P_DEPTO;

RETURN (V_RESULT);


END;

