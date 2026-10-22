package com.example.examen;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.ArrayList;

public class Adaptador extends BaseAdapter {
    private Context context;
    private ArrayList<Entrada> listaAdapter;

    public Adaptador(Context context, ArrayList<Entrada> listaAdapter) {
        this.context = context;
        this.listaAdapter = listaAdapter;
    }

    @Override
    public int getCount() {
        return listaAdapter.size();
    }

    @Override
    public Object getItem(int position) {
        return listaAdapter.get(position);
    }

    @Override
    public long getItemId(int position) {
        return listaAdapter.get(position).getId();
    }

    @Override
    public View getView(int position, View view, ViewGroup parent) {
        LayoutInflater layoutInflater= LayoutInflater.from(context);
        view = layoutInflater.inflate(R.layout.item_listado, null);
        TextView tvIdList =(TextView)view.findViewById(R.id.tvIdList);
        TextView tvPartidoList=(TextView)view.findViewById(R.id.tvPartidoList);
        TextView tvCantidadList =(TextView) view.findViewById(R.id.tvCantidadList);
        TextView tvSitioList =(TextView) view.findViewById(R.id.tvSitioList);
        tvIdList.setText(listaAdapter.get(position).toString());
        tvPartidoList.setText(listaAdapter.get(position).toString());
        tvCantidadList.setText(listaAdapter.get(position).toString());
        tvSitioList.setText(listaAdapter.get(position).toString());
        return view;
    }
}
