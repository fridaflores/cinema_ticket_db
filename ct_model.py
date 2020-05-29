from mysql import connector

class Model: 
    def __init__(self, config_db_file='ct_config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
        
    def close_db(self):
        self.cnx.close()

#___________________________________________CRUD Methods___________________________________________________________________
#Users Accounts________________________________________________________________________________________________________________________________________
    def create_user_acc(self, id_type_user, u_fname, u_sname1, u_sname2, u_password):#Admin
        try:
            sql = 'INSERT INTO users_acc (`id_user`,`u_fname`,`u_sname1`,`u_sname2`,`u_password`) VALUES (%s, %s, %s, %s, %s)' 
            vals = (id_type_user, u_fname, u_sname1, u_sname2, u_password)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_u_a = self.cursor.lastrowid
            return id_u_a #Regresa el id del usuariopara que sepa 
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def read_a_user_acc(self, id_uacc):#Admin
        try:
            sql = 'SELECT id_uacc, id_user, u_fname, u_sname1 FROM users_acc WHERE id_uacc = %s' 
            vals = (id_uacc,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_all_users_acc(self):#Admin
        try:
            sql = 'SELECT id_uacc, id_user, u_fname, u_sname1 FROM users_acc'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def update_user_acc(self, fields, vals):#Admin
        try:
            sql = 'UPDATE users_acc SET '+','.join(fields)+' WHERE id_uacc = %s' 
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_user_acc(self, id_uacc):#Admin
        try:
            sql = 'DELETE FROM users_acc WHERE id_uacc = %s'
            vals = (id_uacc,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 

#Users Login__________________________________________________________________________________________________
#Clients------------------------------------------------------------------------------------------------------
    def cl_access(self, c_id, c_password):#Incluir que cheque tipo de usuario, Admin
        try:
            sql = 'SELECT id_uacc, u_password FROM users_acc WHERE id_uacc = %s' #aqui pedir tipo tambien
            vals = (c_id,)
            self.cursor.execute(sql, vals)
            out = self.cursor.fetchone()
            input = (c_id, c_password)
            if out == input:
                return True
            else:
                return False
        except connector.Error as err:
            return err 

#Admin------------------------------------------------------------------------------------------------------
    def ad_access(self, c_id, c_password):#Incluir que cheque tipo de usuario, Admin
        try:
            sql = 'SELECT id_uacc, u_password FROM users_acc WHERE id_uacc = %s' #aqui pedir tipo tambien
            vals = (c_id,)
            self.cursor.execute(sql, vals)
            out = self.cursor.fetchone()
            input = (c_id, c_password)
            if out == input:
                return True
            else:
                return False
        except connector.Error as err:
            return err 


#Classifications________________________________________________________________________________________________
    def create_a_class(self, m_class, min_age):#Admin
        try:
            sql = 'INSERT INTO classifications (`class`,`m_min_app_age`) VALUES (%s,%s)' 
            vals = (m_class, min_age)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
        
    def read_a_class(self,m_class):#Admin
        try:
            sql = 'SELECT * FROM classifications WHERE class = %s' 
            vals = (m_class,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_all_classifications(self):#Admin
        try:
            sql = 'SELECT * FROM classifications'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def update_a_class(self, fields, vals):#Admin
        try:
            sql = 'UPDATE classifications SET '+','.join(fields)+' WHERE class = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_a_class(self, m_class):#Admin
        try:
            sql = 'DELETE FROM classifications WHERE class = %s'
            vals = (m_class,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 

#Genres______________________________________________________________________________________________________
    def create_genre(self, id_gen):#Admin
        try:
            sql = 'INSERT INTO genres (`id_gen`) VALUES (%s)' 
            vals = (id_gen,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def read_all_genres(self):#Admin
        try:
            sql = 'SELECT * FROM genres'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def update_genre(self, fields, vals):#Admin
        try:
            sql = 'UPDATE genres SET '+','.join(fields)+' WHERE id_gen = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_genre(self,id_gen):#Admin
        try:
            sql = 'DELETE FROM genres WHERE id_gen = %s'
            vals = (id_gen,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 


#Languages____________________________________________________________________________________________________________
    def create_language(self,id_lang, subtitles):#Admin
        try:
            sql = 'INSERT INTO languages(`id_lang`, `subtitles`) VALUES (%s,%s)' 
            vals = (id_lang, subtitles)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
        
    def read_a_language(self,id_lang):#Admin, users en el horario de pelis
        try:
            sql = 'SELECT * FROM languages WHERE id_lang = %s' 
            vals = (id_lang,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def update_language(self, fields, vals):#Admin
        try:
            sql = 'UPDATE languages SET '+','.join(fields)+' WHERE id_lang = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_language(self, id_lang):#Admin
        try:
            sql = 'DELETE FROM languages WHERE id_lang = %s'
            vals = (id_lang,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 

#Movies_________________________________________________________________________________________________
    def create_movie(self, m_title):#Admin
        try:
            sql = 'INSERT INTO movies(`m_title`) VALUES (%s)' 
            vals = (m_title,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_movie = self.cursor.lastrowid
            return id_movie
        except connector.Error as err:
            self.cnx.rollback()
            return err 
        
    def read_a_movie(self,id_movie):#Muestra solo el ID y el título de la película, Admin y cliente
        try:
            sql = 'SELECT * FROM movies WHERE id_movie = %s' 
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 
    
    def read_movie_ad(self,id_movie):#Muestra el título de la pélicula, género y clasificación-> Admin y cliente
        try:
            sql = 'SELECT movies.m_title, movie_det.id_gen, movie_det.id_class FROM movie_det JOIN movies ON movie_det.id_movie = movies.id_movie WHERE movie_det.id_movie = %s'  
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_all_movies(self):#Muestra sólo el título de las péliculas #Admin
        try:
            sql = 'SELECT * FROM movies'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def read_movies_class(self, id_class):#Sólo muestra películas con cierta clasificación #Admin y cliente
        try:
            sql = 'SELECT movies.m_title, movie_det.id_gen, movie_det.id_class FROM movie_det JOIN movies ON movies.id_movie = movie_det.id_movie WHERE movie_det.id_class = %s'
            vals = (id_class,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def update_movie(self, fields, vals):#Admin
        try:
            sql = 'UPDATE movies SET '+','.join(fields)+' WHERE id_movie = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_movie(self, id_movie):#Admin
        try:
            sql = 'DELETE FROM movies  WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    

#Movie Details______________________________________________________________________________________________________________________________
    def create_m_det(self,id_movie,id_gen,id_class):#Admin
        try:
            sql = 'INSERT INTO movie_det(`id_movie`,`id_gen`,`id_class`) VALUES (%s,%s,%s)'
            vals = (id_movie, id_gen, id_class)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_m_det(self, id_movie):#Admin y admin en el horario
        try:
            sql = 'SELECT genres.*, classifications.* FROM movie_det JOIN genres ON movie_det.id_gen = genres.id_gen JOIN classifications ON movie_det.id_class = classifications.class'
            vals = (id_movie,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err


    def update_a_m_det(self, fields, vals):#Admin
        try:
            sql = 'UPDATE movie_det SET '+','.join(fields)+' WHERE id_movie = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_a_movie_det(self, id_movie):#Admin
        try:
            sql = 'DELETE FROM movie_det WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 

#Halls_______________-________________________________________________________________________________________________
    def create_hall(self, num_s):#Admin
        try:
            sql = 'INSERT INTO halls(`num_seats`) VALUES (%s)' 
            vals = (num_s,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_h = self.cursor.lastrowid
            print('idh')
            print(id_h)
            return id_h
        except connector.Error as err:
            self.cnx.rollback()
            return err 
        
    def read_a_hall(self, id_hall):#Admin
        try:
            sql = 'SELECT * FROM halls WHERE id_hall = %s' 
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 
    

    def read_a_hall_s(self, id_hall):#Ver todos los asientos en una sala
        try:
            sql = 'SELECT halls.id_hall, seats.* FROM halls JOIN seats ON halls.id_hall = seats.id_hall WHERE id_hall = %s' 
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_all_halls(self):#Admin
        try:
            sql = 'SELECT * FROM halls'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def update_a_hall(self, fields, vals):#Admin
        try:
            sql = 'UPDATE halls SET '+','.join(fields)+' WHERE id_hall = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_a_hall(self, id_hall):#Admin
        try:
            sql = 'DELETE FROM halls WHERE id_hall = %s'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def ch_hall(self, id_hall):
        try:
            s = 0
            sql = 'SELECT COUNT(*) FROM seats JOIN halls on seats.id_hall = halls.id_hall WHERE halls.id_hall = %s and s_status = %s ' 
            vals = (id_hall, s)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    
#Seats_____________________________________________________________________________________________________________
    def create_seat(self, id_seat, id_row, s_status, id_hall): #admin
        try:
            sql = 'INSERT INTO seats(`id_seat`,`id_row`,`s_status`,`id_hall`) VALUES(%s,%s,%s,%s)' 
            vals = (id_seat, id_row, s_status, id_hall)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def read_seat(self, id_s, id_r, id_hall):#Devuelve 0->si esta vacio el asientoo 1->si esta ocupado
        try:
            sql = 'SELECT s_status FROM seats WHERE id_seat = %s and id_row = %s and id_hall = %s'   
            vals = (id_s, id_r, id_hall)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record[0]
        except connector.Error as err:
            return err 

    #BUSQUEDA POR HACIENTOS DIPONIBLES EN SALA
    def read_seats_status_in_hall(self, id_hall):#Admin
        try:
            s_status = 0
            sql = 'SELECT seats.id_seat, seats.id_row FROM seats WHERE id_hall = %s and s_status = %s'   
            vals = (id_hall, s_status)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            print('holaa?')
            print(records)
            return records
        except connector.Error as err:
            return err 
    
    def read_all_seats_in_hall(self, id_hall):#Leer todos asientos en una sala, Admin
        try:
            sql = 'SELECT * FROM seats WHERE id_hall = %s'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            print('holaa?')
            print(records)
            return records
        except connector.Error as err:
            return err 

    def update_seat(self, id_s, id_sr, id_h):#Admin MODIFICARRRR
        try:
            vals = (id_s, id_sr, id_h)
            sql = 'UPDATE seats SET id_seat = %s and id_row = %s WHERE id_hall = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_seat(self, id_seat, id_row, id_hall):#Admin
        try:
            sql = 'DELETE FROM seats WHERE id_seat = %s and id_row= %s and id_hall= %s'
            vals = (id_seat, id_row)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 


#Schedules___________________________________________________________________________________________________________________
    def create_schedule(self, id_movie, id_proj, id_lang, m_date, m_time, id_hall, num_seats):
        try:
            sql = 'INSERT INTO schedules(`id_movie`, `id_proj`,`id_lang`,`m_date`,`m_time`,`id_hall`,`num_seats`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            vals = (id_movie, id_proj, id_lang, m_date, m_time, id_hall, num_seats)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            id_sch = self.cursor.lastrowid
            return id_sch
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_sch(self, id_s): #Se usa al actualizar
        try:
            sql = 'SELECT schedules.*, movie_det.id_gen, movie_det.id_class FROM schedules JOIN movies ON schedules.id_movie = movies.id_movie JOIN movie_det ON movies.id_movie = movie_det.id_movie WHERE id_sch = %s'
            vals = (id_s,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_sch_hall(self, id_s): #Se usa al actualizar
        try:
            sql = 'SELECT id_hall FROM schedules WHERE id_sch = %s'
            vals = (id_s,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record[0]
        except connector.Error as err:
            return err
    

    def read_a_sch_time(self, time): #Pelis a cierta hora en cierta fecha
        try:
            sql = 'SELECT * FROM schedules WHERE m_time = %s'
            vals = (time,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_a_sch_movie_date(self, m_title, date): #una peli cierto dia
        try:
            sql = 'SELECT * FROM schedules WHERE m_title = %s and m_date = %s'
            vals = (m_title, date)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err #SELECT CURDATE();
    
    def read_today(self): #una peli cierto dia
        try:
            sql = 'SELECT CURDATE()'
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_a_sch_today2(self, date): #Pelis de hoy (cartelera)
        try:
            sql = 'SELECT schedules.id_sch, movies.m_title, schedules.id_proj, schedules.id_lang, m_date, m_time FROM schedules JOIN movies ON schedules.id_movie = movies.id_movie WHERE m_date = %s'
            vals = (date)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_a_sch_movie_class(self, id_class):#todas las funciones con cierto genero en sus peli
        try:
            sql = 'SELECT schedules.*, movie_det.id_gen, movie_det.id_class FROM schedules JOIN movies ON schedules.id_movie = movies.id_movie FROM movies JOIN movie_det ON movies.id_movie = movie_det.id_movie WHERE movie_det.id_class = %s'#Faltaagregar el dia
            vals = (id_class,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def update_schedule(self, fields, vals):
        try:
            sql ='UPDATE schedules SET '+','.join(fields)+' WHERE id_sch = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_schedule(self, id_sch):
        try:
            sql = 'DELETE FROM schedules WHERE id_sch = %s'
            vals = (id_sch,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 

#Type of Tickets________________________________________________________________________________________________
    def create_a_tt(self, type_c, price):#Admin
        try:
            sql = 'INSERT INTO tc_price (`type_c`,`price`) VALUES (%s,%s)' 
            vals = (type_c, price)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
        
    def read_a_pt(self, type_c):#Admin
        try:
            sql = 'SELECT price FROM tc_price WHERE type_c = %s' 
            vals = (type_c,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_all_tts(self):#Admin
        try:
            sql = 'SELECT * FROM tc_price '
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def update_a_tt(self, fields, vals):#Admin
        try:
            sql = 'UPDATE tc_price SET '+','.join(fields)+' WHERE type_c = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_a_tt(self, type_c):#Admin
        try:
            sql = 'DELETE FROM tc_price WHERE type_c = %s'
            vals = (type_c,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    

#Purchase________________________________________________________________________________________________
    def create_a_pch(self, id_client, date, total):#Admin, El date lo mando desde el controlador
        try:
            sql = 'INSERT INTO purchase (`id_client`,`p_date`,`total`) VALUES (%s,%s,%s)' 
            vals = (id_client, date, total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_pch = self.cursor.lastrowid
            return id_pch
        except connector.Error as err:
            self.cnx.rollback()
            return err 
        
    def read_a_pch(self, id_order):#Admin
        try:
            sql = 'SELECT users_acc.u_fname, users_acc.u_sname1, users_acc.u_sname2 FROM purchase JOIN users_acc ON purchase.id_client = users_acc.id_user WHERE id_order = %s' 
            vals = (id_order,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_all_pch(self):#Admin
        try:
            sql = 'SELECT * FROM purchase'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 
    
    def read_all_pch_day(self, day):#Admin
        try:
            sql = 'SELECT users_acc.u_fname, users_acc.u_sname1, users_acc.u_sname2 FROM purchase JOIN users_acc ON purchase.id_client = users_acc.id_user WHERE p_date = %s'
            vals = (day,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 
    

    def read_all_pch_client(self, id_client):#Admin
        try:
            sql = 'SELECT users_acc.u_fname, users_acc.u_sname1, users_acc.u_sname2 FROM purchase JOIN users_acc ON purchase.id_client = users_acc.id_user WHERE id_client = %s'
            vals = (id_client,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def update_a_pch(self, fields, vals):#Admin
        try:
            sql = 'UPDATE purchase SET '+','.join(fields)+' WHERE id_p = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def update_pch_total(self, id_p, total):#Admin
        try:
            sql = 'UPDATE purchase SET total = %s WHERE id_p = %s'
            vals = (id_p, total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_a_pch(self, id_p):#Admin
        try:
            sql = 'DELETE FROM purchase WHERE id_p = %s'
            vals = (id_p,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 


#Purchase Detail________________________________________________________________________________________________
    def create_a_pch_det(self, id_p, id_t, total_p):#Admin
        try:
            sql = 'INSERT INTO purchase_det (`id_p`,`id_t`,`total_t`) VALUES (%s,%s,%s)' 
            vals = (id_p, id_t, total_p)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

     #queda pendiente porque debo hacer CRUD para boletos primero
    """   
    def read_a_pch_det(self, id_order):#Admin
        try:
            sql = 'SELECT users_acc.u_fname, users_acc.u_sname1, users_acc.u_sname2 FROM purchase JOIN users_acc ON purchase.id_client = users_acc.id_user WHERE id_order = %s' 
            vals = (id_order,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 
    """

    def update_a_pch_det(self, fields, vals):#Admin
            try:
                sql = 'UPDATE purchase_det SET '+','.join(fields)+' WHERE id_p = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err 

    def delete_a_pch_det(self, id_p):#Admin
        try:
            sql = 'DELETE FROM purchase_det WHERE id_p = %s'
            vals = (id_p,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 


#Tickets Purchase________________________________________________________________________________________________
    def create_a_tp(self, id_sch, id_tt, id_s, id_rs):#Admin
        try:
            sql = 'INSERT INTO ticket_p (`id_sch`,`id_tt`,`id_s`,`id_rs`) VALUES (%s,%s,%s,%s)' 
            vals = (id_sch, id_tt, id_s, id_rs)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_t = self.cursor.lastrowid
            return id_t
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    """"   
    def read_a_tp(self, type_c):#Admin
        try:
            sql = 'SELECT * FROM tc_price WHERE type_c = %s' 
            vals = (type_c,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 
    
    def read_all_ttp(self):#Todos los boletos comprados por un cliente cierto dia
        try:
            sql = 'SELECT * FROM tc_price '
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 
    """

    def update_a_tp(self, fields, vals):#Admin
        try:
            sql = 'UPDATE ticket_p SET '+','.join(fields)+' WHERE id_t = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_a_tp(self, id_t):#Admin
        try:
            sql = 'DELETE FROM ticket_p WHERE id_p = %s'
            vals = (id_t,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    










                    
