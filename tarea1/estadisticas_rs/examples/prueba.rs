use estadisticas_rs::{promedio_simple, desviacion_estandar, promedio_movil, calcular_moda};

fn main() {
    let data = "1,2,3,4,5,5,6,7,8,8,8,9,10";

    println!("Promedio simple: {}", promedio_simple(data));
    println!("Desviación estándar: {}", desviacion_estandar(data));
    println!("Promedio móvil (ventana=3): {:?}", promedio_movil(data, 3));

    // Para calcular la moda, convertimos la cadena a un vector de f64.
    let nums: Vec<f64> = data
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect();
    println!("Moda: {:?}", calcular_moda(&nums));
}
