DECLARE
    v_dpt_name  departments.department_name%TYPE;
    v_id        departments.department_id%TYPE:=&ID;
BEGIN
    SELECT department_name
    INTO v_dpt_name
    FROM departments
    WHERE department_id = v_id;

    CASE WHEN v_dpt_name = 'Administration' THEN
        dbms_output.put_line('Administration');
    WHEN v_dpt_name = 'Marketing' THEN
        dbms_output.put_line('Marketing');
    WHEN v_dpt_name = 'Human Resources' THEN
        dbms_output.put_line('RH');
    ELSE
        dbms_output.put_line('OUTROS');
    END CASE;

EXCEPTION WHEN OTHERS THEN
    dbms_output.put_line('INVALID DEPARTMENT');
END;