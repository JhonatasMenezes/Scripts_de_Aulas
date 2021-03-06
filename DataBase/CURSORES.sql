-- CURSORES 
-- CRIAR TABELA TESTE
CREATE TABLE TB_PESSOA (
    IDPESSOA        INTEGER NOT NULL
,   NOME            VARCHAR2(50) NOT NULL
,   DATANASCIMENTO  DATE NOT NULL
,   ALTURA          NUMBER(5,2)
,   PESO            NUMBER(5,2));

-- POPULAR A TABELA COM CARGA DE DADOS
DECLARE

V_ID_PESSOA TB_PESSOA.idpessoa%TYPE;
V_NOME TB_PESSOA.nome%TYPE;
V_DT_NASC TB_PESSOA.datanascimento%TYPE;

BEGIN 

V_NOME := 'JOAO DA SILVA';
V_DT_NASC := TO_DATE('01/01/1990');

FOR DD IN 1..50000 LOOP
 SELECT NVL(MAX(P.IDPESSOA),0)+1
 INTO V_ID_PESSOA
 FROM TB_PESSOA P;

 INSERT INTO TB_PESSOA(IDPESSOA,NOME,DATANASCIMENTO)
                VALUES(V_ID_PESSOA,V_NOME,V_DT_NASC);


 END LOOP;

COMMIT;
END;

-- TESTES DE CONCEITO
-- CURSOR EXPLÍCITO
create or replace PROCEDURE PCT_TST_CURSOR IS
V_DT_INICIO TIMESTAMP;
V_DT_FIM    TIMESTAMP;
CURSOR CR_PESSOA IS
SELECT * FROM TB_PESSOA;

V_PESSOA CR_PESSOA%ROWTYPE;

BEGIN

V_DT_INICIO := SYSTIMESTAMP;

    OPEN CR_PESSOA;
    LOOP
    FETCH CR_PESSOA INTO V_PESSOA;
    EXIT WHEN CR_PESSOA%NOTFOUND;
     NULL;
    END LOOP;
    CLOSE CR_PESSOA;


V_DT_FIM := SYSTIMESTAMP;


DBMS_OUTPUT.PUT_LINE('TEMPO PROCESSAMENTO: '
||TO_CHAR(V_DT_FIM - V_DT_INICIO,'DD/MM/YYYY HH24:MI:SS.FF'));

END;

-- CURSOR IMPLÍCITO 
create or replace PROCEDURE PCT_TST_FOR IS
V_DT_INICIO TIMESTAMP;
V_DT_FIM    TIMESTAMP;

BEGIN

V_DT_INICIO := SYSTIMESTAMP;

    FOR DD IN (SELECT P.IDPESSOA
               FROM TB_PESSOA P) LOOP
    NULL;

    END LOOP;



V_DT_FIM := SYSTIMESTAMP;


DBMS_OUTPUT.PUT_LINE('TEMPO PROCESSAMENTO: '
||TO_CHAR(V_DT_FIM - V_DT_INICIO,'DD/MM/YYYY HH24:MI:SS.FF'));

END;

-- CURSOR BULK COUNT
create or replace PROCEDURE PCT_TST_BULK_COUNT IS
V_DT_INICIO TIMESTAMP;
V_DT_FIM    TIMESTAMP;

TYPE TYP_PESSOA IS TABLE OF TB_PESSOA%ROWTYPE;

V_TB_PESSOA TYP_PESSOA;

BEGIN

V_DT_INICIO := SYSTIMESTAMP;

    SELECT * BULK COLLECT INTO V_TB_PESSOA
    FROM TB_PESSOA;

    FOR DD IN 1..V_TB_PESSOA.COUNT LOOP
    NULL;

    END LOOP;


V_DT_FIM := SYSTIMESTAMP;


DBMS_OUTPUT.PUT_LINE('TEMPO PROCESSAMENTO: '
||TO_CHAR(V_DT_FIM - V_DT_INICIO,'DD/MM/YYYY HH24:MI:SS.FF'));

END;

-- CURSOR BULK FIRST LAST
create or replace PROCEDURE PCT_TST_BULK_FIRS_LAST IS
V_DT_INICIO TIMESTAMP;
V_DT_FIM    TIMESTAMP;

TYPE TYP_PESSOA IS TABLE OF TB_PESSOA%ROWTYPE;

V_TB_PESSOA TYP_PESSOA;

BEGIN

V_DT_INICIO := SYSTIMESTAMP;

    SELECT * BULK COLLECT INTO V_TB_PESSOA
    FROM TB_PESSOA;

    FOR DD IN V_TB_PESSOA.FIRST..V_TB_PESSOA.LAST LOOP
    NULL;

    END LOOP;


V_DT_FIM := SYSTIMESTAMP;


DBMS_OUTPUT.PUT_LINE('TEMPO PROCESSAMENTO: '
||TO_CHAR(V_DT_FIM - V_DT_INICIO,'DD/MM/YYYY HH24:MI:SS.FF'));

END;