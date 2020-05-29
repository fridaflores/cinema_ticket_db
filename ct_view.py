"""
POR MODIFICAR:
-Eliminar y borrar
-Tal vez usar una sola funcion de midder, headder y footer para show funcionen todos bien 
-Funcion para asegurar que el usuario desea salir
"""
class View:
    #Basics_______________________________________________________________________________________________________________________
    def start(self):
        print('                              (:   ¡Bienvenido Tresure Hunt Cinema!   :(  ')
        print('                              ____________________________________________')
        print('                        *****Donde tenemos los mejores CLÁSICOS de Cine!*******')
      


    def end(self):
        print('')
        print('                             ------------------------------')
        print('                             (: ¡Gracias por su visita! :) ')
        print('                             ------------------------------')

    def option(self, last):
            print(' ')
            print('                              Selecciona una opcion (1-'+last+'): ', end = '')
            print(' ')
    
    def not_valid_option(self):
        print('')
        print('                              ¡Opcion no valida!\nIntenta de nuevo por favor :)')
        print(' ')
    
    def ask(self, output):
        print(output, end = ' ')
    
    def msg(self, output):
        print(output)
    
    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' Se ' +op+ ' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print('¡ERROR! '.center(len(err)+4, '-'))
        print('-' +err+ ' -')
        print('-'*(len(err)+4))
    
    def sorry(self, err):
        print('¡LO SENTIMOS! '.center(len(err)+4, '-'))
        print('-' +err+ ' -')
        print('-'*(len(err)+4))
 
 #Logins____________________________________________________________________________________________________________   
    def login(self):
        print('____________________________________________________________________________________________________')
        print('|                                                 LOGIN                                            |')
        print('----------------------------------------------------------------------------------------------------')
        print('|                     1. Entrar como Administrador   |     2. Entrar como Cliente                   ')
        print('----------------------------------------------------------------------------------------------------')
        print('|                                                3. Salir                                          |')
        print('____________________________________________________________________________________________________')

    def admin_login(self):
        print('')
        print('                              ________________________________')
        print('                             /    Login de Administrador     /')
        print('                             --------------------------------')
        print('                             |1. Acceder :)                  |')
        print('                             |2. Regresar al Login general   |')
        print('                             ________________________________') 
    
    def client_login(self):
        print('')
        print('                              __________________________________')
        print('                             /    Login de Cliente             /')
        print('                             ----------------------------------')
        print('                             |1. Crear tu cuenta de Cliente    |')
        print('                             |2. ¿Ya tienes cuenta? Accede :)  |')
        print('                             |3. Regresa al Login General      |')
        print('                             __________________________________') 

#Menus_______________________________________________________________________________________________________    
    def client_menu(self):
        print('')
        print('                              __________________________________________________________________________')
        print('                             /  MENÚ DEL CLIENTE                                                        /')
        print('                             __________________________________________________________________________')
        print('                             |1. Ver la cartelera del día                                              |')#Pelicula y Hora
        print('                             |2. COMPRAR BOLETOS                                                       |')
        print('                             |3. Buscar funciones a cierta hora                                        |')
        print('                             |4. Buscar una Película por clasificación                                 |')
        print('                             |5. Ver detalles de Alguna Película                                       |')
        #print('|5. Buscar una Película por tipo de Projección                            |')#3D, 4D, etc
        #print('|6. Ver todas las Peíclas que iniciaran a cierta hora                     |')
        print('                             |6. Salir de Vista de Administrador y volver al menu de acceso general     |')
        print('                             ___________________________________________________________________________')

    def admin_menu(self):
        print('')
        print('                              ___________________________________________________________________________ ')
        print('                             /  MENÚ DEL ADMINISTRADOR                                                   /')
        print('                             ___________________________________________________________________________ ')
        print('                             |                       Consulta la Administración de:                    |')
        print('                             ---------------------------------------------------------------------------')
        print('                             |1. Clasificación de Peliculas                                            |')
        print('                             |2. Género de Peliculas                                                   |')
        print('                             |3. Peliculas y sus detalles                                              |')
        print('                             |4. Idiomas en que se presentaran las Peliculas                           |')
        print('                             |5. Salas                                                                 |')
        print('                             |6. Asientos de las Salas                                                 |')
        print('                             |7. Funciones                                                             |')
        print('                             |8. Tipos de Boleto                                                       |')
        print('                             |9. Cuentas de Usuarios                                                   |')
        print('                             |10. Regresar                                                             |')
        print('                             ___________________________________________________________________________')
    
