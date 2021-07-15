CREATE OR REPLACE PROCEDURE PRC_DMLCMOMP_DEPTO(
P_ID IN departments.department_id%TYPE,     
P_NAME IN departments.department_name%TYPE,
P_MAN IN departments.manager_id%TYPE,
P_LCT IN departments.location_id%TYPE,
P_OPER CHAR)
IS
P_VALID NUMBER;

BEGIN
-- VALIDAÇÃO DA EXIXTÊNCIA DO DPTO
    SELECT COUNT(1)
    INTO P_VALID
    FROM DEPARTMENTS
    WHERE DEPARTMENT_ID = P_ID;

-- TOMADA DE DECISÃO
    IF P_VALID = 0 THEN 
        INSERT INTO DEPARTMENTS 
        VALUES (P_ID,P_NAME,P_MAN,P_LCT);
        DBMS_OUTPUT.put_line('INSERIDO O DPT '|| P_ID||' COM SUCESSO');
    ELSIF P_VALID = 1 AND P_OPER = 'U' THEN
        UPDATE departments
        SET DEPARTMENT_NAME = P_NAME,
            MANAGER_ID = P_MAN,
            LOCATION_ID = P_LCT
        WHERE department_id =  P_ID;
        DBMS_OUTPUT.put_line('ATUALIZADO DPT '|| P_ID||' COM SUCESSO');
    ELSIF P_VALID = 1 AND P_OPER = 'D' THEN
        DELETE FROM departments
        WHERE DEPARTMENT_ID = P_ID;
        DBMS_OUTPUT.put_line('DELETADO O DPT '|| P_ID||' COM SUCESSO');
    END IF;
    COMMIT;
-- AVISO EM CASO DE ERRO
EXCEPTION WHEN OTHERS THEN
    dbms_output.put_line(SQLERRM);

-- FINALIZAÇÃO DO PROGRAMA    
END;
