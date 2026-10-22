package com.example.examen;


import android.content.Context;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.widget.Toast;

public class BDEntradas extends SQLiteOpenHelper {

    Context contexto;

    static String createBDSQL ="CREATE TABLE entradas (id integer primary key autoincrement, partido text, precio float, cantidad integer, sitio text)";


    public BDEntradas(Context context, String entradas, Object o, int i){
        super(context.getApplicationContext(),"BDEntradas",null,1 );
        contexto=context;
    }



    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase) {
        try {
            sqLiteDatabase.execSQL(createBDSQL);
        }catch (SQLException e){
            Toast.makeText(contexto, "Error al crear la base de datos "+e, Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, int i, int i1) {
        try {
            sqLiteDatabase.execSQL("DROP TABLE IF EXISTS contacto");
            onCreate((sqLiteDatabase));
        }catch (SQLException e){
            Toast.makeText(contexto, "Error al actualizar la base de datos "+e,Toast.LENGTH_SHORT).show();
        }
    }

}