#Submenus_________________________________________________________________________________________________________________
#Menu para vista de Inicio, crear tipos de usuario y administradores    

#Users________________________________________________________________________________________________________________
    def users_menu(self):
        print('                           ..............................................')
        print('                           : Administración de CUENTAS DE USUARIOS      :')
        print('                           ..............................................')
        print('                           :                                            :')
        print('                           :  1. Crear un NUEVO admin                    :')
        print('                           :  2. Mostrar especificamente algun Usuario  :')
        print('                           :  3. Mostrar todos los Usuario existentes   :')
        print('                           :  4. Actualizar un Usuario                  :')
        print('                           :  5. Borrar un Usuario                      :')
        print('                           :  6. Regresar a Menu Principal              :')
        print('                           ..............................................')

    def show_a_user(self, record):
        print('                              ID del Usuario: ', record[0])
        print('                              Tipo de Usuario: ', record[1])
        print('                              Nombre: ', record[2])
        print('                              Apellido: ', record[3])

    def show_user_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_user_midder(self):
        print('-'*48)

    def show_user_footer(self):
        print('*'*48)

#Classifications________________________________________________________________________________________________________________
    def class_menu(self):
        print('                      ..............................................')
        print('                           Administración de CLASIFICACIONES ')
        print('                           ..................................')
        print('                            ')
        print('                           1. Crear NUEVA Clasificación')
        print('                           2. Mostrar especificamente alguna Clasificación')
        print('                           3. Mostrar todas las Clasificaciones')
        print('                           4. Actualizar una Clasificación')
        print('                           5. Borrar una Clasificación')
        print('                           6. Regresar a Menu Principal')
        print('                      ..............................................')

    def show_a_class(self, record):
        print('                              Clasificaión: ', record[0])
        print('                              Edad mínima apropiada para esta clasificación: ', record[1])

    def show_class_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_class_midder(self):
        print('-'*48)

    def show_class_footer(self):
        print('*'*48)

#Genres________________________________________________________________________________________________________________
    def genres_menu(self):
        print('                      ..............................................')
        print('                           Administración de GÉNEROS ')
        print('                           ..............................')
        print('                            ')
        print('                           1. Crear NUEVO Género')
        print('                           2. Mostrar todos los Géneros')
        print('                           3. Borrar un Género')
        print('                           4. Regresar a Menu Principal')
        print('                      ..............................................')
    def show_a_genre(self, record):
        print('                              Género: ', record[0])

    def show_genre_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_genre_midder(self):
        print('-'*48)

    def show_genre_footer(self):
        print('*'*48)


#Languages________________________________________________________________________________________________________________
    def lang_menu(self):
        print('                      ..............................................')
        print('                            Administración de IDIOMAS ')
        print('                           ..............................')
        print(' ')
        print('                           1. Crear NUEVO Idioma')
        print('                           2. Mostrar un Idioma')
        print('                           3. Actualizar un Idioma')
        print('                           4. Eliminar un Idioma')
        print('                           5. Volver a Menu Principal') 
        print('                      ..............................................')

    def show_a_lang(self, record):
        print('                              Idioma: ', record[0])
        print('                              Subtítulos: ', record[1])

    def show_lang_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_lang_midder(self):
        print('-'*48)

    def show_lang_footer(self): 
        print('*'*48)


#Movies________________________________________________________________________________________________________________
    def movies_menu(self):
        print('                              ..............................')
        print('                               Administración de PELÍCULAS ')
        print('                              ..............................')
        print(' ')
        print('                              1. Crear NUEVA Película')
        print('                              2. Mostrar una Película')
        print('                              3. Mostrar una Película con sus detalles')
        print('                              4. Mostrar todas las Películas (cartelera)')
        print('                              5. Mostrar las Películas con cierta clasificación')
        print('                              6. Actualizar una Película')
        print('                              7. Eliminar una Película')
        print('                              8. Volver a Menu Principal') 

    def show_a_movie(self, record):
        print('                              ID: ', record[0])
        print('                              Título Película: ', record[1])
    
    def show_a_movie_ad(self, record):
        print('                              ID: ', record[0])
        print('                              Título Película: ', record[1])
        print('                              Género: ', record[2])
        print('                              Clasificación: ', record[2])

    def show_movie_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_movie_midder(self):
        print('-'*48)

    def show_movie_footer(self): 
        print('*'*48)


#View Movie Details________________________________________________________________________________________________________________
    def show_a_md(self, record):
        print('                              ID: ', record[0])
        print('                              Género de la Película: ', record[1])
        print('                              Clasificación de la Película: ', record[2])

    def show_md_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_md_midder(self):
        print('-'*48)

    def show_md_footer(self):
        print('*'*48)


