pub fn calcular_promedio_movil(numeros: &Vec<i32>, ventana: usize) -> Vec<f64> {
    let mut promedios = Vec::new();
    if ventana == 0 || ventana > numeros.len() {
        return promedios;
    }

    for i in 0..=(numeros.len() - ventana) {
        let suma: i32 = numeros[i..i + ventana].iter().sum();
        let promedio = suma as f64 / ventana as f64;
        promedios.push(promedio);
    }

    promedios
}

/// Calcula el promedio de números contenidos en una cadena separada por comas.
/// Retorna un Result con el promedio en f64 o un mensaje de error.
pub fn promedio(data: &str) -> Result<f64, &'static str> {
    // Intentamos parsear cada fragmento a f64
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

/// Calcula la desviación estándar de números contenidos en una cadena separada por comas.
/// Retorna un Result con la desviación estándar en f64 o un mensaje de error.
pub fn desviacion_estandar(data: &str) -> Result<f64, &'static str> {
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

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_promedio() {
        let result = promedio("1,2,3,4,5").unwrap();
        assert_eq!(result, 3.0);
    }
    
    #[test]
    fn test_desviacion_estandar() {
        let result = desviacion_estandar("1,2,3,4,5").unwrap();
        let expected = 1.4142135623730951;
        assert!((result - expected).abs() < 1e-6);
    }
}
