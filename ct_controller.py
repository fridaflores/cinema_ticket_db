from ct_model import Model
from ct_view import View
from datetime import date

#BORRAR TODAS IMPRESIOENES INECESARIAS!!! 
#¿como hacer que no se vea la contraseña cuando la pido?

class Controller:
#Basics
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):#Comienzo del programa
        self.view.start()#Bienvenida al sistema
        self.login_menu()#Opciones de acceso 

    def update_lists(self, fs, vs): # (type_user, flores)
            fields = []
            vals = []
            for f, v in zip(fs, vs):
                if v != '':
                    fields.append(f+' = %s') #fields = [type_user = %s ]
                    vals.append(v) #vals = [flores]
            return fields, vals #[type_user = %s],[flores]

#Users Controller____________________________________________________________________________________      
#Login___________________________________________________________________________________
#Admin__________________________________________________________________________
    def admin_login_menu(self): #Despliega opciones de crear o entrar como admin
                o = '0'
                while o != '2':
                    self.view.admin_login()
                    self.view.option('2')
                    o = input()
                    print(' ')
                    if o == '1':
                        self.admin_access() #Acceder como admin
                    elif o == '3': 
                        return
                    else:
                        self.view.not_valid_option()

    def ask_user_ad(self): #Pide datos personales para creación de un Admin
        print(' ')
        print('Introdice tus datos personales por favor :)')
        print('-------------------------------------------')
        type_user = 'Admin'
        self.view.ask('Nombre: ')
        n = input() 
        self.view.ask('Apellido Paterno: ')
        a_p = input() 
        self.view.ask('Apellido Materno: ')
        a_m = input() 
        self.view.ask('Contraseña: ')
        u_pass = input() 
        return [type_user, n, a_p, a_m, u_pass]
    
    def admin_access(self):#Verifica que el ID de Admin y su contraseña coincidan con los registros en la b.d.
        self.view.ask('ID de Administrador: ')
        i_input = input() 
        id_input = int(i_input)
        self.view.ask('Contraseña: ')
        p_input = input() 
        state = self.model.ad_access(id_input, p_input)#(id, password)
        if state == True:
            print('ACCESO CORRECTO')
            self.admin_menu()#Métodos que puede realizar el admin
        else:
            print('ACCESO INCORRECTO: Tu ID o contraseña son oncorrectas, intenta de nuevo :) ')
        
    def create_user_ad(self):#Creación de un cliente
        type_user, n, a_p, a_m, u_pass = self.ask_user_cl() 
        out = self.model.create_user_acc(type_user, n, a_p, a_m, u_pass)
        if type(out) == int:
            self.view.ok(out, ' agrego')
            print('Este es tu ID de usuario: ')
            print(out)
            print('Lo necesitaras para iniciar sesión, por favor, recuerdalo :)')
        else:
            self.view.error('NO SE PUDO AGREGAR ESTE USUARIO, por favor revisa!')
#Clients_____________________________________________________________________________________________
    def client_login_menu(self): #Despliega opciones de crear o entrar como cliente
                o = '0'
                while o != '3':
                    self.view.client_login()
                    self.view.option('3')
                    o = input()
                    print(' ')
                    if o == '1':
                        self.create_user_cl() #Crear nuevo cliente 
                    if o == '2':
                        self.client_access() #Crear nuevo cliente 
                    elif o == '3': 
                        return
                    else:
                        self.view.not_valid_option()

    def ask_user_cl(self):#Pide datos personales para creacion de cliente
        print(' ')
        print('Introdice tus datos personales por favor :)')
        print('-------------------------------------------')
        type_user = 'Client'
        self.view.ask('Nombre: ')
        n = input() 
        self.view.ask('Apellido Paterno: ')
        a_p = input() 
        self.view.ask('Apellido Materno: ')
        a_m = input() 
        self.view.ask('Contraseña: ')
        u_pass = input() 
        return [type_user, n, a_p, a_m, u_pass]
    
    def client_access(self):#Verifica que el ID de cliente y su contraseña coincidan con los registros en la b.d.
        self.view.ask('ID de Cliente: ')
        i_input = input() 
        id_input = int(i_input)
        self.view.ask('Contraseña: ')
        p_input = input() 
        state = self.model.cl_access(id_input, p_input)#(id, password)
        if state == True:
            print('ACCESO CORRECTO')
            id_client = id_input
            self.client_menu(id_client)
        else:
            print('ACCESO INCORRECTO: Tu ID o contraseña son oncorrectas, intenta de nuevo :) ')
        
    def create_user_cl(self):#Creción de cliente
        type_user, n, a_p, a_m, u_pass = self.ask_user_cl() 
        out = self.model.create_user_acc(type_user, n, a_p, a_m, u_pass)
        if type(out) == int:
            self.view.ok(out, ' agrego')
            print('Este es tu ID de usuario: ')
            print(out)
            print('Lo necesitaras para iniciar sesión, por favor, recuerdalo :)')
        else:
            self.view.error('NO SE PUDO AGREGAR ESTE USUARIO, por favor revisa!')
#Menus____________________________________________________________________________________________________________
#Aparece despues del mensaje de bienvenida al programa, da la opcion de entrar como administrador o como cliente
    def login_menu(self):
        o = '0'
        while o != '3':
            self.view.login()
            self.view.option('3')
            o = input()
            if o == '1':
                self.admin_login_menu() #Entrar como Administrador o crear nuevo admin (arriba esta la def de la función)
            if o == '2':
                self.client_login_menu() #Entrar como Cliente o crear nuevo cliente
            elif o == '3': 
                self.view.end()
            else:
                self.view.not_valid_option()
        return

