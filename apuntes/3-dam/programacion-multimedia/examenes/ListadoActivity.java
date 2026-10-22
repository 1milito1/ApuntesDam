package com.example.examen;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ListView;

import java.util.ArrayList;

public class ListadoActivity extends AppCompatActivity {

    ListView lvListado;
    Button btnVolverListado;
    Adaptador adaptador;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_listado);

        lvListado = findViewById(R.id.lvListado);
        btnVolverListado = findViewById(R.id.btnVolverListado);
        ArrayList<Entrada> entrada = new ArrayList<>();
        adaptador = new Adaptador(this, entrada);

        lvListado.setAdapter(adaptador);


        btnVolverListado.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });


    }
}