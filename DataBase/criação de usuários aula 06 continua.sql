create user uleite identified by oracle;

create user uclayton identified by oracle;

grant create session to uleite;

grant create session to uclayton;

commit;

revoke create session from uleite;

create role dw_manager;

grant create session, create table to dw_manager;

grant dw_manager to uleite;