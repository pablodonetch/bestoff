function buscador(){
    if(document.getElementById('Buscar').value==0)
    {
        return false;
    }
    window.location="/propiedades/buscador?buscar="+document.getElementById('Buscar').value;
}