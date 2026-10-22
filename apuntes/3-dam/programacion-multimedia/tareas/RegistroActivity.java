package com.milito.agenda;

import android.content.ContentValues;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class RegistroActivity extends AppCompatActivity {

    private EditText etNombre, etTelefono, etEmail;
    private int idContacto = -1;
    private AdminSQLiteOpenHelper conSql;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registro);

        etNombre = findViewById(R.id.etNombre);
        etTelefono = findViewById(R.id.etTelefono);
        etEmail = findViewById(R.id.etEmail);
        Button btnCrear = findViewById(R.id.btnCrear);

        conSql = new AdminSQLiteOpenHelper(this, "agenda", null, 1);

        Bundle datos = getIntent().getExtras();
        if (datos != null){
            idContacto = datos.getInt("id");
            etNombre.setText(datos.getString("nombre"));
            etTelefono.setText(datos.getString("telefono"));
            etEmail.setText(datos.getString("email"));

            btnCrear.setText("Actualizar");
            setTitle("Actualizar contacto");

        }

        btnCrear.setOnClickListener(v-> guardar());
        findViewById(R.id.btnCancelar).setOnClickListener(v-> finish());


    }

    private void guardar(){
        String nombre = etNombre.getText().toString().trim();
        String telefono = etTelefono.getText().toString().trim();
        String email = etEmail.getText().toString().trim();

        if (nombre.isEmpty() || telefono.isEmpty() || email.isEmpty()) {
            Toast.makeText(this, "Rellena todos los campos", Toast.LENGTH_SHORT).show();
            return;
        }

        SQLiteDatabase db = conSql.getWritableDatabase();
        ContentValues registro = new ContentValues();
        registro.put("nombre", nombre);
        registro.put("telefono", telefono);
        registro.put("email", email);

        if (idContacto==-1) {
            long res = db.insert("contactos", null, registro);
            if (res != -1) {
                Toast.makeText(this, "Contacto creado correctamente", Toast.LENGTH_SHORT).show();
                finish();
            }
        }else {
            int cantidad = db.update("contactos", registro, "id=" + idContacto, null);
            if(cantidad>0){
                Toast.makeText(this, "Contacto actualizado correctamente", Toast.LENGTH_SHORT).show();
                finish();

            }
            db.close();
            finish();

        }

    }

}
