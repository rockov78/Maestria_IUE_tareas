use rustatistics_2::calcular_promedio_movil;

fn main() {
    let numeros = vec![4, 1, 2, 2, 3, 4, 4, 1, 1, 2];
    let ventana = 3;
    
    let promedio_movil = calcular_promedio_movil(&numeros, ventana);
    
    println!("Promedio móvil: {:?}", promedio_movil);
}