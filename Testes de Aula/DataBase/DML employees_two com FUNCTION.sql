create or replace PROCEDURE PRC_DML_EMPLOYEES(
P_ID IN employees_two.id_emp%TYPE,
P_NAME IN employees_two.name_emp%TYPE,
P_HIRE_DATE IN employees_two.HIRE_DATE%TYPE,
P_DEPTO IN employees_two.department_NAME%TYPE,
P_SAL IN employees_two.salary%TYPE,
P_OPER IN CHAR)

IS

V_VALID NUMBER;

BEGIN

SELECT FCT_VALID_FUNC(P_ID)
INTO V_VALID
FROM DUAL;

  IF V_VALID = 0 AND P_OPER = 'I' THEN
    INSERT INTO employees_two VALUES(
    P_ID, P_NAME, P_HIRE_DATE,
    P_DEPTO, P_SAL);
    dbms_output.put_line('EMPLOYEE '||P_ID||' '||P_NAME||' INSERIDO COM SUCESSO');  

  ELSIF V_VALID = 1 AND P_OPER = 'U' THEN
    UPDATE employees_two 
    SET ID_EMP = P_ID,
        NAME_EMP = P_NAME, 
        HIRE_DATE = P_HIRE_DATE,
        DEPARTMENT_NAME = P_DEPTO,
        SALARY = P_SAL
    WHERE ID_EMP = P_ID;
    dbms_output.put_line('EMPLOYEE '||P_ID||' '||P_NAME||' ATUALIZADO COM SUCESSO');

  ELSIF V_VALID = 1 AND P_OPER = 'D' THEN
    DELETE FROM employees_two
    WHERE ID_EMP = P_ID;
    dbms_output.put_line('EMPLOYEE '||P_ID||' '||P_NAME||' DELETADO COM SUCESSO');

  END IF;
  COMMIT;
  EXCEPTION WHEN OTHERS THEN
    dbms_output.put_line(SQLERRM);

END;