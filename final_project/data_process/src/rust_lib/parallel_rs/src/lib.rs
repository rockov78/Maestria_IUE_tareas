use pyo3::prelude::*;
use rayon::prelude::*;
/// Crate que expone la función `process_temperatures` a Python (o para uso interno).
/// Este crate procesa, en paralelo, una lista de tuplas `(ciudad, cadena_de_temperaturas)`.
/// Para cada entrada, calcula el promedio y la desviación estándar usando funciones internas.
/// Calcula el promedio de números contenidos en una cadena separada por comas.
/// Retorna un `Result` con el promedio en `f64` o un mensaje de error.
fn calcular_promedio(data: &str) -> Result<f64, &'static str> {
    // Convertir la cadena en un vector de f64
    let numeros: Result<Vec<f64>, _> = data.split(',')
        .map(|s| s.trim().parse::<f64>())
        .collect();
    match numeros {
        Ok(nums) => {
            if nums.is_empty() {
                Ok(0.0)
            } else {
                let suma: f64 = nums.iter().sum();
                Ok(suma / (nums.len() as f64))
            }
        },
        Err(_) => Err("Error al parsear los números"),
    }
}

/// Calcula la desviación estándar de los números contenidos en una cadena separada por comas.
/// Retorna un `Result` con la desviación estándar en `f64` o un mensaje de error.
fn calcular_desviacion_estandar(data: &str) -> Result<f64, &'static str> {
    // Convertir la cadena en un vector de f64
    let numeros: Result<Vec<f64>, _> = data.split(',')
        .map(|s| s.trim().parse::<f64>())
        .collect();
    match numeros {
        Ok(nums) => {
            let n = nums.len();
            if n == 0 {
                return Ok(0.0);
            }
            let promedio: f64 = nums.iter().sum::<f64>() / (n as f64);
            let varianza = nums.iter()
                .map(|x| (*x - promedio).powi(2))
                .sum::<f64>() / (n as f64);
            Ok(varianza.sqrt())
        },
        Err(_) => Err("Error al parsear los números"),
    }
}

/// se usa para pasar a python.
/// Procesa las temperaturas para cada ciudad.
/// Para cada tupla `(ciudad, cadena_de_temperaturas)` calcula el promedio y la desviación estándar.
///
/// # Argumentos
///
/// * `data` - Una lista de tuplas `(ciudad, cadena_de_temperaturas)`.
///
/// # Retorno
///
/// Retorna una lista de tuplas `(ciudad, promedio, desviacion_estandar)`.
#[pyfunction]
fn process_temperatures(data: Vec<(String, String)>) -> Vec<(String, f64, f64)> {
    data.into_par_iter()
        .map(|(city, temps)| {
            let avg = calcular_promedio(&temps).unwrap_or(0.0);
            let std_dev = calcular_desviacion_estandar(&temps).unwrap_or(0.0);
            (city, avg, std_dev)
        })
        .collect()
}


/// A Python module implemented in Rust.
#[pymodule]
fn parallel_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(process_temperatures, m)?)?;
    Ok(())
}
