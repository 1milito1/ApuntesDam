package com.milito.agenda;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Objects;

public class ContactoAdapter extends BaseAdapter {

    private Context context;
    private ArrayList<Contacto> lista;

    public ContactoAdapter(Context context, ArrayList<Contacto> lista) {
        this.context = context;
        this.lista = lista;
    }

    @Override
    public int getCount() {
        return lista.size();
    }

    @Override
    public Object getItem(int i) {
        return lista.get(i);
    }

    @Override
    public long getItemId(int i) {
        return lista.get(i).getId();
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        if (view == null) {
            view = LayoutInflater.from(context).inflate(R.layout.item_contacto, viewGroup, false);
        }

        Contacto c = lista.get(i);
        TextView nombre = view.findViewById(R.id.tvFilaNombre);
        TextView telefono = view.findViewById(R.id.tvFilaTelefono);
        TextView email = view.findViewById(R.id.tvFilaEmail);

        nombre.setText(c.getNombre());
        telefono.setText(c.getTelefono());
        email.setText(c.getEmail());

        return view;


    }

}

