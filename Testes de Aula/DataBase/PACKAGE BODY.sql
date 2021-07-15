CREATE OR REPLACE PACKAGE BODY PKG_RH AS

PROCEDURE add_job_history
  (  p_emp_id          job_history.employee_id%type
   , p_start_date      job_history.start_date%type
   , p_end_date        job_history.end_date%type
   , p_job_id          job_history.job_id%type
   , p_department_id   job_history.department_id%type
   )
IS
BEGIN
  INSERT INTO job_history (employee_id, start_date, end_date,
                           job_id, department_id)
    VALUES(p_emp_id, p_start_date, p_end_date, p_job_id, p_department_id);
END add_job_history;

PROCEDURE PRC_CONS_DEPTO
(P_ID IN DEPARTMENTS.DEPARTMENT_ID%TYPE,
P_RESULT OUT DEPARTMENTS.DEPARTMENT_NAME%TYPE)

IS
BEGIN
 SELECT DEPARTMENT_NAME
 INTO P_RESULT
 FROM DEPARTMENTS
 WHERE DEPARTMENT_ID = P_ID;
END;

procedure PRC_CONS_EMP
(P_ID IN EMPLOYEES.EMPLOYEE_ID%TYPE)
IS
V_NAME employees.first_name%TYPE;

BEGIN

SELECT FIRST_NAME
INTO V_NAME
FROM EMPLOYEES
WHERE EMPLOYEE_ID = P_ID;

DBMS_OUTPUT.put_line(V_NAME);

END;

PROCEDURE PRC_CONS_EMPTO
(P_FIRST_NAME IN OUT employees.first_name%TYPE)

IS

BEGIN

SELECT LAST_NAME
INTO P_FIRST_NAME
FROM EMPLOYEES
WHERE FIRST_NAME = P_FIRST_NAME;

END;

PROCEDURE PRC_DML_DEPTO 
(V_ID IN departments.department_id%TYPE,
V_NOME IN departments.department_name%TYPE,
V_MANAGER IN departments.manager_id%TYPE,
V_LOCATION IN departments.location_id%TYPE)
IS

BEGIN
INSERT INTO DEPARTMENTS
VALUES (V_ID,V_NOME,
        V_MANAGER, V_LOCATION);

DBMS_OUTPUT.put_line('DEPTO INSERIDO COM SUCESSO '||' '||V_ID
);

END;

PROCEDURE secure_dml
IS
BEGIN
  IF TO_CHAR (SYSDATE, 'HH24:MI') NOT BETWEEN '08:00' AND '18:00'
        OR TO_CHAR (SYSDATE, 'DY') IN ('SAT', 'SUN') THEN
	RAISE_APPLICATION_ERROR (-20205,
		'You may only make changes during normal office hours');
  END IF;
END secure_dml;

FUNCTION FCT_IMP_PAR
(P_NUM IN NUMBER)  RETURN VARCHAR2 IS 

V_RESULT VARCHAR2(50);
BEGIN

SELECT MOD (P_NUM,2)
INTO V_RESULT
FROM DUAL;

IF V_RESULT = 0 THEN
  RETURN('PAR');

ELSIF V_RESULT = 1 THEN
 RETURN ('IMPAR');
END IF;

END;

FUNCTION FCT_VALID_FUNC
(P_ID IN employees_two.id_emp%TYPE) RETURN NUMBER
IS
V_RESULT NUMBER;

BEGIN

SELECT COUNT (1)
INTO V_RESULT
FROM EMPLOYEES_TWO
WHERE ID_EMP = P_ID;

RETURN (V_RESULT);


END;

END;