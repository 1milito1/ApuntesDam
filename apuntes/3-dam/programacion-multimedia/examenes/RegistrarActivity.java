package com.example.examen;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.android.material.bottomappbar.BottomAppBar;

public class RegistrarActivity extends AppCompatActivity {

    TextView tvPartido, tvPrecio, tvEntrada, tvGrada, tvTotal;
    Button btnVolver;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registrar);

        tvPartido = findViewById(R.id.tvPartido);
        tvPrecio = findViewById(R.id.tvPrecio);
        tvEntrada = findViewById(R.id.tvEntradas);
        tvGrada = findViewById(R.id.tvGrada);
        tvTotal = findViewById(R.id.tvTotal);
        btnVolver =findViewById(R.id.btnVolver);

        btnVolver.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });


    }

}