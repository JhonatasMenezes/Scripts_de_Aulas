-- PROGRAMA INSERIR - ATUALIZAR - DELETAR

-- VERIFICAR EXIST�NCIA DO DPTO
    -- SELECT COUNT 
    -- COMPARAR VALOR

-- SE N�O EXIXTIR INSERIR
   -- BLOCO PARA INSERIR
    
-- SE EXIXTIR DECIDIR SE ATUALIZA OU DELETA
   -- BLOCO PARA ATUALIZAR
   -- BLOCO PARA DELETAR

DECLARE
V_ID departments.department_id%TYPE     :=&ID;
V_NAME departments.department_name%TYPE :='&NAME';
V_MAN departments.manager_id%TYPE       :=&MAN;
V_LCT departments.location_id%TYPE      :=&LOCT;

V_VRF number;

V_OPER CHAR(1):='&OPER';

BEGIN
-- VALIDA��O DA EXIXT�NCIA DO DPTO
    SELECT COUNT(1)
    INTO V_VRF
    FROM DEPARTMENTS
    WHERE DEPARTMENT_ID = V_ID;

-- TOMADA DE DECIS�O
    IF V_VRF = 0 THEN 
        INSERT INTO DEPARTMENTS 
        VALUES (V_ID,V_NAME,V_MAN,V_LCT);
        DBMS_OUTPUT.put_line('INSERIDO O DPT '|| V_ID||' COM SUCESSO');
    ELSIF V_VRF = 1 AND V_OPER = 'U' THEN
        UPDATE departments
        SET DEPARTMENT_NAME = V_NAME,
            MANAGER_ID = V_MAN,
            LOCATION_ID = V_LCT
        WHERE department_id =  V_ID;
        DBMS_OUTPUT.put_line('ATUALIZADO DPT '|| V_ID||' COM SUCESSO');
    ELSIF V_VRF = 1 AND V_OPER = 'D' THEN
        DELETE FROM departments
        WHERE DEPARTMENT_ID = V_ID;
        DBMS_OUTPUT.put_line('DELETADO O DPT '|| V_ID||' COM SUCESSO');
    END IF;
    COMMIT;
-- AVISO EM CASO DE ERRO
EXCEPTION WHEN OTHERS THEN
    dbms_output.put_line(SQLERRM);

-- FINALIZA��O DO PROGRAMA    
END;