#View Halls________________________________________________________________________________________________________________
    def halls_menu(self):
        print('                      ..............................................')
        print('                                 Administración de Salas ')
        print('                             ..............................')
        print(' ')
        print('                      1. Crear Sala')
        print('                      2. Mostrar especificamente alguna Sala y su cantidad de asientos')
        print('                      3. Mostrar todas las Salas')
        print('                      4. Actualizar una Sala')
        print('                      5. Borrar una Sala')
        print('                      6. Regresar a Menu Principal')
        print('                      ................................................')

    def show_a_hall(self, record):
        print('                              Número de Sala: ', record[0])
        print('                              Capacidad: ', record[1], ' personas')

    def show_hall_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_hall_midder(self):
        print('-'*48)

    def show_hall_footer(self):
        print('*'*48)

#View Seats________________________________________________________________________________________________________________
    def seats_menu(self):
        print('               ............................................')
        print('                      Administración de Asientos ')
        print('                      ..............................')
        print('                       ')
        print('                       1. Crear Asiento')
        print('                       2. Ver Asientos disponibles en una sala')
        print('                       3. Leer todos Asientos en una sala')
        print('                       4. Actualizar un Asiento')
        print('                       5. Borrar un Asiento')
        print('                       6. Regresar a Menu Principal')
        print('               ............................................')

    def show_a_seat(self, record):
        print('                              Número de Sala: ', record[3])
        print('                              Asiento: ', record[0])
        print('                              Fila: ', record[1])
        print('                              Estado (0 = Libre, 1 = Ocupado): ', record[2])
    
    def show_a_seat_u(self, record):
        print('                              Asiento: ', record[0][0])
        print('                              Fila: ', record[0][1])
        print('                              Estado (0 = Libre, 1 = Ocupado): ', record[0][2])
        print('                              Número de Sala: ', record[0][3])
    
    def show_a_seat_h(self, record):
        print('                              Asiento: ', record[0])
        print('                              Fila: ', record[1])

    def show_seat_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_seat_midder(self):
        print('-'*48)

    def show_seat_footer(self):
        print('*'*48)


#Schedules________________________________________________________________________________________________________________
    def sch_menu(self):
        print('            .......................................................................')
        print('                                 Administración de FUNCIONES                       ')
        print('            ........................................................................')
        print(' ')
        print('                      1. Crear NUEVA Función')
        print('                      2. Mostrar cierta Función')
        print('                      3. Mostrar todas las Funciones')
        print('                      4. Mostrar todas las Funciones a cierta Hora y Fecha')
        print('                      5. Mostrar todas las Funciones de alguna Película en cierta Fecha')
        print('                      6. Mostrar todas las Funciones con cierto Género de Película')
        print('                      7. Actualizar Función')
        print('                      8. Eliminar Función')
        print('                      9. Volver a Menu Principal') 

    def show_a_sch(self, record):
        print(f'    {record[0]:<8}|{record[1]:<25}|{record[2]:<12}|{record[3]:<12}','|', record[4],'|', record[5])

    def show_sch_header(self, header):
        print(header.center(90,'*'))
        print('______________________________________________________________________________________________')
        print('Función'.ljust(8)+'    |'+'Película'.ljust(25)+'|'+'Proyección'.ljust(12)+'|'+'Idioma'.ljust(12)+'|'+'Día'.ljust(12)+'|'+'Hora'.ljust(25))
        print('-'*90)
    
    def show_sch_midder(self):
        print('-'*90)

    def show_sch_footer(self): 
        print('*'*90)

#Type of Tickets________________________________________________________________________________________________________________
    def tt_menu(self):
        print('                      ..................................')
        print('                      Administración de Tipos de Boletos ')
        print('                      ..................................')
        print(' ')
        print('                      1. Crear NUEVA Tipo de Boleto')
        print('                      2. Mostrar especificamente algun Tipo de Boleto')
        print('                      3. Mostrar todos los Tipos de Boleto')
        print('                      4. Actualizar un Tipo de Boleto')
        print('                      5. Borrar un Tipo de Boleto')
        print('                      6. Regresar a Menu Principal')

    def show_a_tt(self, record):
        print('Tipo de Boleto: ', record[0])
        print('Precio: ', record[1])

    def show_tt_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_tt_midder(self):
        print('-'*48)

    def show_tt_footer(self):
        print('*'*48)






