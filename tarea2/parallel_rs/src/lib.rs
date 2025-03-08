use rayon::prelude::*;
use rustatistics_2::{promedio, desviacion_estandar};

/// Procesa las temperaturas para cada ciudad.
/// Para cada tupla (ciudad, temperaturas) calcula el promedio y la desviación estándar.
pub fn process_temperatures(data: Vec<(String, String)>) -> Vec<(String, f64, f64)> {
    data.into_par_iter()
        .map(|(city, temps)| {
            let avg = promedio(&temps).unwrap_or(0.0);
            let std_dev = desviacion_estandar(&temps).unwrap_or(0.0);
            (city, avg, std_dev)
        })
        .collect()
}