#Esta función se ejecuta despues de haber accedido al sistema como admin
    def admin_menu(self): #Despliega menu de metodos con los que puede interactuar de todas las tablas de la bd y vistas
        o = '0'
        while o != '10':
            self.view.admin_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.class_menu() #CRUD de Clasificación de pelis
            elif o == '2': 
                self.genres_menu()#CRUD de géneros
            elif o == '3': 
                self.movies_menu()#CRUD de Películas
            elif o == '4': 
                self.lang_menu()#CRUD de Idiomas 
            elif o == '5': 
                self.halls_menu()#CRUD de Salas 
            elif o == '6': 
                self.seats_menu()#CRUD de Asientos 
            elif o == '7': 
                self.sch_menu()#CRUD de Funciones
            elif o == '8': 
                self.tt_menu()#CRUD de Tipos de Boleto
            elif o == '9': 
                self.users_menu()   #CRUD de Usuarios
            elif o == '10': 
                self.view.end() 
            else:
                self.view.not_valid_option()
        return

#Esta función se ejecuta despues de haber accedido al sistema como cliente    
    def client_menu(self, id_client):#Despliega menu de metodos con los que puede interactuar, solo con ciertas tablas y vistas
        o = '0'
        while o != '6': #MODIFICAR Y AGREGAR OPCIONES REALES QUE PUEDE REALIZAR EL CLIENTE
            self.view.client_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.read_a_sch_today()#Ver la cartelera del día
            elif o == '2': 
                self.buy_tickets(id_client)#Comprar boletos 
            elif o == '3': 
                self.read_a_sch_time()#Ver funciones a cierta hora
            elif o == '4': 
                self.read_a_sch_class()#Ver funciones a con cierta clasificación
            elif o == '5':
                self.read_a_movie_ad()#Ver pelicula con sus detalles 
            elif o == '6': 
                self.view.end()
            else:
                self.view.not_valid_option()
        return

