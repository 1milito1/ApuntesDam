package com.example.examen;

import static java.lang.reflect.Array.getInt;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Spinner;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText etPrecio,etEntradas;
    Button btnRegistrar,btnListado;
    Spinner spPartido;
    RadioGroup radioGroup;
    RadioButton rbGrada1, rbGrada2;
    private int posicion;
    SQLiteDatabase db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etPrecio = findViewById(R.id.etPrecio);
        etEntradas = findViewById(R.id.etEntradas);
        btnRegistrar = findViewById(R.id.btnRegistrar);
        btnListado = findViewById(R.id.btnListado);
        spPartido = findViewById(R.id.spPartido);
        radioGroup = findViewById(R.id.radioGroup);
        rbGrada1 = findViewById(R.id.rbGrada1);
        rbGrada2 = findViewById(R.id.rbGrada2);
        BDEntradas bdEntradas = new BDEntradas(getApplicationContext(), "entradas", null, 1);

        db = bdEntradas.getReadableDatabase();

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                R.array.partidos, android.R.layout.simple_spinner_item);

        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        spPartido.setAdapter(adapter);

        spPartido.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {

                if(position == 0){
                    etPrecio.setText("20");
                } else if (position == 1) {
                    etPrecio.setText("30");

                } else if (position == 2) {
                    etPrecio.setText("50");

                }else if (position == 3){
                    etPrecio.setText("100");
                }


            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });



        btnRegistrar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (etEntradas.getText().toString().isEmpty()) {
                    Toast.makeText(getApplicationContext(), "Rellena los campos", Toast.LENGTH_SHORT).show();


                } else {


                    Intent i = new Intent(getApplicationContext(), RegistrarActivity.class);


                    startActivity(i);
                }
            }
        });
        btnListado.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), ListadoActivity.class);
                startActivity(intent);
            }
        });

    }

}








