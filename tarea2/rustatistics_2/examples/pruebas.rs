use rustatistics_2::{promedio, desviacion_estandar};

fn main() {
    // Datos de ejemplo: cadena de números separados por comas
    let datos = "1,2,3,4,5";
    println!("Datos: {}", datos);

    // Calcular y mostrar el promedio
    match promedio(datos) {
        Ok(prom) => println!("El promedio es: {}", prom),
        Err(e) => println!("Error al calcular el promedio: {}", e),
    }

    // Calcular y mostrar la desviación estándar
    match desviacion_estandar(datos) {
        Ok(desv) => println!("La desviación estándar es: {}", desv),
        Err(e) => println!("Error al calcular la desviación estándar: {}", e),
    }
}