#Metodos generales de Usuarios (Admins y Clients)_________________________________________________________________________-----------
    #uressrs menu en controller
    def users_menu(self):
            o = '0'
            while o != '6':
                self.view.users_menu()
                self.view.option('6')
                o = input()
                print(' ')
                if o == '1':
                    self.create_user_ad #Crear admin
                elif o == '2': 
                    self.read_a_user()
                elif o == '3': 
                    self.read_all_users()
                elif o == '4': 
                    self.update_a_user()
                elif o == '5': 
                    self.delete_a_user()
                elif o == '6': 
                    return
                else:
                    self.view.not_valid_option()
    
    
    def read_a_user(self):
        self.view.ask('Introduce ID del Usuario que desea consultar: ')
        i_user = input()
        user = self.model.read_a_user_acc(i_user)
        if type(user)==tuple:
            self.view.show_user_header('Datos del Usuario '+i_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('ESTE ID DE TIPO DE USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL USUARIO, por favor revisa.')
    
    def read_all_users(self):
        users = self.model.read_all_users_acc()
        if type(users) == list:
            self.view.show_user_header('Estos son todos los Usuarios que existen: ')
            for user in users:
                print(' ')
                self.view.show_a_user(user)
                print(' ')
            self.view.show_user_midder()
            self.view.show_user_footer
        else:
            self.view.error('PROBLEMA AL LEER LOS USUARIOS, por favor revisa.')
        return
    
    def update_a_user(self):
        self.view.ask('Introduce el ID del Usuario a modificar: ')
        i_user = input()
        user = self.model.read_a_user_acc(i_user)
        if type(user) == tuple:
            self.view.show_user_header('Datos del Usuario con ID  '+i_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('ESE USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER UASUARIO, por favor revisa.')
            return
        self.view.msg('A continuacion ingrese el nuevo valor.')
        self.view.msg('Deje un espacio vacio en caso de no querer modificar.')
        whole_vals = self.ask_user_cl()
        fields, vals = self.update_lists(['id_type_user', 'u_fname', 'u_sname1','u_sname2', 'u_password'], whole_vals)#(ty_u, flores) ->> fields, vals = [type_user = %s],[flores]
        vals.append(i_user) 
        vals = tuple(vals)#vals = (flores, 7)
        out = self.model.update_user_acc(fields,vals) #([type_user, ...= %s], (flores, 7))
        if out == True:
            self.view.ok(i_user,' actualizo')
        else:
            self.view.error('PROBLEMA AL LEER EL USUARIO, por favor revisa.')
        return
    
    def delete_a_user(self):
        self.view.ask('Introduce ID del Usuario de desea eliminar: ')
        i_user = input()
        count = self.model.delete_user_acc(i_user)
        if count != 0:
            self.view.ok(i_user, 'se borro')
        else:
            if count == 0:
                self.view.error('ESTE ID DE USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL USUARIO, por favor revisa.')
        return


#Classifications Controller____________________________________________________________________________________
    def class_menu(self):
        o = '0'
        while o != '6':
            self.view.class_menu()
            self.view.option('6')
            o = input()
            print(' ')
            if o == '1':
                self.create_class()
            elif o == '2': 
                self.read_a_class()
            elif o == '3': 
                self.read_all_classifications()
            elif o == '4': 
                self.update_a_class()
            elif o == '5': 
                self.delete_a_class()
            elif o == '6': 
                return
            else:
                self.view.not_valid_option()

    def ask_class_c(self):
        self.view.ask('Edad mínima apropiada para esta clasificación: ')
        min_age = input()#3
        return min_age
    
    def ask_class_u(self):
        self.view.ask('Edad mínima apropiada para esta clasificación: ')
        min_age = input()#3
        return [min_age]
    
    def create_class(self): 
        self.view.ask('Identificador de la Clasificaión: ')
        id_class = input() #AA
        min_age = self.ask_class_c()#3
        out = self.model.create_a_class(id_class, min_age)#(AA,3)
        print('out')
        print(out)
        if out == True:
            self.view.ok(id_class, ' agrego')
        else:
            if out.errno == 1062:
                self.view.error('ESA CLASIFICACIÓN ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR ESA CLASIFICACIÓN, por favor revisa!')
    
    def read_a_class(self):
        self.view.ask('Introduce el ID de la Clasificación que deseas consultar: ')
        i_class = input()
        print('')
        _class = self.model.read_a_class(i_class)
        if type(_class)==tuple:
            self.view.show_class_header('Especificación de la Clasificación '+i_class+' ')
            self.view.show_a_class(_class)
            self.view.show_class_midder()
            self.view.show_class_footer()
        else:
            if _class == None:
                self.view.error('ESTA CLASIFICACIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CLASIFICACIÓN, por favor revisa.')
    
    def read_all_classifications(self):
        _classes = self.model.read_all_classifications()
        if type(_classes) == list:
            self.view.show_class_header('Estas son todas las Clasificaciones que existen: ')
            for _class in _classes:
                self.view.show_a_class(_class)
                print('----------------------------------')
            self.view.show_class_midder()
            self.view.show_class_footer
        else:
            self.view.error('PROBLEMA AL LEER LOS USUARIOS, por favor revisa.')
        return
    
    def update_a_class(self):
        self.view.ask('Introduce el ID de la Clasificación a modificar: ')
        i_class = input()#AA
        _class = self.model.read_a_class(i_class)
        if type(_class) == tuple:
            self.view.show_class_header('Datos de la Clasificación con ID  '+i_class+' ')
            self.view.show_a_class(_class)
            self.view.show_class_midder()
            self.view.show_class_footer()
        else:
            if _class == None:
                self.view.error('ESTA CLASIFICACIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER CLASIFICACIÓN, por favor revisa.')
            return
        self.view.msg('A continuacion ingrese el nuevo valor.')
        self.view.msg('Deje un espacio vacio en caso de no querer modificar.')
        whole_vals = self.ask_class_u()#flores
        fields, vals = self.update_lists(['m_min_app_age'], whole_vals)#(ty_u, flores) ->> fields, vals = [type_user = %s],[flores]
        vals.append(i_class) #vals = [flores, 7]
        vals = tuple(vals)#vals = (flores, 7)
        out = self.model.update_a_class(fields,vals) #([type_user = %s], (flores, 7))
        if out == True:
            self.view.ok(i_class,' actualizo')
        else:
            self.view.error('PROBLEMA AL LEER LA CLASIFICACIÓN, por favor revisa.')
        return
    
    def delete_a_class(self):
        self.view.ask('Introduce ID de la Clasificación que desea eliminar: ')
        i_class = input()
        count = self.model.delete_a_class(i_class)
        if count != 0:
            self.view.ok(i_class, 'se borro')
        else:
            if count == 0:
                self.view.error('ESTE ID DE CLASIFICACIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA CLASIFICACIÓN, por favor revisa.')
        return

#Genres Controller____________________________________________________________________________________
    def genres_menu(self):
        o = '0'
        while o != '4':
            self.view.genres_menu()
            self.view.option('4')
            o = input()
            print(' ')
            if o == '1':
                self.create_genre()
            elif o == '2': 
                self.read_all_genres()
            elif o == '3': 
                self.delete_genre()
            elif o == '4': 
                return
            else:
                self.view.not_valid_option()
    
    def ask_genre_u(self):
        self.view.ask('Introduce la actualización Género: ')
        genre = input()#3
        return [genre]
    
    def create_genre(self): 
        self.view.ask('Género: ')
        id_genre = input() #Comedia
        out = self.model.create_genre(id_genre)#(Comedia)
        print('out')
        print(out)
        if out == True:
            self.view.ok(id_genre, ' agrego')
        else:
            if out.errno == 1062:
                self.view.error('ESTE GÉNERO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR ESE GÉNERO, por favor revisa!')
    
    
    def read_all_genres(self):
        genres = self.model.read_all_genres()
        if type(genres) == list:
            self.view.show_genre_header('Estos son todos los Géneros que existen: ')
            for genre in genres:
                self.view.show_a_genre(genre)
                print('----------------------------------')
            self.view.show_genre_midder()
            self.view.show_genre_footer
        else:
            self.view.error('PROBLEMA AL LEER LOS GÉNEROS, por favor revisa.')
        return
        
    def delete_genre(self):
        self.view.ask('Introduce el Género que desea eliminar: ')
        i_genre = input()
        count = self.model.delete_genre(i_genre)
        if count != 0:
            self.view.ok(i_genre, 'se borro')
        else:
            if count == 0:
                self.view.error('ESTE GÉNERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR GÉNERO, por favor revisa.')
        return


#Languages Controller____________________________________________________________________________________
    def lang_menu(self):
        o = '0'
        while o != '5':
            self.view.lang_menu()
            self.view.option('5')
            o = input()
            print(' ')
            if o == '1':
                self.create_lang()
            elif o == '2': 
                self.read_a_lang()
            elif o == '3': 
                self.update_lang()
            elif o == '4': 
                self.delete_lang()
            elif o == '5': 
                return
            else:
                self.view.not_valid_option()
    
    def ask_lang_c(self):
        self.view.ask('Subtítulos: ')
        id_sub = input() 
        return id_sub
    
    def ask_lang_u(self):
        self.view.ask('Subtítulos: ')
        id_sub = input()
        return [id_sub]
        
    def create_lang(self): 
        self.view.ask('Idioma: ')
        id_lang = input() #Ingles
        id_sub = self.ask_lang_c()
        out = self.model.create_language(id_lang, id_sub)#(Ingles, español)
        print('out')
        print(out)
        if out == True:
            self.view.ok(id_lang, ' agrego')
        else:
            if out.errno == 1062:
                self.view.error('ESTE IDIOMA ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR ESE IDIOMA, por favor revisa!')
    
    def read_a_lang(self):
        self.view.ask('Introduce el Idioma deseas consultar: ')
        i_lang = input()
        print('')
        lang = self.model.read_a_language(i_lang)
        if type(lang)==tuple:
            self.view.show_lang_header('Subtítulos en: '+i_lang+' ')
            self.view.show_a_lang(lang)
            self.view.show_lang_midder()
            self.view.show_lang_footer()
        else:
            if lang == None:
                self.view.error('ESE IDIOMA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL IDIOMA, por favor revisa.')
    
    def update_lang(self):
        self.view.ask('Introduce el Idioma: ')
        i_lang = input()
        lang = self.model.read_a_language(i_lang)
        if type(lang) == tuple:
            self.view.show_lang_header('Datos del Idioma '+i_lang+' ')
            self.view.show_a_lang(lang)
            self.view.show_lang_midder()
            self.view.show_lang_footer()
        else:
            if lang == None:
                self.view.error('ESE IDIOMA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER IDIOMA, por favor revisa.')
            return
        self.view.msg('A continuacion ingrese el nuevo valor.')
        self.view.msg('Deje un espacio vacio en caso de no querer modificar.')
        whole_vals = self.ask_lang_u()
        fields, vals = self.update_lists(['subtitles'], whole_vals)
        vals.append(i_lang)
        vals = tuple(vals)
        out = self.model.update_language(fields,vals) 
        print('Out')
        print(out)
        if out == True:
            self.view.ok(i_lang,' actualizo')
        else:
            self.view.error('PROBLEMA AL LEER IDIOMA, por favor revisa.')
        return
        
    def delete_lang(self):
        self.view.ask('Introduce el Idioma que deseas eliminar: ')
        i_lang = input()
        count = self.model.delete_language(i_lang)
        if count != 0:
            self.view.ok(i_lang, 'se borro')
        else:
            if count == 0:
                self.view.error('ESTE IDIOMA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR IDIOMA, por favor revisa.')
        return

#Movies Controller____________________________________________________________________________________
    def movies_menu(self):
        o = '0'
        while o != '8':
            self.view.movies_menu()
            self.view.option('8')
            o = input()
            print(' ')
            if o == '1':
                self.create_movie()
            elif o == '2': 
                self.read_a_movie() #Leer una pelicula basico
            elif o == '3': 
                self.read_a_movie_ad()#Leer una peli con detalles
            elif o == '4': 
                self.read_all_movies() #Leer todas las pelis
            elif o == '5': 
                self.read_movies_class()#Leer pelixs con cierta clasificacion
            elif o == '6': 
                self.update_a_movie()
            elif o == '7': 
                self.delete_a_movie()
            elif o == '8': 
                return
            else:
                self.view.not_valid_option()

    def ask_movie_c(self):
        self.view.ask('Título: ')
        m_t = input() #Matrix
        return m_t
    
    def ask_movie_u(self):
        self.view.ask('Título ')
        m_t = input()
        return [m_t]
    
    def ask_a_md(self):
        self.view.ask('Género: ')
        genre = input()#3
        self.view.ask('Clasificación: ')
        _class = input()
        return genre, _class
    
    def create_md(self, id_movie): 
        genre, _class = self.ask_a_md()
        out = self.model.create_m_det(id_movie, genre, _class)#(Ingles, español)
        print('out')
        print(out)
        if out == True:
            self.view.ok(id_movie, ' agrego')
        else:
            if out.errno == 1062:
                self.view.error('ESTE PELICULA ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL DETALLE DE LA PELICULA, por favor revisa!')

    def create_movie(self):
        movie_title = self.ask_movie_c() 
        out = self.model.create_movie(movie_title)#Regresa lastrow -> out = id de la ultima peli creada
        if type(out) == int:
            self.create_md(out)#Aqui creo el detalle de la pelicula
            self.view.ok(movie_title,' agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA PELÍCULA ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA PELÍCULA, por favor revisa!')
    
    def read_a_movie(self):
        self.view.ask('Introduce ID de la pelicula que deseas ver: ')
        i_movie = input()
        print('')
        movie = self.model.read_a_movie(i_movie)
        if type(movie)==tuple:
            self.view.show_movie_header('Título de la Película: '+i_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('ESTE ID DE TIPO DE PELÍCULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELÍCULA, por favor revisa.')
    
    def read_a_movie_ad(self):
        self.view.ask('Introduce ID de la pelicula que deseas ver: ')
        i_movie = input()
        print('')
        movie = self.model.read_movie_ad(i_movie)
        print(movie)
        if type(movie)==tuple:
            self.view.show_movie_header('Detalles de la Película: '+movie[0]+' ')
            self.view.show_a_md(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('ESTE ID DE TIPO DE PELÍCULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELÍCULA, por favor revisa.')
    
    def read_all_movies(self):
        movies = self.model.read_all_movies()
        if type(movies) == list:
            self.view.show_movie_header('Estas son todas las Películas que existen: ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer
        else:
            self.view.error('PROBLEMA AL LEER LAS PELÍCULAS, por favor revisa.')
        return
    
    def read_movies_class(self):
        self.view.ask('¿Qué clasificación de Películas buscas?: ') 
        id_class = input()
        print('')
        print('id_class')
        print(id_class)
        movie_class = self.model.read_movies_class(id_class)
        print('move det despues de leer el class')
        print(movie_class)
        if type(movie_class)==list:
            self.view.show_md_header('Películas con clasificación '+id_class+' ')
            for movie in movie_class:
                self.view.show_a_movie(movie)
            self.view.show_md_midder()
            self.view.show_md_footer()
        else:
            if movie_class == None:
                self.view.error('ESTE clasificación DE PELÍCULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL clasificación, por favor revisa.')
    
    
    def update_a_movie(self):
        self.view.ask('Introduce el ID de la Película a modificar: ')
        i_movie = input()#Marix
        movie = self.model.read_a_movie(i_movie)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la Película con ID  '+i_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('ESA PELÍCULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER PELÍCULA, por favor revisa.')
            return
        self.view.msg('A continuacion ingrese el nuevo valor.')
        self.view.msg('Deje un espacio vacio en caso de no querer modificar.')
        whole_vals = self.ask_movie_u()
        fields, vals = self.update_lists(['m_title'], whole_vals)
        vals.append(i_movie) 
        vals = tuple(vals)
        out = self.model.update_movie(fields,vals) 
        if out == True:
            self.view.ok(i_movie,' actualizo')
        else:
            self.view.error('PROBLEMA AL LEER LA PELÍCULA, por favor revisa.')
        return
    
    def delete_a_movie(self):
        self.view.ask('Introduce ID de la Película que deseas eliminar: ')
        i_movie = input()
        count = self.model.delete_movie(i_movie)
        if count != 0:
            self.view.ok(i_movie, 'se borro')
        else:
            if count == 0:
                self.view.error('ESTE ID DE TIPO DE PELÍCULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL ELIMINAR PELÍCULA, por favor revisa.')
        return


#Halls____________________________________________________________________________________
    def halls_menu(self):
            o = '0'
            while o != '6':
                self.view.halls_menu()
                self.view.option('6')
                o = input()
                print(' ')
                if o == '1':
                    self.create_hall()
                elif o == '2': 
                    self.read_a_hall_s()
                elif o == '3': 
                    self.read_all_halls()
                elif o == '4': 
                    self.update_a_hall()
                elif o == '5': 
                    self.delete_a_hall()
                elif o == '6': 
                    return
                else:
                    self.view.not_valid_option()

    def ask_hall(self):
        self.view.ask('Cantidad de asientos: ')
        c_seats = input()
        return c_seats
    
    def create_hall(self): 
        c_seats = self.ask_hall()
        out = self.model.create_hall(c_seats)#id de la sala
        
        if type(out) == int:
            print(' ')
            self.view.ok(out, ' agrego como  sala')
            print(' ')
        else:
            self.view.error('NO SE PUDO AGREGAR ESA SALA, por favor revisa!')
    
    def read_a_hall_s(self):
            self.view.ask('Introduce el ID de la Sala que deseas consultar: ')
            id_hall = input()
            print('')
            hall = self.model.read_a_hall_s(id_hall)
            if type(hall)==tuple:
                self.view.show_hall_header('Sala '+id_hall+' ')
                self.view.show_a_hall(hall)
                self.view.show_hall_midder()
                self.view.show_hall_footer()
            else:
                if hall == None:
                    self.view.error('ESTA CLASIFICACIÓN NO EXISTE')
                else:
                    self.view.error('PROBLEMA AL LEER EL CLASIFICACIÓN, por favor revisa.')
        
    def read_all_halls(self):
        halls = self.model.read_all_halls()
        if type(halls) == list:
            self.view.show_hall_header('Estas son todas las Salas que existen: ')
            for hall in halls:
                self.view.show_a_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer
        else:
            self.view.error('PROBLEMA AL LEER LAS SALAS, por favor revisa.')
        return
    
    def update_a_hall(self):
        self.view.ask('Introduce el ID de la Sala que deseas modificar: ')
        id_hall = input()
        out = self.model.read_a_hall(id_hall)
        print('out')
        print(out)
        if type(out) == tuple:
            self.view.show_hall_header('Sala  '+id_hall+' ')
            self.view.show_a_hall(out)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if out == None:
                self.view.error('ESTE ID NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER ID, por favor revisa.')
            return
        self.view.msg('A continuacion ingrese el nuevo valor.')
        self.view.msg('Deje un espacio vacio en caso de no querer modificar.')
        whole_vals = self.ask_hall()
        fields, vals = self.update_lists(['num_seats'], whole_vals)
        vals.append(id_hall) 
        vals = tuple(vals)
        out = self.model.update_a_hall(fields,vals)
        if out == True:
            self.view.ok(id_hall,' actualizo')
        else:
            self.view.error('PROBLEMA AL LEER ID, por favor revisa.')
        return
    
    def delete_a_hall(self):
        self.view.ask('Introduce ID del Detalle de la Sala que desea eliminar: ')
        id_hall = input()
        count = self.model.delete_a_hall(id_hall)
        if count != 0:
            self.view.ok(id_hall, 'se borro')
        else:
            if count == 0:
                self.view.error('ESTE ID DE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL SALA, por favor revisa.')
        return


#Seats____________________________________________________________________________________
    def seats_menu(self):
            o = '0'
            while o != '5':
                self.view.seats_menu()
                self.view.option('5')
                o = input()
                print(' ')
                if o == '1':
                    self.create_seat()
                elif o == '2': 
                    self.read_seats_status_in_hall()#Leer asientos disponibles en sala
                elif o == '3': 
                    self.read_all_seats_hall()#Leer todos asientos en una sala, Admin
                elif o == '4': 
                    self.delete_a_seat()
                elif o == '5': 
                    return
                else:
                    self.view.not_valid_option()

    def ask_seat_c(self):
        self.view.ask('Número de asiento: ')
        n_s = input()
        self.view.ask('Fila del asiento: ')
        r_s = input()
        s_status = 0 
        self.view.ask('Sala: ')
        hall = input()
        return n_s, r_s, s_status, hall
    
    def ask_seat_u(self):
        self.view.ask('Número de asiento: ')
        n_s = input()
        self.view.ask('Fila del asiento: ')
        r_s = input()
        self.view.ask('Estado (0 = Libre, 1 = Ocupado): ')
        s_status = input()
        self.view.ask('Sala: ')
        hall = input()
        return n_s, r_s, s_status, hall
    
    def ask_seat_d(self):
        self.view.ask('Número de asiento: ')
        n_s = input()
        self.view.ask('Fila del asiento: ')
        r_s = input()
        self.view.ask('Sala: ')
        hall = input()
        return n_s, r_s, hall
    
    def create_seat(self): 
        n_s, r_s, s_status, hall = self.ask_seat_c()
        out = self.model.create_seat(n_s, r_s, s_status, hall)
        print(out)
        if out == True:
            print(' ')
            self.view.ok(n_s, ' agrego en la sala')
            print(' ')
        else:
            self.view.error('NO SE PUDO AGREGAR ESA SALA, por favor revisa!')
        
    def read_seats_status_in_hall(self):
        self.view.ask('Introduce la Sala que deseas consultar: ')
        id_h = input()
        seats = self.model.read_seats_status_in_hall(id_h)
        if type(seats) == list:
            self.view.show_seat_header('Estos son todos los Asientos DISPONIBLES en esa Sala: ')
            for seat in seats:
                self.view.show_a_seat_h(seat)
                self.view.show_seat_midder()
                self.view.show_seat_footer
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS, por favor revisa.')
        return
    
    def read_all_seats_hall(self):
        self.view.ask('Introduce la Sala que deseas consultar: ')
        id_h = input()
        print('')
        seats = self.model.read_all_seats_in_hall(id_h)
        if type(seats) == list:
            self.view.show_seat_header('Estas son todos los Asientos que hay en esa Sala: ')
            for seat in seats:
                self.view.show_a_seat(seat)
                self.view.show_seat_midder()
                self.view.show_seat_footer
        else:
            self.view.error('PROBLEMA AL LEER EL, por favor revisa.')
        return
    
    def delete_a_seat(self):
        n_s, r_s, hall = self.ask_seat_d()
        count = self.model.delete_seat( n_s, r_s, hall)
        if count != 0:
            self.view.ok(n_s, 'se borro')
        else:
            if count == 0:
                self.view.error('ESTE ID DE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ASIENTO, por favor revisa.')
        return


#SCH Controller____________________________________________________________________________________
    def sch_menu(self):
        o = '0'
        while o != '8':
            self.view.sch_menu()
            self.view.option('8')
            o = input()
            print(' ')
            if o == '1':
                self.create_sch()
            elif o == '2': 
                self.read_a_sch()
            elif o == '3': 
                self.read_a_sch_today()
            elif o == '4': 
                self.read_a_sch_time()
            elif o == '5': 
                self.read_a_sch_m_d()
            elif o == '6': 
                self.read_a_sch_class()
            elif o == '7': 
                self.update_sch()
            elif o == '8': 
                self.delete_sch()
            elif o == '9': 
                return
            else:
                self.view.not_valid_option()

    def ask_sch(self):
        self.view.ask('ID de la Película para esta Función: ')
        id_m = input()#3
        self.view.ask('Tipo de Projección: ')
        pr = input()#3D
        self.view.ask('ID del Idioma para esta Función: ')
        id_l = input()#Español
        self.view.ask('Fecha para esta Función: ')
        date = input()
        self.view.ask('Hora para esta Función: ')
        time = input()#3
        self.view.ask('ID de la Sala a presentar esta Función: ')
        id_hall = input()#3
        return id_m, pr, id_l, date, time, id_hall 


    def create_sch(self): 
        id_m, pr, id_l, date, time, id_hall = self.ask_sch()
        n_sav = 100
        print('asientos disponibles')
        print(n_sav)
        id_sch = self.model.create_schedule(id_m, pr, id_l, date, time, id_hall, n_sav)
        print('supuesto id de l funcion nueva')
        print(id_sch)
        if type(id_sch) == int:
            self.view.ok(id_sch, ' agrego')
        else:
            if id_sch.errno == 1062:
                self.view.error('ESA FUNCIÓN ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR ESA FUNCIÓN, por favor revisa!')
    
    def read_a_sch(self):
        self.view.ask('Introduce el ID de la Función que deseas consultar: ')
        id_sch = input()
        print('')
        sch = self.model.read_a_sch(id_sch)
        if type(sch) == tuple:
            self.view.show_sch_header('Especificación de la Función '+id_sch+' ')
            self.view.show_a_sch(sch)
            self.view.show_sch_midder()
            self.view.show_sch_footer()
        else:
            if sch == None:
                self.view.error('ESTA FUNCIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL FUNCIÓN, por favor revisa.')
    
    def read_a_sch_time(self):
        self.view.ask('Introduce la Hora de tu preferencia para una Función: ')#Escribir como expresar
        time = input()
        schs = self.model.read_a_sch_time(time)
        if type(schs) == list:
            self.view.show_class_header('Estas son todas las Funciones que coinciden con tus preferencias: ')
            for sch in schs:
                self.view.show_a_sch(sch)
            self.view.show_sch_midder()
            self.view.show_sch_footer
        else:
            self.view.sorry('POR AHORA NO HAY FUNCIONES QUE CUMPLAN CON TUS PREFERENCIAS :( ')
        return
    
    def read_a_sch_today(self):
            today = self.model.read_today()
            schs = self.model.read_a_sch_today2(today)
            if type(schs) == list:
                self.view.show_sch_header('CARTELERA DE HOY: ')
                for sch in schs:
                    self.view.show_a_sch(sch)
                    self.view.show_sch_midder()
                    self.view.show_sch_footer
            else:
                self.view.sorry('POR AHORA NO HAY FUNCIONES QUE CUMPLAN CON TUS PREFERENCIAS :( ')
            return

    def read_a_sch_m_d(self):
        self.view.ask('Introduce la Pelicula que buscas: ')#Escribir como expresar
        id_m = input()
        self.view.ask('Introduce la Fecha de tu preferencia para una Función: ')#Escribir como expresar
        date = input()
        schs = self.model.read_a_sch_movie_date(id_m, date)
        if type(schs) == list:
            self.view.show_class_header('Estas son todas las Funciones que coinciden con tus preferencias: ')
            for sch in schs:
                self.view.show_a_sch(sch)
            self.view.show_sch_midder()
            self.view.show_sch_footer
        else:
            self.view.sorry('POR AHORA NO HAY FUNCIONES QUE CUMPLAN CON TUS PREFERENCIAS :(')
        return
    
    def read_a_sch_class(self):
        self.view.ask('Introduce la Clasificación de la Pelicula que buscas: ')#Escribir como expresar
        id_c = input()
        schs = self.model.read_a_sch_movie_class(id_c)
        if type(schs) == list:
            self.view.show_class_header('Estas son todas las Funciones que coinciden con tus preferencias: ')
            for sch in schs:
                self.view.show_a_sch(sch)
            self.view.show_sch_midder()
            self.view.show_sch_footer
        else:
            self.view.sorry('POR AHORA NO HAY FUNCIONES QUE CUMPLAN CON TUS PREFERENCIAS :( ')
        return
    
    def update_sch(self):
        self.view.ask('Introduce el ID de la Función a modificar: ')
        i_sch = input()#
        sch = self.model.read_a_sch(i_sch)
        if type(sch) == tuple:
            self.view.show_sch_header('Datos de la Función con ID  '+i_sch+' ')
            self.view.show_a_sch(sch)
            self.view.show_sch_midder()
            self.view.show_sch_footer()
        else:
            if i_sch == None:
                self.view.error('ESTA FUNCIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER FUNCACIÓN, por favor revisa.')
            return
        self.view.msg('A continuacion ingrese el nuevo valor.')
        self.view.msg('Deje un espacio vacio en caso de no querer modificar.')
        whole_vals = self.ask_sch()
        fields, vals = self.update_lists(['id_movie', 'id_proj', 'id_lang', 'm_date', 'm_time', 'id_hall'], whole_vals)    
        vals.append(i_sch) 
        out = self.model.update_schedule(fields,vals) 
        if out == True:
            self.view.ok(i_sch,' actualizo')
        else:
            self.view.error('PROBLEMA AL LEER LA FUNCIÓN, por favor revisa.')
        return
    
    def delete_sch(self):
        self.view.ask('Introduce ID de la Función que desea eliminar: ')
        i_sch = input()
        count = self.model.delete_schedule(i_sch)
        if count != 0:
            self.view.ok(i_sch, 'se borro')
        else:
            if count == 0:
                self.view.error('ESTA FUNCIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA FUNCIÓN, por favor revisa.')
        return


#Type of tickets Controller____________________________________________________________________________________
    def tt_menu(self):
        o = '0'
        while o != '6':
            self.view.tt_menu()
            self.view.option('6')
            o = input()
            print(' ')
            if o == '1':
                self.create_tt()
            elif o == '2': 
                self.read_a_tt()
            elif o == '3': 
                self.read_all_tts()
            elif o == '4': 
                self.update_a_tt()
            elif o == '5': 
                self.delete_a_tt()
            elif o == '6': 
                return
            else:
                self.view.not_valid_option()

    def ask_tt_c(self):
        self.view.ask('Precio de este boleto: ')
        price = input()#3
        return price
    
    def ask_tt_u(self):
        self.view.ask('Precio de este boleto: ')
        price = input()#3
        return [price]
    
    def create_tt(self): 
        self.view.ask('Introduce que tipo de boleto deseas crear: ')
        id_tt = input() #AA
        price = self.ask_tt_c()#3
        out = self.model.create_a_tt(id_tt, price)#(AA,3)
        if out == True:
            self.view.ok(id_tt, ' agrego')
        else:
            if out.errno == 1062:
                self.view.error('ESE TIPO DE BOLETO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR ESE TIPO DE BOLETO, por favor revisa!')
    
    def read_a_tt(self):
        self.view.ask('Introduce que tipo de boleto deseas consultar: ')
        id_tt = input()
        print('')
        tt = self.model.read_a_pt(id_tt)
        if type(tt)==tuple:
            self.view.show_tt_header('Especificación del Boleto '+id_tt+' ')
            self.view.show_a_tt(tt)
            self.view.show_tt_midder()
            self.view.show_tt_footer()
        else:
            if tt == None:
                self.view.error('ESTA CLASIFICACIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CLASIFICACIÓN, por favor revisa.')
    
    def read_all_tts(self):
        tts = self.model.read_all_tts()
        if type(tts) == list:
            self.view.show_tt_header('Estas son todos los Tipos de Boleto que existen: ')
            for tt in tts:
                self.view.show_a_tt(tt)
                print('----------------------------------')
            self.view.show_tt_midder()
            self.view.show_tt_footer
        else:
            self.view.error('PROBLEMA AL LEER LOS BOLETOS, por favor revisa.')
        return
    
    def update_a_tt(self):
        self.view.ask('Introduce el Tipo de Boleto a modificar: ')
        i_tt = input()#AA
        tts = self.model.read_a_class(i_tt)
        if type(tts) == tuple:
            self.view.show_tt_header('Datos de la Clasificación con ID  '+i_tt+' ')
            self.view.show_a_tt(tts)
            self.view.show_tt_midder()
            self.view.show_tt_footer()
        else:
            if tts == None:
                self.view.error('ESTE BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER BOLETO, por favor revisa.')
            return
        self.view.msg('A continuacion ingrese el nuevo valor.')
        self.view.msg('Deje un espacio vacio en caso de no querer modificar.')
        whole_vals = self.ask_tt_u()
        fields, vals = self.update_lists(['type_c','price'], whole_vals)
        vals.append(i_tt) 
        vals = tuple(vals)
        out = self.model.update_a_tt(fields,vals)
        if out == True:
            self.view.ok(i_tt,' actualizo')
        else:
            self.view.error('PROBLEMA AL LEER EL BOLETO, por favor revisa.')
        return
    
    def delete_a_tt(self):
        self.view.ask('Introduce Tipo de Boleto que deseas eliminar: ')
        i_tt = input()
        count = self.model.delete_a_tt(i_tt)
        if count != 0:
            self.view.ok(i_tt, 'se borro')
        else:
            if count == 0:
                self.view.error('ESTE TIPO DE BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA CLASIFICACIÓN, por favor revisa.')
        return


#Buy ticket____________________________________________________________________________________
    def choose_seats(self, id_hall):
            self.view.ask('                      Elige la fila de tu Asiento: ')
            id_sr = input()#Fila (A, B, C)
            self.view.ask('                      Elige tu Asiento preferido: ')
            id_s = input()#Asiento (1,2,3)
            seat_status = self.model.read_seat(id_s, id_sr, id_hall)#Aseguramos que el lugar esta desocupado
            return seat_status, id_s, id_sr

    def ask_tickets(self, id_sch, id_pch, i, id_hall):#Paso 4
            print('                      Para boleto: ', i + 1)
            self.view.ask('                      Ingresa el tipo de boleto: ')
            id_tt = input()#tipo de boleto
            p_t = self.model.read_a_pt(id_tt) #leo precio del boleto
            seat_status, id_s, id_sr = self.choose_seats(id_hall)
            if seat_status == 0:
                update_seat = self.model.update_seat(id_s, id_sr, id_hall)#Si esto se logro continua, HACER IF 
                #if update_seat == True:
                id_tx = self.model.create_a_tp(id_sch, id_tt, id_s, id_sr)#Creo un boleto con sus especificaciones, asientos, funcion, etc
                if type(id_tx) == int:
                    print('                      Boleto apartado')
                    #Aqui podria guardar para despues deplegar en pantalla detalles de cada boleto
                    out_pd = self.model.create_a_pch_det(id_pch, id_tx, p_t[0])#(id_compra, id_boleto, precio_boleto)
                    if out_pd == True: 
                        return p_t[0] #Regreso el $$$$ del boleto
                    else:
                        self.view.error('                      No se ha podido crear el detalle de la compra')
                        return 0
                else:
                    self.view.error('Ha ocurrido un error inesperado')
                    return 0
                #else:
                #        self.view.error('Ha ocurrido un error inesperado')
                #       return 0
            else:
                self.view.sorry('Ese asiento ya esta apartado.')
                return 0
    
    def choose_tickets(self, id_pch):#Paso 3
        self.view.ask('                      ¿A qué Función te gustaria asistir?: ')
        id_sch = input()#función
        id_hall = self.model.read_a_sch_hall(id_sch)
        print('                      ¿Cuántos Boletos deseas comprar?')
        n_tk= input()
        n = int(n_tk)
        n_total = 0
        for i in range(n):
            n_total += self.ask_tickets(id_sch, id_pch, i, id_hall)#Le mando la cantidad de boletos que quiero comprar y regresa los id de los tickets
        print('total')
        print(n_total)
        return n_total

    def create_purchase(self, id_cl):# Paso2, tickets lista con ids de los tck
        today = date.today()
        total = 0.0
        id_pch = self.model.create_a_pch(id_cl, today, total)#CREO COMPRA
        if type(id_pch) == int:
            print('                      Agreguemos los boletos a tu compra :) ')
            print(' ')
            total = self.choose_tickets(id_pch)
            self.model.update_pch_total(id_pch, total)
            return id_pch
        else:
            self.view.error('NO SE PUDO REALIZAR LA COMPRA')
            
    def buy_tickets(self, id_client):#Paso 1 (Se supone que ya sabes a que Número de función entraras)
        id_pch = self.create_purchase(id_client)
        if type(id_pch) == int:
            print('                    *********************************************************************************')
            print('                      ¡Tus boleto shan sido apartados correctamente! :)')
            print('                    ---------------------------------------------------------------------------------')
            print('                      Esperamos tu pago en TAQUILLA minimo 10 minutos antes de tu función')
            print('                      De lo contrario tu(s) botelo(s) seran puestos de nuevo en venta')
            print('                    *********************************************************************************')
        else:
            self.view.error('NO SE PUDO REALIZAR LA COMPRA, por favor revisa!')
        
