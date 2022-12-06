# import conecction of bd facturacion
from app.connections import connec_bd_fact

# Update column for params in functions
def update_colum_fac(table_name: str, column_name: str,  value_update: str, id:str):
    try:
        tenant_safe: int = 1341
        end_file: str = ".xml"
        path_server: str = "/var/fuentes//facturas//1341/fac/" + value_update + end_file
        #cursor = connec_bd_fact.connect_bd().cursor()
        query: str = "UPDATE facturacion." + table_name + " f " \
                     "SET f." + column_name + " = " + "'" + path_server + "' " \
                     "WHERE f.id = " + id + " " \
                     "AND f.id_tenant = " + str(tenant_safe)
        print(query)
        #cursor.execute()

    except Exception as e:
        print("Error ejecutando consulta ")
        print(e)

#update_colum_fac("fac_efactura", "fac_path_file", "hlafafasdfdsafasd", "772326")