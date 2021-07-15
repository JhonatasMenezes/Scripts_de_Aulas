-- PACKAGE SPECIFICATION
CREATE OR REPLACE PACKAGE PKG_RH AS
PROCEDURE add_job_history
  (  p_emp_id          job_history.employee_id%type
   , p_start_date      job_history.start_date%type
   , p_end_date        job_history.end_date%type
   , p_job_id          job_history.job_id%type
   , p_department_id   job_history.department_id%type
   );

PROCEDURE PRC_CONS_DEPTO
(P_ID IN DEPARTMENTS.DEPARTMENT_ID%TYPE,
P_RESULT OUT DEPARTMENTS.DEPARTMENT_NAME%TYPE);

procedure PRC_CONS_EMP
(P_ID IN EMPLOYEES.EMPLOYEE_ID%TYPE);

PROCEDURE PRC_CONS_EMPTO
(P_FIRST_NAME IN OUT employees.first_name%TYPE);

PROCEDURE PRC_DML_DEPTO 
(V_ID IN departments.department_id%TYPE,
V_NOME IN departments.department_name%TYPE,
V_MANAGER IN departments.manager_id%TYPE,
V_LOCATION IN departments.location_id%TYPE);

PROCEDURE secure_dml;

FUNCTION FCT_IMP_PAR
(P_NUM IN NUMBER)  RETURN VARCHAR2;

FUNCTION FCT_VALID_FUNC
(P_ID IN employees_two.id_emp%TYPE) RETURN NUMBER;

END;
-- PACKAGE BODY
